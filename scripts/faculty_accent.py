from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

CSS = r'''/* FACULTY_ACCENT_V1 */
:root{
  --fac:#5d171b;
  --fac-hi:#b94d56;
  --fac-soft:rgba(93,23,27,.24);
  --fac-soft2:rgba(185,77,86,.08);
  --fac-border:rgba(185,77,86,.38);
}
[data-theme="light"]{
  --fac:#5d171b;
  --fac-hi:#741f26;
  --fac-soft:rgba(93,23,27,.11);
  --fac-soft2:rgba(93,23,27,.055);
  --fac-border:rgba(93,23,27,.28);
}

/*
  Identity system
  ---------------
  Black / white carries the layout.
  Engineering CMU burgundy is used as a structural signal: filled markers,
  rails, selected surfaces and primary actions. No glow or pulsing.
*/

.brand span{color:var(--fac-hi)!important;text-shadow:none!important}

/* Section headers stay white. The small terminal marker carries the faculty color. */
.shead h2{color:var(--fg)!important}
.shead h2::before{
  color:#fff!important;
  background:var(--fac)!important;
  display:inline-block;
  padding:.08em .28em .10em;
  margin-right:.26em;
  border-radius:4px;
  font-size:.78em;
  line-height:1;
  letter-spacing:0;
  text-shadow:none!important;
  animation:none!important;
}
.shead .rule{background:linear-gradient(90deg,var(--fac) 0 52px,var(--bd2) 52px,var(--bd) 68%,transparent)!important}
.shead .n{color:var(--fg3)!important;border:1px solid var(--fac-border);background:var(--fac-soft2);padding:.16rem .42rem;border-radius:5px}

/* Selected navigation is intentionally obvious rather than faintly tinted. */
.nav-links a.on{color:#fff!important;background:var(--fac)!important}
.lang button[aria-pressed="true"]{color:#fff!important;background:var(--fac)!important}

/* Hero status remains restrained. */
.pill{color:var(--fg)!important;border-color:var(--fac-border)!important;background:var(--fac-soft2)!important;box-shadow:none!important}
.dot{background:var(--fac-hi)!important;animation:none!important;box-shadow:none!important}
.role .cur{background:var(--fac-hi)!important;box-shadow:none!important}

/* Primary career focus gets a visible burgundy rail and a slightly lifted surface. */
.pil:first-child{
  border-color:var(--fac-border)!important;
  background:linear-gradient(100deg,var(--fac-soft2),var(--s1) 46%,var(--s1))!important;
  box-shadow:inset 3px 0 0 var(--fac)!important;
}
.pil:first-child .ic{color:var(--fac-hi)!important;filter:none!important}
.pil:first-child h3{color:var(--fg)!important}
.pil:not(:first-child) .ic{color:var(--fg2)!important;filter:none!important}
.pil:hover{border-color:var(--bd2)!important;box-shadow:none!important}
.pil:first-child:hover{border-color:var(--fac-border)!important;box-shadow:inset 3px 0 0 var(--fac)!important}

/* NETDES is the flagship project: stronger surface, rail and case-study action. */
.proj:first-child{
  background:linear-gradient(100deg,var(--fac-soft2),transparent 56%)!important;
  box-shadow:inset 4px 0 0 var(--fac)!important;
}
.proj:first-child .idx{
  color:#fff!important;
  background:var(--fac)!important;
  border-radius:5px;
  padding:.12rem .38rem;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-width:2.2rem;
}
.proj:first-child .plinks a:first-child{
  color:#fff!important;
  background:var(--fac)!important;
  border:1px solid var(--fac)!important;
  border-radius:6px;
  padding:.28rem .55rem;
  font-weight:700!important;
}
.proj:first-child .plinks a:first-child:hover{background:#741f26!important;border-color:#741f26!important;color:#fff!important}
.proj h3,.pil h3,.xp h3,.cert h4,.hero h1{color:var(--fg)!important}

/* Credentials: completed state is now a solid mark, not more colored text. */
.cert.done .mk{
  color:#fff!important;
  background:var(--fac)!important;
  border-color:var(--fac)!important;
  text-shadow:none!important;
  box-shadow:none!important;
}
.cert.done:hover{border-color:var(--fac-border)!important;box-shadow:none!important}
.cert.prog .mk,.cert.todo .mk{box-shadow:none!important;text-shadow:none!important}

/* Resume is the strongest recruiter-facing action. */
.resume-nav-btn{background:var(--fac)!important;border-color:var(--fac)!important;color:#fff!important;box-shadow:none!important}
.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:#741f26!important;border-color:#741f26!important;color:#fff!important;box-shadow:none!important}
.resume-hero-btn{color:#fff!important;border-color:var(--fac)!important;background:var(--fac)!important;box-shadow:none!important}
.resume-hero-btn:hover{color:#fff!important;border-color:#741f26!important;background:#741f26!important;box-shadow:none!important}
.resume-toolbar{border-bottom-color:var(--fac-border)!important}

/* Resume paper: burgundy is editorial hierarchy, not decoration. */
.resume-paper .resume-rule{background:var(--fac)!important}
.resume-paper .resume-sec h3{color:var(--fac)!important;border-bottom-color:#d8b9bb!important}
.resume-paper a{color:var(--fac)!important;border-bottom-color:#cfaeb1!important}
.resume-paper a:hover{color:#3f0f12!important;border-bottom-color:var(--fac)!important}
.resume-paper .resume-cred-label{color:var(--fac)!important}
.resume-paper .resume-cred-item::before{background:#666!important}
.resume-paper .resume-project-links a{color:var(--fac)!important;font-weight:700}
.resume-paper .resume-contact-line a{color:#3f3f3f!important;border-bottom-color:#bdbdbd!important}
.resume-paper .resume-contact-line a:hover{color:var(--fac)!important;border-bottom-color:var(--fac)!important}

@media print{
  body.resume-printing .resume-paper .resume-rule{background:#5d171b!important}
  body.resume-printing .resume-paper .resume-sec h3{color:#5d171b!important;border-bottom-color:#caa9ac!important}
  body.resume-printing .resume-paper a{color:#5d171b!important}
  body.resume-printing .resume-paper .resume-cred-label{color:#5d171b!important}
  body.resume-printing .resume-paper .resume-cred-item::before{background:#666!important}
}
/* /FACULTY_ACCENT_V1 */'''

if '/* FACULTY_ACCENT_V1 */' in s:
    s = re.sub(r'/\* FACULTY_ACCENT_V1 \*/.*?/\* /FACULTY_ACCENT_V1 \*/', CSS, s, count=1, flags=re.S)
else:
    if '</style>' not in s:
        raise RuntimeError('Style closing tag not found')
    s = s.replace('</style>', '\n' + CSS + '\n</style>', 1)

assert '--fac:#5d171b' in s
assert 'FACULTY_ACCENT_V1' in s
assert 'animation:none!important' in s
assert '.pil:first-child{' in s
assert '.proj:first-child{' in s
assert '.cert.done .mk{' in s
assert '.resume-paper .resume-sec h3{color:var(--fac)!important' in s

path.write_text(s, encoding='utf-8')
print('Applied stronger Engineering CMU structural hierarchy')
