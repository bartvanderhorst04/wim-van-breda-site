#!/usr/bin/env node
/*
 * scripts/seo-audit.js
 * ---------------------------------------------------------------------
 * Herbruikbare, dependency-vrije SEO-audit voor "Wim van Breda.dc.html".
 *
 * WAT DIT DOET
 * Dit script leest de site NIET via HTTP/crawling (de site is een
 * client-side gerouteerde SPA in één bestand; er bestaat geen los
 * bestand per pagina om te crawlen). In plaats daarvan herbouwt het —
 * met een kopie van dezelfde helperfuncties als Component.meta()/
 * applyJsonLd() in het brondbestand — de volledige paginalijst
 * rechtstreeks uit de brondata (Component.MACHINES, OCCASIONS, BRANDS,
 * RENTAL, NEWS, MAGAZINES, VACANCIES + machine-images.js). Dat is
 * betrouwbaarder dan een browsercrawl over 350+ interne states, en
 * gebruikt exact dezelfde regels als de live site.
 *
 * GEBRUIK
 *   node scripts/seo-audit.js
 *   node scripts/seo-audit.js --write     (schrijft ook seo-pages.csv/json,
 *                                           seo-redirects.csv, sitemap.xml,
 *                                           robots.txt opnieuw weg)
 *
 * BELANGRIJK BIJ ONDERHOUD
 * Als Component.meta() / applyJsonLd() / capTitle() / capDescription() /
 * occasionTitleBase() in "Wim van Breda.dc.html" wijzigen, werk de kopieën
 * hieronder dan mee bij — dit script leest die logica niet live in, het
 * is een bewuste, leesbare kopie (geen require() van de browser-JS, want
 * die hangt af van React/DCLogic/window/document die hier niet bestaan).
 * ---------------------------------------------------------------------
 */
'use strict';
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const HTML_PATH = path.join(ROOT, 'Wim van Breda.dc.html');
const IMAGES_PATH = path.join(ROOT, 'machine-images.js');
const BASE = 'https://www.wimvanbreda.nl';
const WRITE = process.argv.includes('--write');

// ---- 1. Databronnen uit de HTML extraheren -----------------------------
const html = fs.readFileSync(HTML_PATH, 'utf8');

function extractStatement(marker) {
  const start = html.indexOf(marker);
  if (start === -1) throw new Error('marker niet gevonden: ' + marker);
  let i = start + marker.length;
  const n = html.length;
  let depth = 0, inStr = null, escape = false, inLineComment = false, inBlockComment = false;
  const valStart = i;
  while (i < n) {
    const c = html[i];
    if (inLineComment) { if (c === '\n') inLineComment = false; i++; continue; }
    if (inBlockComment) { if (c === '*' && html[i + 1] === '/') { inBlockComment = false; i += 2; continue; } i++; continue; }
    if (inStr) {
      if (escape) escape = false;
      else if (c === '\\') escape = true;
      else if (c === inStr) inStr = null;
      i++; continue;
    }
    if (c === '/' && html[i + 1] === '/') { inLineComment = true; i += 2; continue; }
    if (c === '/' && html[i + 1] === '*') { inBlockComment = true; i += 2; continue; }
    if (c === "'" || c === '"' || c === '`') { inStr = c; i++; continue; }
    if (c === '(' || c === '[' || c === '{') depth++;
    else if (c === ')' || c === ']' || c === '}') depth--;
    else if (c === ';' && depth === 0) return html.slice(valStart, i);
    i++;
  }
  throw new Error('einde bestand bereikt zonder afsluiting voor ' + marker);
}

const DATA = {};
const Component = DATA; // laat Component.X-verwijzingen binnen de data zelf resolven
const NAMES = ['BRANDS_EXTRA', 'BRANDS', 'MACHINES', 'OCCASIONS', 'BRAND_LOGOS', 'BRAND_DETAIL_MEDIA', 'RENTAL', 'WERK_BLOK', 'VACANCIES', 'NEWS', 'MAGAZINES'];
NAMES.forEach(name => {
  const src = extractStatement('static ' + name + ' = ').trim();
  // Wrap in parens: a bare eval() of source starting with "{" is parsed as
  // a block statement, not an object-literal expression.
  // eslint-disable-next-line no-eval
  DATA[name] = eval('(' + src + ')');
});

