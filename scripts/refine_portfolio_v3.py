from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "PORTFOLIO_SYSTEM_V3" not in s:
    raise RuntimeError("Expected PORTFOLIO_SYSTEM_V3 baseline")


def ensure(old: str, new: str, label: str):
    global s
    if new in s:
        return
    if old not in s:
        raise RuntimeError(f"Expected source not found: {label}")
    s = s.replace(old, new, 1)

# Section headings: retain the short burgundy rule, expand it to the heading width on hover.
ensure(
    '.shead h2{font-size:clamp(1.45rem,3vw,2rem);font-weight:650}.shead h2::after{content:"";display:block;width:42px;height:2px;background:var(--accent);margin-top:.7rem}',
    '.shead h2{font-size:clamp(1.45rem,3vw,2rem);font-weight:650;justify-self:start;transition:color .22s var(--ease)}.shead h2::after{content:"";display:block;width:42px;max-width:100%;height:2px;background:var(--accent);margin-top:.7rem;transition:width .24s var(--ease)}.shead h2:hover{color:var(--accent)}.shead h2:hover::after{width:100%}',
    'interactive section heading rule',
)

# Profile card: keep the approved lift/zoom interaction while improving metadata hierarchy.
ensure(
    '.badge{margin:0;border:1px solid var(--line);border-top:3px solid var(--accent-strong);background:var(--surface);border-radius:4px;overflow:hidden;box-shadow:0 18px 48px rgba(0,0,0,.14);transition:border-color .24s,transform .24s,box-shadow .24s}.badge:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 22px 54px rgba(0,0,0,.19)}.b-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--surface-2)}.b-photo img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1);transition:transform .55s var(--ease)}.badge:hover .b-photo img{transform:scale(1.018)}.b-photo::after,.scan,.ret{display:none!important}.b-meta{padding:1rem .95rem .95rem;font:500 .72rem/1.75 var(--mono);color:var(--muted);border-top:1px solid var(--line)}.b-meta div{display:grid;grid-template-columns:62px 1fr;gap:.6rem}.b-meta b{color:var(--quiet);font-weight:500}.b-meta em{font-style:normal;color:var(--text)}.b-meta .ok{color:var(--accent)}',
    '.badge{margin:0;border:1px solid var(--line);border-top:3px solid var(--accent-strong);background:var(--surface);border-radius:4px;overflow:hidden;box-shadow:0 18px 48px rgba(0,0,0,.14);transition:border-color .24s,transform .24s,box-shadow .24s}.badge:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 22px 54px rgba(0,0,0,.19)}.b-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--surface-2)}.b-photo img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1);transition:transform .55s var(--ease)}.badge:hover .b-photo img{transform:scale(1.018)}.b-photo::after,.scan,.ret{display:none!important}.b-meta{padding:1rem .95rem .95rem;font:500 .72rem/1.75 var(--mono);color:var(--muted);border-top:1px solid var(--line)}.b-meta div{display:grid;grid-template-columns:62px minmax(0,1fr);gap:.6rem;align-items:start}.b-meta b{color:var(--quiet);font-weight:500}.b-meta em{font-style:normal;color:var(--text);overflow-wrap:anywhere}.b-meta div:nth-child(-n+3) em{color:var(--accent)}.b-meta .ok{color:var(--text)}',
    'profile metadata hierarchy',
)

# Card hover surfaces must stay light/clean instead of exposing gray grid backgrounds.
s = s.replace('.pil:hover{background:var(--hover)}', '.pil:hover{background:color-mix(in srgb,var(--surface) 94%,var(--accent) 6%)}', 1)
s = s.replace('.lnk:hover{background:var(--hover);transform:none}', '.lnk:hover{background:color-mix(in srgb,var(--surface) 94%,var(--accent) 6%);transform:none}', 1)

