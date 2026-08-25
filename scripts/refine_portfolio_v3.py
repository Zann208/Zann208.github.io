# V3 interaction refinement trigger
from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

if "PORTFOLIO_SYSTEM_V3" in s:
    print("Portfolio interaction refinement already applied")
    raise SystemExit(0)


def must_replace(old: str, new: str, label: str, count: int = 1):
    global s
    if old not in s:
        raise RuntimeError(f"Expected source not found: {label}")
    s = s.replace(old, new, count)

# Remove legacy visual layers that were overriding the canonical dossier system.
s, n = re.subn(r"\n?/\* HIERARCHY_POLISH_V2 \*/.*?/\* /HIERARCHY_POLISH_V2 \*/\n?", "\n", s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError("Legacy HIERARCHY_POLISH_V2 block not found")
s, n = re.subn(r"\n?/\* RECRUITER_POLISH_V1 \*/.*?/\* /RECRUITER_POLISH_V1 \*/\n?", "\n", s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError("Legacy RECRUITER_POLISH_V1 block not found")

# Rename the canonical design marker.
s = s.replace("/* PORTFOLIO_SYSTEM_V2 — Infrastructure Dossier */", "/* PORTFOLIO_SYSTEM_V3 — Infrastructure Dossier */", 1)
s = s.replace("/* /PORTFOLIO_SYSTEM_V2 */", "/* /PORTFOLIO_SYSTEM_V3 */", 1)

# Stronger but restrained semantic palette for credentials and interaction states.
must_replace(
    "  --accent:#b34d56;--accent-strong:#7a242c;--accent-soft:rgba(179,77,86,.10);",
    "  --accent:#b34d56;--accent-strong:#7a242c;--accent-soft:rgba(179,77,86,.10);\n  --hover:rgba(179,77,86,.075);--success:#86a28d;--progress:#cf6972;--planned:#b9a06a;--member:#8da3bd;",
    "dark interaction tokens",
)
must_replace(
    "  --accent:#7a242c;--accent-strong:#5d171b;--accent-soft:rgba(122,36,44,.07);",
    "  --accent:#7a242c;--accent-strong:#5d171b;--accent-soft:rgba(122,36,44,.07);\n  --hover:rgba(122,36,44,.055);--success:#3f7450;--progress:#7a242c;--planned:#7b6129;--member:#4d6684;",
    "light interaction tokens",
)

# Red/burgundy is now the deliberate hover language in both themes.
must_replace(
    ".nav-links a:hover,.nav-links a.on{color:var(--text);border-bottom-color:var(--accent)}",
    ".nav-links a:hover,.nav-links a.on{color:var(--accent);border-bottom-color:var(--accent)}",
    "navigation hover",
)
must_replace(
    ".tog{border:1px solid var(--line);background:transparent;color:var(--muted);width:32px;height:32px;display:grid;place-items:center;cursor:pointer;margin-left:.25rem}.tog:hover{border-color:var(--line-strong);color:var(--text)}.tog svg{width:14px;height:14px}",
    ".tog{border:1px solid var(--line);background:transparent;color:var(--muted);width:32px;height:32px;display:grid;place-items:center;cursor:pointer;margin-left:.25rem;transition:border-color .18s,color .18s,background .18s}.tog:hover{border-color:var(--accent);color:var(--accent);background:var(--hover)}.tog svg{width:14px;height:14px}",
    "theme toggle hover",
)

# Hero: keep the fixed role, restore only the block cursor interaction, enlarge and refine portrait.
must_replace(
    ".hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:clamp(2.2rem,7vw,5.5rem);align-items:center}",
    ".hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 350px;gap:clamp(2.4rem,6vw,5rem);align-items:center}",
    "hero portrait column",
)
must_replace(
    ".role{font-size:clamp(1.05rem,2.3vw,1.28rem);color:var(--accent);margin-bottom:1.35rem;font-weight:600;min-height:0;font-family:var(--sans)}\n.role .cur{display:none}.lede",
    ".role{font-size:clamp(1.05rem,2.3vw,1.28rem);color:var(--accent);margin-bottom:1.35rem;font-weight:600;min-height:0;font-family:var(--sans)}\n.role::after{content:\"\";display:inline-block;width:.52em;height:.84em;margin-left:.2em;background:var(--accent);vertical-align:-.07em;animation:roleCursor 1.1s steps(1,end) infinite}\n@keyframes roleCursor{0%,48%{opacity:1}49%,100%{opacity:0}}\n.role .cur{display:none}.lede",
    "role block cursor",
)
must_replace(
    ".now{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.25rem;padding-top:1.35rem;border-top:1px solid var(--line)}",
    ".now{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.25rem;padding-top:1.35rem;border-top:1px solid var(--line)}",
    "hero metadata columns",
)
must_replace(
    ".badge{margin:0;border:0;border-top:3px solid var(--accent-strong);background:var(--surface);border-radius:0;overflow:hidden}.b-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--surface-2)}.b-photo img{width:100%;height:100%;object-fit:cover;display:block;transform:none!important}.b-photo::after,.scan,.ret{display:none!important}.b-meta{padding:1rem 0 0;font:500 .72rem/1.75 var(--mono);color:var(--muted)}.b-meta div{display:grid;grid-template-columns:62px 1fr;gap:.6rem}.b-meta b{color:var(--quiet);font-weight:500}.b-meta em{font-style:normal;color:var(--text)}.b-meta .ok{color:var(--accent)}\n@media(max-width:900px){.hero-grid{grid-template-columns:1fr}.badge{max-width:300px}.now{grid-template-columns:1fr 1fr}}",
    ".badge{margin:0;border:1px solid var(--line);border-top:3px solid var(--accent-strong);background:var(--surface);border-radius:4px;overflow:hidden;box-shadow:0 18px 48px rgba(0,0,0,.14);transition:border-color .24s,transform .24s,box-shadow .24s}.badge:hover{border-color:var(--accent);transform:translateY(-2px);box-shadow:0 22px 54px rgba(0,0,0,.19)}.b-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--surface-2)}.b-photo img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1);transition:transform .55s var(--ease)}.badge:hover .b-photo img{transform:scale(1.018)}.b-photo::after,.scan,.ret{display:none!important}.b-meta{padding:1rem .95rem .95rem;font:500 .72rem/1.75 var(--mono);color:var(--muted);border-top:1px solid var(--line)}.b-meta div{display:grid;grid-template-columns:62px 1fr;gap:.6rem}.b-meta b{color:var(--quiet);font-weight:500}.b-meta em{font-style:normal;color:var(--text)}.b-meta .ok{color:var(--accent)}\n@media(max-width:900px){.hero-grid{grid-template-columns:1fr}.badge{max-width:350px}.now{grid-template-columns:1fr 1fr}}",
    "profile image card",
)

# Focus cards: maintain the engineering sheet structure but make interaction visible.
must_replace(
    ".pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.pil{background:transparent;border:0;border-right:1px solid var(--line);border-radius:0;padding:1.5rem 1.5rem 1.5rem 0;margin-right:1.5rem}.pil:last-child{border-right:0;margin-right:0}.pil::after{display:none}.pil .ic{color:var(--accent);display:block;margin-bottom:1rem}.pil .ic svg{width:20px;height:20px}.pil h3{font-size:1rem;margin-bottom:.5rem}.pil p{font-size:.9rem;color:var(--muted);line-height:1.62}.pil:hover,.pil:hover .ic{transform:none!important}\n@media(max-width:760px){.pillars{grid-template-columns:1fr}.pil{border-right:0;border-bottom:1px solid var(--line);margin:0;padding:1.3rem 0}.pil:last-child{border-bottom:0}}",
    ".pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}.pil{background:var(--surface);border:0;border-radius:0;padding:1.45rem;margin:0;position:relative;transition:background .2s,color .2s}.pil::after{content:\"\";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--accent);transform:scaleY(0);transform-origin:bottom;transition:transform .24s var(--ease)}.pil:last-child{margin:0}.pil .ic{color:var(--accent);display:block;margin-bottom:1rem;transition:transform .24s var(--ease)}.pil .ic svg{width:20px;height:20px}.pil h3{font-size:1rem;margin-bottom:.5rem;transition:color .18s}.pil p{font-size:.9rem;color:var(--muted);line-height:1.62}.pil:hover{background:var(--hover)}.pil:hover::after{transform:scaleY(1)}.pil:hover .ic{transform:translateY(-2px)}.pil:hover h3{color:var(--accent)}\n@media(max-width:760px){.pillars{grid-template-columns:1fr}.pil{border:0;margin:0;padding:1.3rem}.pil:last-child{border-bottom:0}}",
    "focus interaction",
)

# Projects and experience get a subtle red hover rather than generic white brightness.
must_replace(
    ".projects{display:flex;flex-direction:column}.proj{display:grid;grid-template-columns:minmax(0,1fr);padding:1.75rem 0;border-top:1px solid var(--line)}.proj:last-child{border-bottom:1px solid var(--line)}.proj:hover{background:none}",
    ".projects{display:flex;flex-direction:column}.proj{display:grid;grid-template-columns:minmax(0,1fr);padding:1.75rem 0;border-top:1px solid var(--line);transition:background .2s,padding-left .24s var(--ease)}.proj:last-child{border-bottom:1px solid var(--line)}.proj:hover{background:var(--hover);padding-left:.45rem}.proj:hover h3{color:var(--accent)}",
    "project hover",
)
must_replace(
    ".exp{display:flex;flex-direction:column}.xp{display:grid;grid-template-columns:180px minmax(0,1fr);gap:1.5rem;padding:1.5rem 0;border-top:1px solid var(--line)}.xp:last-child{border-bottom:1px solid var(--line)}.xp:hover{background:none}",
    ".exp{display:flex;flex-direction:column}.xp{display:grid;grid-template-columns:180px minmax(0,1fr);gap:1.5rem;padding:1.5rem 0;border-top:1px solid var(--line);transition:background .2s,padding-left .24s var(--ease)}.xp:last-child{border-bottom:1px solid var(--line)}.xp:hover{background:var(--hover);padding-left:.45rem}.xp:hover h3{color:var(--accent)}",
    "experience hover",
)

# Credentials: semantic status colors, cleaner marks, and red hover response.
old_creds = ".cred-groups{display:grid;gap:2.2rem}.cred-group-head{margin-bottom:.85rem}.cred-group-head h3{font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;color:var(--accent)}.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;border-top:1px solid var(--line)}.cert{display:flex;align-items:flex-start;gap:.75rem;padding:1rem 1rem 1rem 0;background:transparent;border:0;border-bottom:1px solid var(--line);border-radius:0}.cert .mk{font:.69rem var(--mono);color:var(--quiet);min-width:25px}.cert.done .mk{color:var(--accent)}.cert h4{font-size:.9rem;font-weight:600;margin-bottom:.15rem}.cert span{font:.66rem var(--mono);color:var(--quiet)}"
new_creds = ".cred-groups{display:grid;gap:2.3rem}.cred-group-head{display:flex;align-items:center;gap:.8rem;margin-bottom:.8rem}.cred-group-head::after{content:\"\";height:1px;flex:1;background:var(--line)}.cred-group-head h3{font-size:.76rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);white-space:nowrap}.cred-group:nth-child(1) .cred-group-head h3{color:var(--success)}.cred-group:nth-child(2) .cred-group-head h3{color:var(--member)}.cred-group.path .cred-group-head h3{color:var(--progress)}.cred-group.membership .cred-group-head h3{color:var(--member)}.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1px;background:var(--line);border:1px solid var(--line)}.cert{display:flex;align-items:flex-start;gap:.8rem;padding:1rem;background:var(--surface);border:0;min-height:82px;transition:background .2s}.cert:hover{background:var(--hover)}.cert .mk{font:700 .74rem var(--mono);color:var(--quiet);min-width:30px;transition:color .18s,transform .2s}.cert.done.course .mk,.cert.done.training .mk{color:var(--success)}.cert.prog .mk{color:var(--progress)}.cert.todo .mk{color:var(--planned)}.cert.membership .mk{color:var(--member)}.cert:hover .mk{transform:translateX(2px)}.cert h4{font-size:.9rem;font-weight:650;margin-bottom:.15rem;transition:color .18s}.cert:hover h4{color:var(--accent)}.cert span:not(.mk){font:.66rem var(--mono);color:var(--quiet)}.cert .ieee-mark{min-width:42px;letter-spacing:.025em}.cred-group.membership .certs{grid-template-columns:minmax(280px,560px);justify-content:start}"
must_replace(old_creds, new_creds, "credential system")

# Connect cards use the same hover language, including light mode.
must_replace(
    ".links{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}.lnk{display:block;background:var(--bg);padding:1.35rem;color:var(--text);position:relative}.lnk::before{display:none}.lnk:hover{background:var(--surface);transform:none}.lnk-top{display:flex;align-items:center;gap:.7rem;margin-bottom:.7rem}.lnk-top svg.pf{width:18px;height:18px;color:var(--accent)}.lnk-top b{font-size:.92rem}.lnk-top .ar{margin-left:auto;color:var(--quiet)}",
    ".links{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}.lnk{display:block;background:var(--surface);padding:1.35rem;color:var(--text);position:relative;transition:background .2s}.lnk::before{display:none}.lnk:hover{background:var(--hover);transform:none}.lnk-top{display:flex;align-items:center;gap:.7rem;margin-bottom:.7rem}.lnk-top svg.pf{width:18px;height:18px;color:var(--accent)}.lnk-top b{font-size:.92rem;transition:color .18s}.lnk-top .ar{margin-left:auto;color:var(--quiet);transition:color .18s,transform .2s}.lnk:hover .lnk-top b,.lnk:hover .ar{color:var(--accent)}.lnk:hover .ar{transform:translate(2px,-2px)}",
    "connect hover",
)

# Refine generic buttons and explicit light-mode hover contrast.
must_replace(
    ".cta{display:flex;gap:.7rem;flex-wrap:wrap;margin-bottom:2rem}.btn{font:600 .78rem var(--sans);padding:.7rem 1rem;border:1px solid var(--line-strong);color:var(--text);background:transparent;cursor:pointer;display:inline-flex;align-items:center;gap:.4rem;border-radius:var(--radius);transition:background .18s,border-color .18s,color .18s}.btn:hover{border-color:var(--accent);background:var(--accent-soft)}.btn.pri{background:var(--accent-strong);border-color:var(--accent-strong);color:#fff}.btn.pri:hover{background:var(--accent);border-color:var(--accent)}",
    ".cta{display:flex;gap:.7rem;flex-wrap:wrap;margin-bottom:2rem}.btn{font:600 .78rem var(--sans);padding:.7rem 1rem;border:1px solid var(--line-strong);color:var(--text);background:transparent;cursor:pointer;display:inline-flex;align-items:center;gap:.4rem;border-radius:var(--radius);transition:background .18s,border-color .18s,color .18s,transform .18s}.btn:hover{border-color:var(--accent);background:var(--hover);color:var(--accent);transform:translateY(-1px)}.btn.pri{background:var(--accent-strong);border-color:var(--accent-strong);color:#fff}.btn.pri:hover{background:var(--accent);border-color:var(--accent);color:#fff}",
    "button hover",
)

# Update the existing resume button overrides in the canonical block.
must_replace(
    ".rev{opacity:1;transform:none}.resume-nav-btn{background:var(--accent-strong)!important;border:1px solid var(--accent-strong)!important;color:#fff!important;font:600 .75rem var(--sans)!important;padding:.5rem .72rem!important;border-radius:var(--radius)!important;box-shadow:none!important}.resume-hero-btn{color:var(--text)!important;border-color:var(--line-strong)!important;background:transparent!important}.resume-hero-btn:hover{border-color:var(--accent)!important;background:var(--accent-soft)!important}",
    ".rev{opacity:1;transform:none}.resume-nav-btn{background:var(--accent-strong)!important;border:1px solid var(--accent-strong)!important;color:#fff!important;font:600 .75rem var(--sans)!important;padding:.5rem .72rem!important;border-radius:var(--radius)!important;box-shadow:none!important;transition:background .18s,border-color .18s,transform .18s!important}.resume-nav-btn:hover,.resume-nav-btn[aria-expanded=\"true\"]{background:var(--accent)!important;border-color:var(--accent)!important;color:#fff!important;transform:translateY(-1px)}.resume-hero-btn{color:var(--text)!important;border-color:var(--line-strong)!important;background:transparent!important}.resume-hero-btn:hover{border-color:var(--accent)!important;background:var(--hover)!important;color:var(--accent)!important}",
    "resume button hover",
)

# Replace the old portal CSS (which referenced removed variables) with one clean V3 portal block.
portal_css = r'''/* RESUME_PORTAL_V3 */
.resume-backdrop{position:fixed;inset:0;z-index:120;background:rgba(0,0,0,.72);backdrop-filter:blur(9px);-webkit-backdrop-filter:blur(9px);display:none;align-items:flex-start;justify-content:center;padding:clamp(1rem,4vw,3rem);overflow:auto}
.resume-backdrop.open{display:flex}
.resume-shell{width:min(940px,100%);background:var(--surface);border:1px solid var(--line-strong);border-radius:7px;box-shadow:0 28px 90px rgba(0,0,0,.38);overflow:hidden;animation:resumeIn .24s var(--ease)}
@keyframes resumeIn{from{opacity:0;transform:translateY(10px) scale(.995)}to{opacity:1;transform:none}}
.resume-toolbar{display:flex;align-items:center;gap:1rem;padding:.78rem 1rem;border-bottom:1px solid var(--line);background:var(--surface);position:sticky;top:0;z-index:2}
.resume-toolbar-copy{min-width:0;flex:1}.resume-toolbar-copy b{display:block;font:650 .79rem var(--sans);color:var(--text)}
.resume-actions{display:flex;gap:.45rem;align-items:center}.resume-action{font:600 .72rem var(--sans);padding:.48rem .7rem;border-radius:4px;border:1px solid var(--line-strong);background:transparent;color:var(--muted);cursor:pointer;display:inline-flex;align-items:center;gap:.35rem;transition:color .18s,border-color .18s,background .18s}.resume-action:hover{color:var(--accent);border-color:var(--accent);background:var(--hover)}
.resume-close{width:32px;height:32px;padding:0;display:grid;place-items:center;font-size:1rem}.resume-stage{padding:clamp(.75rem,2vw,1.5rem);background:#d6d6d6}
@media(max-width:820px){.nav-links a[href="#contact"]{display:none}.resume-nav-btn{padding:.42rem .64rem!important}.resume-shell{border-radius:5px}.resume-toolbar{gap:.5rem}.resume-action .action-word{display:none}.resume-stage{padding:.5rem}}
@media(max-width:470px){.resume-backdrop{padding:.35rem}.resume-paper{padding:22px 16px 23px}.resume-actions{gap:.28rem}.resume-action{padding:.45rem .55rem}}
@media print{body.resume-printing>*:not(#resumePortal){display:none!important}body.resume-printing #resumePortal{position:static!important;display:block!important;background:none!important;padding:0!important;overflow:visible!important}body.resume-printing .resume-shell{width:auto!important;border:0!important;box-shadow:none!important;border-radius:0!important}body.resume-printing .resume-toolbar{display:none!important}body.resume-printing .resume-stage{padding:0!important;background:#fff!important}@page{size:A4;margin:0}}
/* /RESUME_PORTAL_V3 */'''
s, n = re.subn(r"/\* RESUME_PORTAL_V1 \*/.*?(?=/\* RESUME_CLEAN_LAYOUT_V1 \*/)", portal_css + "\n\n", s, count=1, flags=re.S)
if n != 1:
    raise RuntimeError("Legacy resume portal block not found")

# Remove recruiter-marketing subtitle from inside the resume portal.
s = s.replace('        <span>1 page · recruiter-ready · updated Aug 2026</span>\n', '', 1)

# Remove the Studying / CCNA hero stat; CCNA remains in credentials and resume content.
s = s.replace('      <div><b data-i="n1">studying</b><em>CCNA</em></div>\n', '', 1)

# Clean status marks. The IEEE mark is now explicit and intentional.
s = s.replace('<span class="mk">[✓]</span>', '<span class="mk" aria-hidden="true">✓</span>')
s = s.replace('<span class="mk">[~]</span>', '<span class="mk" aria-hidden="true">…</span>')
s = s.replace('<span class="mk">[ ]</span>', '<span class="mk" aria-hidden="true">○</span>')
s = s.replace('<span class="mk">[M]</span>', '<span class="mk ieee-mark" aria-hidden="true">IEEE</span>', 1)

path.write_text(s, encoding="utf-8")
print("Portfolio V3 interaction refinement applied")