global.window = {};
require(IMAGES_PATH);
const MACHINE_IMAGES = global.window.MACHINE_IMAGES || {};
function firstPhoto(m) {
  const arr = MACHINE_IMAGES[m.slug] || MACHINE_IMAGES[m.id];
  return (Array.isArray(arr) && arr.length) ? arr[0] : null;
}

// ---- 2. Kopie van de helpers uit Component (zie Wim van Breda.dc.html) -
function capTitle(base, suffix) {
  suffix = suffix || ' | Wim van Breda';
  const full = base + suffix;
  return full.length <= 60 ? full : base;
}
function capDescription(d) {
  if (!d || d.length <= 175) return d;
  const win = d.slice(0, 162);
  const cut = win.lastIndexOf('. ');
  return cut > 80 ? d.slice(0, cut + 1) : d;
}
function occasionTitleBase(displayName) {
  return /\boccasion\s*$/i.test(displayName) ? displayName : displayName + ' occasion';
}
function capFirst(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }
function displayName(m) {
  if (!m) return '';
  const n = m.name || '';
  if (!m.brand) return n;
  return n.toLowerCase().startsWith(m.brand.toLowerCase()) ? n : (m.brand + ' ' + n);
}
function published() { return DATA.MACHINES.filter(m => (!m.pubStatus || m.pubStatus === 'publish') && !m.rentalOnly); }
function rentalPool() { return DATA.MACHINES.filter(m => !m.pubStatus || m.pubStatus === 'publish'); }
function publishedOcc() { return DATA.OCCASIONS.filter(m => !m.pubStatus || m.pubStatus === 'publish'); }

const DUP_OCC_DISTINGUISH = (() => {
  const groups = {};
  publishedOcc().forEach(o => { const key = occasionTitleBase(displayName(o)).toLowerCase(); (groups[key] = groups[key] || []).push(o); });
  const prio = ['bouwjaar', 'serienummer', 'afscherming', 'urenstand', 'voorraadnummer'];
  const specOf = (o, field) => { const hit = (o.specs || []).find(s => String(s.k || '').toLowerCase().replace(/:$/, '') === field); return hit ? String(hit.v) : null; };
  const map = {};
  Object.keys(groups).forEach(key => {
    const list = groups[key];
    if (list.length < 2) return;
    map[key] = prio.find(f => { const vals = list.map(o => specOf(o, f)); return vals.every(v => v) && new Set(vals).size === list.length; }) || null;
  });
  return map;
})();
const DUP_FALLBACK_MIXED = (() => {
  const groups = {};
  rentalPool().concat(publishedOcc()).forEach(m => { if (m.kort) return; const b = displayName(m) + (m.type ? ' — ' + m.type.toLowerCase() : '') + '.'; (groups[b] = groups[b] || []).push(m); });
  const mixed = {};
  Object.keys(groups).forEach(b => { const list = groups[b]; if (list.length < 2) return; if (new Set(list.map(m => m.isOccasion === true)).size > 1) mixed[b] = true; });
  return mixed;
})();
const DUP_KORTS = (() => {
  const seen = {};
  rentalPool().concat(publishedOcc()).forEach(m => { if (m.kort) seen[m.kort] = (seen[m.kort] || 0) + 1; });
  const dup = {};
  Object.keys(seen).forEach(k => { if (seen[k] > 1) dup[k] = true; });
  return dup;
})();
const RENTAL_SLUG = { maaimachines: 'maaimachines', aanbouwwerktuigen: 'aanbouwwerktuigen-maaiarmen-kranen', bosbouw: 'bosbouw' };