# Capabilities: restore a subtle interaction without turning the columns into floating cards.
ensure(
    '.stack{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.st{background:transparent;border:0;border-right:1px solid var(--line);border-radius:0;padding:1.25rem 1.5rem 1.25rem 0;margin-right:1.5rem}.st:last-child{border-right:0;margin-right:0}.st h3{font-size:.78rem;color:var(--accent);margin-bottom:.8rem;letter-spacing:.04em;text-transform:uppercase}.st ul{list-style:none;margin:0;padding:0;font-size:.86rem;color:var(--muted);line-height:1.9}',
    '.stack{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.st{background:transparent;border:0;border-right:1px solid var(--line);border-radius:0;padding:1.25rem 1.5rem 1.25rem 0;margin-right:1.5rem;transition:background .2s}.st:last-child{border-right:0;margin-right:0}.st:hover{background:var(--hover)}.st h3{font-size:.78rem;color:var(--accent);margin-bottom:.8rem;letter-spacing:.04em;text-transform:uppercase;transition:color .18s}.st:hover h3{color:var(--progress)}.st ul{list-style:none;margin:0;padding:0;font-size:.86rem;color:var(--muted);line-height:1.9}',
    'capability hover',
)

# Credentials: no empty gray grid cells; semantic completed/progress/member colors; clean hover.
old_creds = '.cred-groups{display:grid;gap:2.3rem}.cred-group-head{display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem}.cred-group-head::after{content:"";height:1px;flex:1;background:var(--line)}.cred-group-head h3{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);white-space:nowrap}.cred-group:nth-child(1) .cred-group-head h3{color:var(--success)}.cred-group:nth-child(2) .cred-group-head h3{color:var(--member)}.cred-group.path .cred-group-head h3{color:var(--progress)}.cred-group.membership .cred-group-head h3{color:var(--member)}.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}.cert{display:flex;align-items:flex-start;gap:.8rem;padding:1rem;background:var(--surface);border:0;min-height:82px;transition:background .2s}.cert:hover{background:var(--hover)}'
new_creds = '.cred-groups{display:grid;gap:2.3rem}.cred-group-head{display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem}.cred-group-head::after{content:"";height:1px;flex:1;background:var(--line)}.cred-group-head h3{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);white-space:nowrap}.cred-group:not(.path):not(.membership) .cred-group-head h3{color:var(--success)}.cred-group.path .cred-group-head h3{color:var(--progress)}.cred-group.membership .cred-group-head h3{color:var(--member)}.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:transparent;border:0}.cert{display:flex;align-items:flex-start;gap:.8rem;padding:1rem;background:var(--surface);border:1px solid var(--line);min-height:82px;transition:background .2s}.cert:hover{background:color-mix(in srgb,var(--surface) 94%,var(--accent) 6%)}'
ensure(old_creds, new_creds, 'credential grid cleanup')

# Contact block is the one intentionally centered section.
ensure(
    '.contact{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:2.6rem 0;text-align:left}.contact::before{display:none}.contact h2{font-size:clamp(1.6rem,4vw,2.5rem);margin-bottom:.7rem}.contact p{color:var(--muted);max-width:56ch;margin:0 0 1.6rem}.soc{display:flex;gap:.65rem;flex-wrap:wrap}.contact #copied{font:.72rem var(--mono);color:var(--accent);margin-top:1rem;height:1.2em;opacity:0}',
    '.contact{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:2.6rem 0;text-align:center}.contact::before{display:none}.contact h2{font-size:clamp(1.6rem,4vw,2.5rem);margin-bottom:.7rem}.contact p{color:var(--muted);max-width:56ch;margin:0 auto 1.6rem}.soc{display:flex;justify-content:center;gap:.65rem;flex-wrap:wrap}.contact #copied{font:.72rem var(--mono);color:var(--accent);margin:1rem auto 0;height:1.2em;opacity:0}',
    'centered contact section',
)

