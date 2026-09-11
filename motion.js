/* ==========================================================================
   Wim van Breda — premium smooth scroll
   Adds: Lenis smooth scroll, tuned to match aichecked.nl exactly. Purely
   additive — does not touch existing markup, text, colors or layout.
   Respects prefers-reduced-motion and disables Lenis on touch devices so
   mobile scroll stays native. Configuration copied 1:1 from aichecked.nl's
   own production /motion.js (same Lenis version, same options).
   ========================================================================== */
(function(){
  'use strict';

  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isCoarsePointer = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;

  function initLenis(){
    if(reduceMotion || isCoarsePointer) return;
    if(typeof window.Lenis !== 'function') return;
    if(window.__wvbLenis) return; // never double-init

    var lenis = new window.Lenis({
      duration: 1.05,
      easing: function(t){ return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.4
    });
    window.__wvbLenis = lenis;

    var rafId;
    function raf(time){
      lenis.raf(time);
      rafId = requestAnimationFrame(raf);
    }
    rafId = requestAnimationFrame(raf);

    // No custom anchor-click handling: navigation on this site is handled
    // entirely by the app's own in-memory router (nav()/window.scrollTo),
    // which keeps working unchanged — Lenis just smooths regular wheel
    // scrolling, it does not intercept programmatic scrollTo calls.
  }

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', initLenis);
  } else {
    initLenis();
  }
})();