function metaForDetail(m) {
  const isOcc = m.isOccasion === true;
  const dn = displayName(m);
  let titleBase = m.id === 'stihl-tuinmachines' ? 'STIHL tuinmachines en gereedschap' : dn;
  if (isOcc) titleBase = occasionTitleBase(titleBase);
  let distinguisher = null;
  if (isOcc) {
    const field = DUP_OCC_DISTINGUISH[titleBase.toLowerCase()];
    if (field) { const hit = (m.specs || []).find(s => String(s.k || '').toLowerCase().replace(/:$/, '') === field); if (hit) distinguisher = { field, value: String(hit.v) }; }
  }
  if (distinguisher) titleBase += ' (' + distinguisher.value + ')';
  const isDupKort = m.kort && DUP_KORTS[m.kort];
  const fallbackBase = dn + (m.type ? ' — ' + m.type.toLowerCase() : '') + '.';
  let base = m.kort ? (isDupKort ? dn + ': ' + m.kort : m.kort) : fallbackBase;
  if (distinguisher) base += ' (' + distinguisher.field + ': ' + distinguisher.value + ')';
  const needsOccClosing = isOcc && !m.kort && DUP_FALLBACK_MIXED[fallbackBase];
  const closing = needsOccClosing ? 'Bekijk deze occasion, specificaties en beschikbaarheid bij Wim van Breda in Geldermalsen.' : 'Bekijk specificaties en toepassingen bij Wim van Breda in Geldermalsen.';
  return { t: capTitle(titleBase), d: capDescription(base + ' ' + closing), u: m.url || ((isOcc ? '/occasions/' : '/machines/') + m.id + '/') };
}

// ---- 3. Volledige pagina-inventaris opbouwen ---------------------------
const pages = [];
function addPage(o) {
  pages.push(Object.assign({ old_url_if_changed: '', notes: '', og_image: '', primary_image: '', schema_type: '', robots: 'index,follow' }, o));
}

addPage({ url: '/', page_type: 'home', slug: '', h1: 'De meest effectieve machines voor berm, sloot, tuin en park', seo_title: 'Machines voor berm, sloot, tuin en park | Wim van Breda', meta_description: 'Wim van Breda levert, onderhoudt en verhuurt professionele machines voor groen-, berm- en terreinbeheer. Nieuw, occasion en verhuur uit Geldermalsen.', canonical: BASE + '/', og_title: 'Machines voor berm, sloot, tuin en park | Wim van Breda', og_description: 'Wim van Breda levert, onderhoudt en verhuurt professionele machines voor groen-, berm- en terreinbeheer. Nieuw, occasion en verhuur uit Geldermalsen.', schema_type: 'Organization,WebSite' });