# Navbar resume control: compact and consistent with the rest of the navigation.
ensure(
    '.rev{opacity:1;transform:none}.resume-nav-btn{background:var(--accent-strong)!important;border:1px solid var(--accent-strong)!important;color:#fff!important;font:600 .75rem var(--sans)!important;padding:.5rem .72rem!important;border-radius:var(--radius)!important;box-shadow:none!important;transition:background .18s,border-color .18s,transform .18s!important}.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:var(--accent)!important;border-color:var(--accent)!important;color:#fff!important;transform:translateY(-1px)}.resume-hero-btn{color:var(--text)!important;border-color:var(--line-strong)!important;background:transparent!important}.resume-hero-btn:hover{border-color:var(--accent)!important;background:var(--hover)!important;color:var(--accent)!important}',
    '.rev{opacity:1;transform:none}.resume-nav-btn{height:38px;background:var(--accent-strong);border:1px solid var(--accent-strong);color:#fff;font:600 .75rem var(--sans);padding:0 .72rem;border-radius:var(--radius);box-shadow:none;display:inline-flex;align-items:center;justify-content:center;gap:.35rem;cursor:pointer;white-space:nowrap;transition:background .18s,border-color .18s,transform .18s}.resume-nav-btn svg{width:12px;height:12px;flex:none;transition:transform .2s var(--ease)}.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:var(--accent);border-color:var(--accent);color:#fff;transform:translateY(-1px)}.resume-nav-btn[aria-expanded="true"] svg{transform:rotate(180deg)}.resume-hero-btn{color:var(--text);border-color:var(--line-strong);background:transparent}.resume-hero-btn:hover{border-color:var(--accent);background:var(--hover);color:var(--accent)}',
    'compact resume navigation control',
)
ensure(
    '@media(max-width:820px){.nav-links a[href="#contact"]{display:none}.resume-nav-btn{padding:.42rem .64rem!important}.resume-shell{border-radius:5px}.resume-toolbar{gap:.5rem}.resume-action .action-word{display:none}.resume-stage{padding:.5rem}}',
    '@media(max-width:820px){.nav-in{gap:.8rem}.nav-links a[href="#contact"]{display:none}.resume-nav-btn{height:36px;padding:0 .62rem}.resume-shell{border-radius:5px}.resume-toolbar{gap:.5rem}.resume-action .action-word{display:none}.resume-stage{padding:.5rem}}',
    'compact mobile resume control',
)

# Profile metadata content and localization.
# Accept either the original abbreviated baseline or a builder-expanded intermediate.
s = s.replace('<div><b data-i="b2">program</b><em>Information Systems and Network Engineering · Chiang Mai University</em></div>', '<div><b data-i="b2">program</b><em data-i="b2v">Information Systems and Network Engineering · Chiang Mai University</em></div>', 1)
ensure(
    '<div><b data-i="b2">program</b><em>ISNE · CMU</em></div>',
    '<div><b data-i="b2">program</b><em data-i="b2v">Information Systems and Network Engineering · Chiang Mai University</em></div>',
    'long-form program metadata',
)
s = s.replace('b2:"หลักสูตร",b3:', 'b2:"หลักสูตร",b2v:"วิศวกรรมระบบสารสนเทศและเครือข่าย · มหาวิทยาลัยเชียงใหม่",b3:', 1)
s = s.replace('b2:"专业",b3:', 'b2:"专业",b2v:"信息系统与网络工程 · 清迈大学",b3:', 1)
s = s.replace('avail:"● 可接洽"', 'avail:"可接洽"', 1)

# Remove the planned CompTIA item and make the group label accurate everywhere.
s = re.sub(r'\s*<div class="cert todo"><span class="mk" aria-hidden="true">○</span><div><h4>CompTIA Security\+</h4><span data-i="cPlan">planned</span></div></div>', '', s, count=1)
s = s.replace('<div class="cred-group-head"><h3 data-i="cgPath">In progress / planned</h3></div>', '<div class="cred-group-head"><h3 data-i="cgPath">In progress</h3></div>', 1)
s = s.replace('cgPath:"กำลังเรียน / วางแผน"', 'cgPath:"กำลังเรียน"', 1)
s = s.replace('cgPath:"进行中 / 计划中"', 'cgPath:"进行中"', 1)
s = s.replace(',cPlan:"วางแผนไว้"', '', 1)
s = s.replace(',cPlan:"计划中"', '', 1)

# Guardrails for the approved V3 state.
checks = {
    'brand punctuation': '<a class="brand" href="#top">thu<span>.</span>htoo<span>.</span>zan</a>',
    'long-form program': 'Information Systems and Network Engineering · Chiang Mai University',
    'compact resume button': '.resume-nav-btn{height:38px',
    'centered contact': '.contact{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:2.6rem 0;text-align:center}',
    'heading underline interaction': '.shead h2:hover::after{width:100%}',
}
for label, token in checks.items():
    if token not in s:
        raise RuntimeError(f"Portfolio invariant failed: {label}")
if 'CompTIA Security+' in s:
    raise RuntimeError('CompTIA Security+ should not be present')

path.write_text(s, encoding="utf-8")
print("Portfolio V3 refinements are current")
