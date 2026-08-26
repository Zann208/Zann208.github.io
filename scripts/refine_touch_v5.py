from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "TOUCH_INTERACTION_V5" in s:
    print("Touch Interaction V5 already applied")
    raise SystemExit(0)

if "RESPONSIVE_V4" not in s:
    raise RuntimeError("Expected Responsive V4 baseline before Touch V5")

css = r'''

/* TOUCH_INTERACTION_V5 — persistent touch feedback for mobile/WebViews */
@media (hover:none),(pointer:coarse){
  .touch-hit{background:var(--hover)!important}
  .touch-hit.proj,.touch-hit.xp{padding-left:.35rem}
  .touch-hit.proj h3,.touch-hit.xp h3,.touch-hit.pil h3,.touch-hit.cert h4,.touch-hit.lnk .lnk-top b,.touch-hit.lnk .ar{color:var(--accent)!important}
  .touch-hit.pil::after{transform:scaleY(1)!important}
  .touch-hit.pil .ic{transform:translateY(-2px)!important}
  .touch-hit.cert .mk{transform:translateX(2px)!important}
  .touch-hit.lnk .ar{transform:translate(2px,-2px)!important}
  .touch-hit.badge{border-color:var(--accent)!important;transform:translateY(-1px)}
  .touch-hit.badge .b-photo img{transform:scale(1.006)!important}
  .touch-hit.shead h2{color:var(--accent)!important}
  .touch-hit.shead h2::after{width:100%!important}
  .touch-hit.btn,.touch-hit.resume-action,.touch-hit.tog,.touch-hit.resume-nav-btn{border-color:var(--accent)!important;color:var(--accent)!important;background:var(--hover)!important}
  .touch-hit.btn.pri,.touch-hit.resume-nav-btn{background:var(--accent)!important;color:#fff!important}
}
/* /TOUCH_INTERACTION_V5 */
'''

marker = "/* /PORTFOLIO_SYSTEM_V3 */"
if marker not in s:
    raise RuntimeError("Portfolio style marker not found")
s = s.replace(marker, css + "\n" + marker, 1)

js = r'''
<script>
(function(){
  if(window.__touchInteractionV5) return;
  window.__touchInteractionV5 = true;

  var coarse = false;
  try { coarse = window.matchMedia && (window.matchMedia('(hover: none)').matches || window.matchMedia('(pointer: coarse)').matches); } catch(e) {}
  if(!coarse && !('ontouchstart' in window) && !(navigator.maxTouchPoints > 0)) return;

  var selectors = [
    '.proj','.xp','.pil','.cert','.lnk','.badge','.shead',
    '.btn','.resume-action','.tog','.resume-nav-btn'
  ].join(',');

  var timers = new WeakMap();

  function pulse(el){
    if(!el) return;
    var prior = timers.get(el);
    if(prior) clearTimeout(prior);
    el.classList.add('touch-hit');
    var t = setTimeout(function(){
      el.classList.remove('touch-hit');
      timers.delete(el);
    }, 420);
    timers.set(el,t);
  }

  document.addEventListener('pointerup', function(e){
    if(e.pointerType && e.pointerType !== 'touch' && e.pointerType !== 'pen') return;
    var el = e.target.closest(selectors);
    if(el) pulse(el);
  }, {passive:true});

  document.addEventListener('touchend', function(e){
    var el = e.target.closest && e.target.closest(selectors);
    if(el) pulse(el);
  }, {passive:true});
})();
</script>
'''

end_marker = "\n</body>"
if end_marker not in s:
    raise RuntimeError("Body closing tag not found")
s = s.replace(end_marker, js + end_marker, 1)

path.write_text(s, encoding="utf-8")
print("Applied Touch Interaction V5")