const FIXED_PAGES = [
  { page: 'machines', url: '/machines/', h1: 'Nieuwe machines', type: 'listing', t: 'Nieuwe machines voor groenbeheer | Wim van Breda', d: 'Bekijk het actuele aanbod nieuwe machines voor groen-, berm- en terreinbeheer. Filter op machinetype en merk en vraag deskundig advies aan.' },
  { page: 'occasions', url: '/occasions/', h1: 'Occasions', type: 'listing', t: 'Occasions: gebruikte machines | Wim van Breda', d: 'Gebruikte machines, technisch nagekeken in onze eigen werkplaats. Filter op merk en type.' },
  { page: 'verhuur', url: '/verhuur/', h1: 'Verhuur', type: 'listing', t: 'Machines huren voor tijdelijke inzet | Wim van Breda', d: 'Huur professionele machines voor groen-, berm- en terreinbeheer. Beschikbare verhuurmachines, korte lijnen en service vanuit Geldermalsen.' },
  { page: 'service', url: '/service/', h1: 'Service, reparatie en onderhoud', type: 'fixed', t: 'Service, reparatie en onderhoud | Wim van Breda', d: 'Reparatie en onderhoud van machines in onze werkplaats in Geldermalsen of bij u op locatie. Servicemonteurs, vervangend materieel en duizenden onderdelen op voorraad.' },
  { page: 'merken', url: '/merken/', h1: 'Merken', type: 'listing', t: 'Merken machines groenbeheer | Wim van Breda', d: 'De merken waarmee Wim van Breda samenwerkt: Herder, Votex, GreenTec en meer. Zoek op merk of filter op machinetype.' },
  { page: 'nieuws', url: '/nieuws/', h1: 'Nieuws', type: 'listing', t: 'Nieuws over machines en het bedrijf | Wim van Breda', d: 'Nieuwe machines in het programma, leveringen, beurzen en ontwikkelingen bij Wim van Breda in Geldermalsen.' },
  { page: 'werken', url: '/werken-bij/', h1: 'Werken bij Wim van Breda', type: 'fixed', t: 'Werken bij Wim van Breda: vacatures | Wim van Breda', d: 'Echte vakmensen met passie voor deze sector. Bekijk de actuele vacatures bij Wim van Breda in Geldermalsen of stuur een open sollicitatie.' },
  { page: 'geleverd', url: '/geleverd/', h1: 'Geleverd', type: 'listing', t: 'Geleverde machines en projecten | Wim van Breda', d: 'Machines die recent hun weg naar onze klanten vonden: maaiarmen, klepelmaaiers, veegmachines en meer, geleverd door Wim van Breda.' },
  { page: 'magazines', url: '/magazines/', h1: 'Magazines', type: 'listing', t: 'Wim van Breda Magazine | Wim van Breda', d: 'Onze magazines met machinenieuws, klantverhalen uit de praktijk en achtergronden over het werk in weg, berm en sloot.' },
  { page: 'over', url: '/over-ons/', h1: 'Over ons', type: 'fixed', t: 'Over ons: bewuste vooruitgang sinds 1957 | Wim van Breda', d: 'Wim van Breda is een familiebedrijf met 45 collega’s, eigen werkplaats en ruim zestig jaar historie. Lees ons verhaal en bekijk de tijdlijn vanaf 1957.' },
  { page: 'contact', url: '/contact/', h1: 'Contact', type: 'fixed', t: 'Contact, openingstijden en route | Wim van Breda', d: 'Bel, WhatsApp of bezoek Wim van Breda aan de Oudenhof 14 in Geldermalsen. Openingstijden, telefoonnummers per afdeling en contactformulier.' }
];
FIXED_PAGES.forEach(fp => addPage({ url: fp.url, page_type: fp.type, slug: fp.url.replace(/^\/|\/$/g, ''), h1: fp.h1, seo_title: fp.t, meta_description: fp.d, canonical: BASE + fp.url, og_title: fp.t, og_description: fp.d }));

DATA.RENTAL.forEach(rc => {
  const slug = RENTAL_SLUG[rc.id] || rc.id;
  const u = '/verhuur/' + slug + '/';
  const t = capTitle(rc.name + ' huren');
  const d = capDescription(rc.intro + ' Bekijk het verhuuraanbod bij Wim van Breda in Geldermalsen.');
  addPage({ url: u, page_type: 'verhuur_categorie', slug, h1: rc.name, seo_title: t, meta_description: d, canonical: BASE + u, og_title: t, og_description: d });
});

DATA.BRANDS.forEach(b => {
  const u = '/merken/' + b.id + '/';
  const t = capTitle(b.name + ' machines');
  const d = capDescription('Bekijk het ' + b.name + '-programma bij Wim van Breda: ' + b.intro.replace(/\.$/, '') + '. Advies, onderdelen en service uit Geldermalsen.');
  const media = DATA.BRAND_DETAIL_MEDIA[b.id] || {};
  const logo = media.logo || DATA.BRAND_LOGOS[b.id] || '';
  addPage({ url: u, page_type: 'merk', slug: b.id, h1: b.name, seo_title: t, meta_description: d, canonical: BASE + u, og_title: t, og_description: d, og_image: media.hero || logo, primary_image: logo, schema_type: '(geen los schema; alleen Organization)' });
});

let machinesWithoutPhoto = 0;
rentalPool().forEach(m => {
  const meta = metaForDetail(m);
  const photo = firstPhoto(m);
  if (!photo) machinesWithoutPhoto++;
  addPage({ url: meta.u, page_type: 'machine', slug: m.id, h1: displayName(m), seo_title: meta.t, meta_description: meta.d, canonical: BASE + meta.u, og_title: meta.t, og_description: meta.d, og_image: photo ? photo.src : '', primary_image: photo ? photo.src : '', schema_type: 'Product,BreadcrumbList',
    notes: [m.rentalOnly ? 'rental-only: niet op /machines/-overzicht, wel eigen detailpagina' : '', (m.pubStatus && m.pubStatus !== 'publish') ? 'pubStatus=' + m.pubStatus : '', !photo ? 'geen foto beschikbaar' : ''].filter(Boolean).join('; ') });
});

