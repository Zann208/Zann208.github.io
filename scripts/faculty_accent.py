from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

CSS = r'''/* FACULTY_ACCENT_V1 */
:root{
  --fac:#5d171b;
  --fac-hi:#c15a62;
  --fac-title:#d07a80;
  --fac-muted:#946166;
  --fac-soft:rgba(93,23,27,.20);
  --fac-soft2:rgba(193,90,98,.09);
  --fac-border:rgba(193,90,98,.38);
  --fac-glow:rgba(193,90,98,.34);
  --fac-glow-soft:rgba(93,23,27,.18);
}
[data-theme="light"]{
  --fac:#5d171b;
  --fac-hi:#741f26;
  --fac-title:#681a20;
  --fac-muted:#8b5b60;
  --fac-soft:rgba(93,23,27,.10);
  --fac-soft2:rgba(93,23,27,.055);
  --fac-border:rgba(93,23,27,.28);
  --fac-glow:rgba(93,23,27,.18);
  --fac-glow-soft:rgba(93,23,27,.08);
}

/* Portfolio identity: black/white stays dominant; burgundy marks the important bits. */
.brand span{color:var(--fac-hi)!important;text-shadow:none!important}
.shead h2{color:var(--fac-title)!important}
.shead h2::before{color:var(--fac-hi)!important;animation:facultySignal 3.8s ease-in-out infinite}
.shead .rule{background:linear-gradient(90deg,var(--fac-border),rgba(193,90,98,.10),transparent)!important}
.shead .n{color:var(--fac-muted)!important}
.nav-links a.on{color:var(--fac-hi)!important;background:var(--fac-soft2)!important}
.lang button[aria-pressed="true"]{color:var(--fac-hi)!important;background:var(--fac-soft2)!important}
.pill{color:var(--fac-hi)!important;border-color:var(--fac-border)!important;background:var(--fac-soft2)!important;box-shadow:none!important}
.dot{background:var(--fac-hi)!important;animation:facultyDotSignal 4.2s ease-in-out infinite!important}
.role .cur{background:var(--fac-hi)!important;box-shadow:none!important}
.pil .ic{color:var(--fac-hi)!important;filter:none!important}
.pil:hover{border-color:var(--fac-border)!important;box-shadow:none!important}
.proj:first-child .idx{color:var(--fac-hi)!important}
.proj:first-child .plinks a:first-child{color:var(--fac-hi)!important;font-weight:700}
.proj:first-child .plinks a:first-child:hover{color:#fff!important}
.cert.done .mk{color:var(--fac-hi)!important;border-color:var(--fac-border)!important;background:var(--fac-soft2)!important;text-shadow:none!important;box-shadow:none!important}
.cert.done:hover{border-color:var(--fac-border)!important;box-shadow:none!important}

@keyframes facultySignal{
  0%,100%{text-shadow:0 0 3px var(--fac-glow-soft)}
  50%{text-shadow:0 0 7px var(--fac-glow),0 0 14px var(--fac-glow-soft)}
}
@keyframes facultyDotSignal{
  0%,100%{box-shadow:0 0 0 0 rgba(193,90,98,.08),0 0 3px var(--fac-glow-soft)}
  50%{box-shadow:0 0 0 4px rgba(193,90,98,.035),0 0 8px var(--fac-glow)}
}
@media(prefers-reduced-motion:reduce){
  .shead h2::before,.dot{animation:none!important;text-shadow:none!important;box-shadow:none!important}
}

/* Keep content titles white so the section hierarchy stays clear. */
.proj h3,.pil h3,.xp h3,.cert h4,.hero h1{color:var(--fg)!important}

/* Resume is the strongest recruiter action. */
.resume-nav-btn{background:var(--fac)!important;border-color:var(--fac)!important;color:#fff!important;box-shadow:none!important}
.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:#741f26!important;border-color:#741f26!important;color:#fff!important;box-shadow:none!important}
.resume-hero-btn{color:var(--fac-hi)!important;border-color:var(--fac-border)!important;background:var(--fac-soft2)!important;box-shadow:none!important}
.resume-hero-btn:hover{color:#fff!important;border-color:var(--fac-hi)!important;background:var(--fac)!important;box-shadow:none!important}
.resume-toolbar{border-bottom-color:var(--fac-border)!important}

/* Resume paper stays static and print-friendly. */
.resume-paper .resume-rule{background:var(--fac)!important}
.resume-paper .resume-sec h3{color:var(--fac)!important;border-bottom-color:#d8b9bb!important}
.resume-paper a{color:var(--fac)!important;border-bottom-color:#cfaeb1!important}
.resume-paper a:hover{color:#3f0f12!important;border-bottom-color:var(--fac)!important}
.resume-paper .resume-cred-label{color:var(--fac)!important}
.resume-paper .resume-cred-item::before{background:var(--fac)!important}
.resume-paper .resume-project-links a{color:var(--fac)!important;font-weight:700}
.resume-paper .resume-contact-line a{color:#3f3f3f!important;border-bottom-color:#bdbdbd!important}
.resume-paper .resume-contact-line a:hover{color:var(--fac)!important;border-bottom-color:var(--fac)!important}

@media print{
  body.resume-printing .resume-paper .resume-rule{background:#5d171b!important}
  body.resume-printing .resume-paper .resume-sec h3{color:#5d171b!important;border-bottom-color:#caa9ac!important}
  body.resume-printing .resume-paper a{color:#5d171b!important}
  body.resume-printing .resume-paper .resume-cred-label{color:#5d171b!important}
  body.resume-printing .resume-paper .resume-cred-item::before{background:#5d171b!important}
}
/* /FACULTY_ACCENT_V1 */'''

if '/* FACULTY_ACCENT_V1 */' in s:
    s = re.sub(r'/\* FACULTY_ACCENT_V1 \*/.*?/\* /FACULTY_ACCENT_V1 \*/', CSS, s, count=1, flags=re.S)
else:
    if '</style>' not in s:
        raise RuntimeError('Style closing tag not found')
    s = s.replace('</style>', '\n' + CSS + '\n</style>', 1)

assert '--fac:#5d171b' in s
assert '--fac-title:#d07a80' in s
assert '@keyframes facultySignal' in s
assert '@keyframes facultyDotSignal' in s
assert 'prefers-reduced-motion:reduce' in s
assert 'FACULTY_ACCENT_V1' in s
assert '.shead h2{color:var(--fac-title)!important}' in s
assert '.resume-paper .resume-sec h3{color:var(--fac)!important' in s

path.write_text(s, encoding='utf-8')
print('Restored previous Engineering CMU accent treatment')