let occasionsWithoutPhoto = 0;
publishedOcc().forEach(o => {
  const meta = metaForDetail(o);
  const photo = firstPhoto(o);
  if (!photo) occasionsWithoutPhoto++;
  addPage({ url: meta.u, page_type: 'occasion', slug: o.id.replace(/^occ-/, ''), h1: displayName(o), seo_title: meta.t, meta_description: meta.d, canonical: BASE + meta.u, og_title: meta.t, og_description: meta.d, og_image: photo ? photo.src : '', primary_image: photo ? photo.src : '', schema_type: 'Product,BreadcrumbList', notes: !photo ? 'geen foto beschikbaar' : '' });
});

DATA.NEWS.forEach(a => {
  const t = capTitle(a.title);
  const d = a.metaDescription || capDescription(a.intro || (a.title + '. Lees het volledige bericht op de website van Wim van Breda in Geldermalsen.'));
  const u = '/nieuws/' + a.slug + '/';
  addPage({ url: u, page_type: 'nieuws_item', slug: a.slug, h1: a.title, seo_title: t, meta_description: d, canonical: BASE + u, og_title: t, og_description: d, primary_image: a.img || '', schema_type: 'Article' });
});

DATA.MAGAZINES.forEach(m => {
  const t = capTitle(m.editie + ' (' + m.jaar + ')');
  const d = capDescription(m.tekst);
  const u = '/magazines/' + m.slug + '/';
  addPage({ url: u, page_type: 'magazine', slug: m.slug, h1: m.editie, seo_title: t, meta_description: d, canonical: BASE + u, og_title: t, og_description: d });
});

// JobPosting: alleen op een concrete vacature (nooit "open-sollicitatie",
// dat is geen specifieke functie) en alleen met een echte, van de live
// WordPress-site (wimvanbreda.nl) overgenomen v.datePosted — zie de
// toelichting bij elk record in Component.VACANCIES in de HTML-bron.
// Bewust geen validThrough: Wim van Breda sluit vacatures zelf af.
DATA.VACANCIES.forEach(v => {
  const t = capTitle(capFirst(v.titel.replace(/^Vacature /, '')));
  const d = capDescription(v.kort + ' Solliciteer direct bij Wim van Breda in Geldermalsen.');
  const u = '/werken-bij/' + v.id + '/';
  const hasJobPosting = v.id !== 'open-sollicitatie' && !!v.datePosted;
  // H1 op de vacaturepagina zelf toont v.titel ONgewijzigd (dus mét "Vacature ")
  addPage({
    url: u, page_type: 'vacature', slug: v.id, h1: v.titel, seo_title: t, meta_description: d, canonical: BASE + u, og_title: t, og_description: d,
    schema_type: hasJobPosting ? 'JobPosting' : (v.id === 'open-sollicitatie' ? '(geen JobPosting: open sollicitatie, geen specifieke functie)' : '(geen JobPosting: geen betrouwbare datePosted gevonden op de live site)'),
    notes: hasJobPosting ? 'JobPosting datePosted=' + v.datePosted + ' (overgenomen van live wimvanbreda.nl, Yoast SEO datePublished)' : ''
  });
});

// ---- 4. Audit-checks ----------------------------------------------------
const issues = [];
function issue(type, detail) { issues.push({ type, detail }); }

pages.forEach(p => {
  if (!p.seo_title) issue('missing_title', p.url);
  if (!p.meta_description) issue('missing_description', p.url);
  if (!p.canonical) issue('missing_canonical', p.url);
  if (!p.h1) issue('missing_h1', p.url);
  if (/localhost/i.test(p.canonical)) issue('localhost_in_canonical', p.url);
  if (/\/nieuwe-machines\//i.test(p.canonical)) issue('forbidden_url_pattern', p.url + ' canonical bevat /nieuwe-machines/');
  if (/occasion\s+occasion/i.test(p.seo_title)) issue('double_occasion_word', p.url + ' => ' + p.seo_title);
  if ((p.seo_title || '').length > 65) issue('title_too_long_review', p.url + ' (' + p.seo_title.length + ' tekens) — controleer of dit een bewust lange, natuurlijke titel is');
});
function groupDup(field, type) {
  const map = {};
  pages.forEach(p => { (map[p[field]] = map[p[field]] || []).push(p.url); });
  Object.entries(map).forEach(([k, urls]) => { if (urls.length > 1) issue(type, k.slice(0, 90) + ' => ' + urls.join(' | ')); });
}
groupDup('seo_title', 'duplicate_title');
groupDup('meta_description', 'duplicate_description');
groupDup('canonical', 'duplicate_canonical');
const bySlugType = {};
pages.forEach(p => { const k = p.page_type + '::' + p.slug; (bySlugType[k] = bySlugType[k] || []).push(p.url); });
Object.entries(bySlugType).forEach(([k, urls]) => { if (urls.length > 1) issue('duplicate_slug', k + ' => ' + urls.join(' | ')); });

// JobPosting-specifieke checks: nooit op open-sollicitatie, nooit zonder datePosted.
pages.filter(p => p.page_type === 'vacature').forEach(p => {
  if (p.slug === 'open-sollicitatie' && p.schema_type === 'JobPosting') issue('jobposting_on_open_sollicitatie', p.url);
  if (p.schema_type === 'JobPosting' && !/datePosted=\d{4}-\d{2}-\d{2}/.test(p.notes || '')) issue('jobposting_missing_dateposted', p.url);
});

// ---- 5. Output -----------------------------------------------------------
console.log('=== SEO audit — Wim van Breda ===');
console.log('Totaal pagina\'s:', pages.length);
console.log('Per type:', JSON.stringify(pages.reduce((a, p) => { a[p.page_type] = (a[p.page_type] || 0) + 1; return a; }, {})));
console.log('Machines zonder lokale foto:', machinesWithoutPhoto, 'van', rentalPool().length);
console.log('Occasions zonder lokale foto:', occasionsWithoutPhoto, 'van', publishedOcc().length);
console.log('');
console.log('Gevonden issues:', issues.length);
const byType = issues.reduce((a, i) => { a[i.type] = (a[i.type] || 0) + 1; return a; }, {});
console.log(byType);
if (issues.length) {
  console.log('');
  issues.forEach(i => console.log('  [' + i.type + '] ' + i.detail));
}

if (WRITE) {
  const COLUMNS = ['url', 'page_type', 'slug', 'h1', 'seo_title', 'meta_description', 'canonical', 'og_title', 'og_description', 'og_image', 'robots', 'schema_type', 'primary_image', 'old_url_if_changed', 'notes'];
  const csvEscape = v => { v = (v === undefined || v === null) ? '' : String(v); return /[",\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; };
  const csvLines = [COLUMNS.join(',')].concat(pages.map(p => COLUMNS.map(c => csvEscape(p[c])).join(',')));
  fs.writeFileSync(path.join(ROOT, 'seo-pages.csv'), csvLines.join('\n') + '\n');
  fs.writeFileSync(path.join(ROOT, 'seo-pages.json'), JSON.stringify(pages.map(p => { const o = {}; COLUMNS.forEach(c => o[c] = p[c] || ''); return o; }), null, 2));
  const indexable = pages.filter(p => (p.robots || 'index,follow') === 'index,follow');
  const sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + indexable.map(p => '  <url>\n    <loc>' + p.canonical + '</loc>\n  </url>').join('\n') + '\n</urlset>\n';
  fs.writeFileSync(path.join(ROOT, 'sitemap.xml'), sitemap);
  console.log('');
  console.log('--write: seo-pages.csv, seo-pages.json en sitemap.xml opnieuw weggeschreven in ' + ROOT);
}

process.exitCode = issues.filter(i => i.type !== 'title_too_long_review').length > 0 ? 1 : 0;
