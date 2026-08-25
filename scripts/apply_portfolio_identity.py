from pathlib import Path
import re

BURGUNDY = "#7a242c"

HOME_CSS = r'''/* PORTFOLIO_SYSTEM_V2 — Infrastructure Dossier */
:root{
  --bg:#080808;--surface:#0d0d0d;--surface-2:#131313;
  --line:#242424;--line-strong:#3a3a3a;
  --text:#f2f2f0;--muted:#b0b0ad;--quiet:#777773;
  --accent:#b34d56;--accent-strong:#7a242c;--accent-soft:rgba(179,77,86,.10);
  --mono:"JetBrains Mono",ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;
  --sans:"Inter","Noto Sans Thai","Noto Sans SC",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --max:1120px;--radius:5px;--ease:cubic-bezier(.22,1,.36,1);
}
[data-theme="light"]{
  --bg:#f4f3f0;--surface:#fff;--surface-2:#eceae6;
  --line:#d8d5d0;--line-strong:#bbb7b0;
  --text:#181816;--muted:#5c5a56;--quiet:#807d77;
  --accent:#7a242c;--accent-strong:#5d171b;--accent-soft:rgba(122,36,44,.07);
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);font-size:1rem;line-height:1.72;letter-spacing:-.005em;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
::selection{background:var(--accent);color:#fff}
h1,h2,h3,h4{margin:0;font-family:var(--sans);line-height:1.13;letter-spacing:-.035em}
p{margin:0 0 1rem}p:last-child{margin-bottom:0}
img,svg{max-width:100%}.mono{font-family:var(--mono)}
.wrap{max-width:var(--max);margin-inline:auto;padding-inline:clamp(1.25rem,4vw,2.5rem)}
.skip{position:absolute;left:-9999px;top:0;background:var(--accent-strong);color:#fff;padding:.7rem 1rem;z-index:200}.skip:focus{left:0}
.lbl{font:600 .68rem/1.4 var(--mono);letter-spacing:.11em;text-transform:uppercase;color:var(--quiet)}

nav{position:sticky;top:0;z-index:60;background:color-mix(in srgb,var(--bg) 92%,transparent);border-bottom:1px solid var(--line);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px)}
.nav-in{max-width:var(--max);margin:auto;padding:.78rem clamp(1.25rem,4vw,2.5rem);display:flex;align-items:center;gap:1.25rem}
.brand{font-size:.91rem;font-weight:700;letter-spacing:-.02em;white-space:nowrap}.brand span{color:var(--accent)}
.nav-links{display:flex;align-items:center;gap:.1rem;margin-left:auto}
.nav-links a{font-size:.78rem;color:var(--muted);padding:.4rem .58rem;border-bottom:1px solid transparent;transition:color .18s,border-color .18s}
.nav-links a:hover,.nav-links a.on{color:var(--text);border-bottom-color:var(--accent)}
.lang{display:flex;border-left:1px solid var(--line);margin-left:.3rem;padding-left:.5rem}
.lang button{border:0;background:none;color:var(--quiet);font:600 .65rem var(--mono);padding:.38rem .38rem;cursor:pointer}.lang button[aria-pressed="true"]{color:var(--accent)}
.tog{border:1px solid var(--line);background:transparent;color:var(--muted);width:32px;height:32px;display:grid;place-items:center;cursor:pointer;margin-left:.25rem}.tog:hover{border-color:var(--line-strong);color:var(--text)}.tog svg{width:14px;height:14px}
@media(max-width:820px){.nav-links a:not(.keep){display:none}}

section{padding:clamp(4rem,8vw,6.5rem) 0;scroll-margin-top:64px}
.shead{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:1.2rem;margin-bottom:2rem}
.shead h2{font-size:clamp(1.45rem,3vw,2rem);font-weight:650}.shead h2::after{content:"";display:block;width:42px;height:2px;background:var(--accent);margin-top:.7rem}
.shead .rule{height:1px;background:var(--line)}.shead .n{display:none}
.sub{color:var(--muted);font-size:.96rem;max-width:66ch;margin:-.8rem 0 2rem}

.hero{padding-top:clamp(4.4rem,9vw,7rem);padding-bottom:clamp(3.5rem,7vw,5.5rem)}
.hero-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:clamp(2.2rem,7vw,5.5rem);align-items:center}
.availability,.pill{display:inline-block;color:var(--accent);font:600 .72rem var(--mono);letter-spacing:.08em;text-transform:uppercase;border-left:2px solid var(--accent);padding:.12rem 0 .12rem .65rem;margin-bottom:1.5rem;background:none!important;border-radius:0!important}
.dot{display:none}.hero h1{font-size:clamp(3rem,8vw,5.7rem);font-weight:650;letter-spacing:-.065em;margin-bottom:.7rem}
.role{font-size:clamp(1.05rem,2.3vw,1.28rem);color:var(--accent);margin-bottom:1.35rem;font-weight:600;min-height:0;font-family:var(--sans)}
.role .cur{display:none}.lede{font-size:clamp(1.03rem,1.8vw,1.15rem);color:var(--muted);max-width:60ch;margin-bottom:2rem}.lede strong{color:var(--text)}
.cta{display:flex;gap:.7rem;flex-wrap:wrap;margin-bottom:2rem}.btn{font:600 .78rem var(--sans);padding:.7rem 1rem;border:1px solid var(--line-strong);color:var(--text);background:transparent;cursor:pointer;display:inline-flex;align-items:center;gap:.4rem;border-radius:var(--radius);transition:background .18s,border-color .18s,color .18s}.btn:hover{border-color:var(--accent);background:var(--accent-soft)}.btn.pri{background:var(--accent-strong);border-color:var(--accent-strong);color:#fff}.btn.pri:hover{background:var(--accent);border-color:var(--accent)}
.now{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.25rem;padding-top:1.35rem;border-top:1px solid var(--line)}.now div{display:flex;flex-direction:column;gap:.2rem}.now b{font:600 .65rem var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--quiet)}.now em{font-style:normal;font-size:.84rem;color:var(--text)}
.badge{margin:0;border:0;border-top:3px solid var(--accent-strong);background:var(--surface);border-radius:0;overflow:hidden}.b-photo{position:relative;aspect-ratio:4/5;overflow:hidden;background:var(--surface-2)}.b-photo img{width:100%;height:100%;object-fit:cover;display:block;transform:none!important}.b-photo::after,.scan,.ret{display:none!important}.b-meta{padding:1rem 0 0;font:500 .72rem/1.75 var(--mono);color:var(--muted)}.b-meta div{display:grid;grid-template-columns:62px 1fr;gap:.6rem}.b-meta b{color:var(--quiet);font-weight:500}.b-meta em{font-style:normal;color:var(--text)}.b-meta .ok{color:var(--accent)}
@media(max-width:900px){.hero-grid{grid-template-columns:1fr}.badge{max-width:300px}.now{grid-template-columns:1fr 1fr}}

.two{display:grid;grid-template-columns:1.35fr .85fr;gap:clamp(2rem,5vw,4rem);align-items:start}.two p{color:var(--muted)}
.card,.facts{background:transparent;border:0;border-left:2px solid var(--accent-strong);border-radius:0;padding:0 0 0 1.25rem}.facts dl{margin:0;font-size:.88rem}.facts dt{font:600 .65rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--quiet);margin-top:1rem}.facts dt:first-child{margin-top:0}.facts dd{margin:.15rem 0 0;color:var(--text)}.facts .foot{font:.68rem var(--mono);color:var(--muted);margin:1rem 0 0;padding-top:.8rem;border-top:1px solid var(--line)}
@media(max-width:840px){.two{grid-template-columns:1fr}}

.pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.pil{background:transparent;border:0;border-right:1px solid var(--line);border-radius:0;padding:1.5rem 1.5rem 1.5rem 0;margin-right:1.5rem}.pil:last-child{border-right:0;margin-right:0}.pil::after{display:none}.pil .ic{color:var(--accent);display:block;margin-bottom:1rem}.pil .ic svg{width:20px;height:20px}.pil h3{font-size:1rem;margin-bottom:.5rem}.pil p{font-size:.9rem;color:var(--muted);line-height:1.62}.pil:hover,.pil:hover .ic{transform:none!important}
@media(max-width:760px){.pillars{grid-template-columns:1fr}.pil{border-right:0;border-bottom:1px solid var(--line);margin:0;padding:1.3rem 0}.pil:last-child{border-bottom:0}}

.projects{display:flex;flex-direction:column}.proj{display:grid;grid-template-columns:minmax(0,1fr);padding:1.75rem 0;border-top:1px solid var(--line)}.proj:last-child{border-bottom:1px solid var(--line)}.proj:hover{background:none}.proj .idx{display:none}.proj-top{display:flex;align-items:baseline;gap:.75rem;flex-wrap:wrap;margin-bottom:.55rem}.proj-top h3{font-size:1.18rem;font-weight:650}.proj p{font-size:.94rem;color:var(--muted);max-width:74ch;margin-bottom:.85rem}.badge-s{font:600 .64rem var(--mono);text-transform:uppercase;letter-spacing:.07em;color:var(--quiet);padding:0;border:0;background:none!important}.badge-s.live{color:var(--accent)}.plinks{display:flex;gap:1rem;flex-wrap:wrap;margin:.3rem 0 .85rem}.plinks a{font-size:.82rem;font-weight:600;color:var(--text);border-bottom:1px solid var(--line-strong);padding-bottom:.08rem}.plinks a:hover{color:var(--accent);border-bottom-color:var(--accent)}.plinks a.src{color:var(--muted)}.tags{display:flex;flex-wrap:wrap;gap:.55rem}.tag{font:500 .68rem var(--mono);color:var(--quiet);padding:0;border:0}.tag+.tag::before{content:"/";margin-right:.55rem;color:var(--line-strong)}

.exp{display:flex;flex-direction:column}.xp{display:grid;grid-template-columns:180px minmax(0,1fr);gap:1.5rem;padding:1.5rem 0;border-top:1px solid var(--line)}.xp:last-child{border-bottom:1px solid var(--line)}.xp:hover{background:none}.xp .when{font:.78rem var(--mono);color:var(--muted);padding-top:.15rem}.xp .when i{display:block;font-style:normal;font-size:.63rem;color:var(--quiet);text-transform:uppercase;letter-spacing:.08em;margin-top:.2rem}.xp h3{font-size:1.05rem}.xp .org{font-size:.82rem;color:var(--accent);margin-top:.25rem;display:block}.xp p{font-size:.92rem;color:var(--muted);margin:.55rem 0 0;max-width:70ch}@media(max-width:660px){.xp{grid-template-columns:1fr;gap:.35rem}}

.stack{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.st{background:transparent;border:0;border-right:1px solid var(--line);border-radius:0;padding:1.25rem 1.5rem 1.25rem 0;margin-right:1.5rem}.st:last-child{border-right:0;margin-right:0}.st h3{font-size:.78rem;color:var(--accent);margin-bottom:.8rem;letter-spacing:.04em;text-transform:uppercase}.st ul{list-style:none;margin:0;padding:0;font-size:.86rem;color:var(--muted);line-height:1.9}.st li{display:block}.st li::before{content:"—";color:var(--quiet);margin-right:.45rem}.note{font-size:.88rem;color:var(--quiet);margin-top:1.4rem;border-left:2px solid var(--line-strong);padding-left:1rem}@media(max-width:760px){.stack{grid-template-columns:1fr}.st{border-right:0;border-bottom:1px solid var(--line);margin:0;padding:1.1rem 0}.st:last-child{border-bottom:0}}

.cred-groups{display:grid;gap:2.2rem}.cred-group-head{margin-bottom:.85rem}.cred-group-head h3{font-size:.78rem;letter-spacing:.05em;text-transform:uppercase;color:var(--accent)}.certs{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;border-top:1px solid var(--line)}.cert{display:flex;align-items:flex-start;gap:.75rem;padding:1rem 1rem 1rem 0;background:transparent;border:0;border-bottom:1px solid var(--line);border-radius:0}.cert .mk{font:.69rem var(--mono);color:var(--quiet);min-width:25px}.cert.done .mk{color:var(--accent)}.cert h4{font-size:.9rem;font-weight:600;margin-bottom:.15rem}.cert span{font:.66rem var(--mono);color:var(--quiet)}

.links{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line)}.lnk{display:block;background:var(--bg);padding:1.35rem;color:var(--text);position:relative}.lnk::before{display:none}.lnk:hover{background:var(--surface);transform:none}.lnk-top{display:flex;align-items:center;gap:.7rem;margin-bottom:.7rem}.lnk-top svg.pf{width:18px;height:18px;color:var(--accent)}.lnk-top b{font-size:.92rem}.lnk-top .ar{margin-left:auto;color:var(--quiet)}.lnk .h{font:.73rem var(--mono);color:var(--accent);display:block;margin-bottom:.45rem}.lnk .d{font-size:.88rem;color:var(--muted)}.lnk .st8{font:.63rem var(--mono);text-transform:uppercase;letter-spacing:.07em;color:var(--quiet);margin-top:.7rem;display:block}@media(max-width:620px){.links{grid-template-columns:1fr}}
.contact{border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:2.6rem 0;text-align:left}.contact::before{display:none}.contact h2{font-size:clamp(1.6rem,4vw,2.5rem);margin-bottom:.7rem}.contact p{color:var(--muted);max-width:56ch;margin:0 0 1.6rem}.soc{display:flex;gap:.65rem;flex-wrap:wrap}.contact #copied{font:.72rem var(--mono);color:var(--accent);margin-top:1rem;height:1.2em;opacity:0}.contact #copied.show{opacity:1}
footer{border-top:1px solid var(--line);padding:2rem 0}.foot{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font:.66rem var(--mono);color:var(--quiet)}
.rev{opacity:1;transform:none}.resume-nav-btn{background:var(--accent-strong)!important;border:1px solid var(--accent-strong)!important;color:#fff!important;font:600 .75rem var(--sans)!important;padding:.5rem .72rem!important;border-radius:var(--radius)!important;box-shadow:none!important}.resume-hero-btn{color:var(--text)!important;border-color:var(--line-strong)!important;background:transparent!important}.resume-hero-btn:hover{border-color:var(--accent)!important;background:var(--accent-soft)!important}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation:none!important;transition:none!important}}
@media print{nav,.cta{display:none!important}}
/* /PORTFOLIO_SYSTEM_V2 */
'''

RESUME_ACCENT = r'''/* RESUME_ACCENT_V2 */
.resume-paper .resume-rule{background:#7a242c!important}
.resume-paper .resume-sec h3{color:#7a242c!important;border-bottom-color:#d8b9bb!important}
.resume-paper a,.resume-paper .resume-cred-label,.resume-paper .resume-project-links a{color:#7a242c!important}
.resume-paper .resume-cred-item::before{background:#7a242c!important}
.resume-toolbar{border-bottom-color:rgba(179,77,86,.35)!important}
@media print{body.resume-printing .resume-paper .resume-rule{background:#7a242c!important}body.resume-printing .resume-paper .resume-sec h3,body.resume-printing .resume-paper a,body.resume-printing .resume-paper .resume-cred-label{color:#7a242c!important}}
/* /RESUME_ACCENT_V2 */'''

NETDES_CSS = r'''/* NETDES_DOSSIER_V2 */
:root{--bg:#080808;--surface:#0e0e0e;--surface2:#141414;--line:#272727;--line2:#3b3b3b;--fg:#f1f1ef;--fg2:#b2b2af;--fg3:#787874;--accent:#b34d56;--accent2:#7a242c;--mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--sans:"Inter","Noto Sans Thai","Noto Sans SC",system-ui,-apple-system,"Segoe UI",sans-serif;--max:1040px;--text:740px}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.72;-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}.wrap{width:min(var(--max),calc(100% - 2.5rem));margin:auto}
.top{position:sticky;top:0;z-index:20;border-bottom:1px solid var(--line);background:rgba(8,8,8,.92);backdrop-filter:blur(10px)}.top-in{min-height:58px;display:flex;align-items:center;gap:16px}.brand{font-size:13px;font-weight:700;white-space:nowrap}.brand span{color:var(--accent)}.top-links{margin-left:auto;display:flex;align-items:center;gap:6px}.top-links a,.lang button{font:600 11px var(--sans);border:0;background:transparent;color:var(--fg2);padding:7px 8px;cursor:pointer;border-bottom:1px solid transparent}.top-links a:hover,.lang button:hover,.lang button[aria-pressed="true"]{color:var(--fg);border-bottom-color:var(--accent)}.lang{display:flex;gap:2px;border-left:1px solid var(--line);padding-left:5px}
.hero{padding:92px 0 62px;border-bottom:1px solid var(--line)}.eyebrow{font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent);margin-bottom:18px;border-left:2px solid var(--accent);padding-left:9px}h1,h2,h3{margin:0;font-family:var(--sans);letter-spacing:-.04em;line-height:1.14}h1{font-size:clamp(48px,9vw,92px);margin-bottom:14px;font-weight:650}.hero h1 span{color:var(--accent);font-weight:400}.hero-lede{font-size:clamp(18px,2.5vw,22px);color:var(--fg2);max-width:760px;margin:0 0 28px}.hero-lede strong{color:var(--fg)}.actions{display:flex;gap:9px;flex-wrap:wrap}.btn{display:inline-flex;align-items:center;gap:7px;font:600 12px var(--sans);border:1px solid var(--line2);padding:9px 13px;border-radius:4px}.btn.primary{background:var(--accent2);color:#fff;border-color:var(--accent2)}.btn:hover{border-color:var(--accent);background:rgba(179,77,86,.08)}
.facts{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-top:44px}.fact{padding:18px 18px 18px 0;border-right:1px solid var(--line);margin-right:18px}.fact:last-child{border-right:0;margin-right:0}.fact b{display:block;font:650 22px var(--sans);color:var(--fg);margin-bottom:3px}.fact span{font:500 10px var(--mono);color:var(--fg3);text-transform:uppercase;letter-spacing:.07em}
main{padding-bottom:90px}.sec{padding:66px 0;border-bottom:1px solid var(--line)}.sec-grid{display:grid;grid-template-columns:190px minmax(0,var(--text));gap:56px;align-items:start}.sec-no{font:600 11px var(--mono);color:var(--accent);letter-spacing:.07em;text-transform:uppercase;position:sticky;top:82px}.sec-no b{display:none}.sec h2{font-size:clamp(27px,4vw,39px);margin-bottom:22px}.sec h3{font-size:18px;margin:30px 0 11px}.copy{color:var(--fg2);font-size:16px}.copy p{margin:0 0 16px}.copy strong{color:var(--fg)}
.flow{display:grid;grid-template-columns:repeat(5,1fr);margin-top:28px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.step{padding:15px 14px 15px 0;border-right:1px solid var(--line);margin-right:14px}.step:last-child{border-right:0;margin-right:0}.step b{display:block;font-size:12px;margin-bottom:6px;color:var(--fg)}.step span{display:block;color:var(--fg3);font-size:12px;line-height:1.45}.proof{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);border:1px solid var(--line);margin-top:24px}.box{background:var(--bg);padding:18px}.box-label{font:600 10px var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}.box p{margin:0;color:var(--fg2);font-size:14px}pre{margin:0;background:var(--surface);border:0;border-left:2px solid var(--accent2);padding:15px;overflow:auto;color:#dededb;font:12.5px/1.65 var(--mono)}.verify{margin-top:10px}
.logic{display:grid;gap:0;margin:24px 0;border-top:1px solid var(--line)}.logic div{display:block;border-bottom:1px solid var(--line);padding:14px 0}.logic div::before{display:none}.logic b{display:block;font:600 14px var(--sans);margin-bottom:3px;color:var(--fg)}.logic span{color:var(--fg2);font-size:14px}.callout{border-left:2px solid var(--accent2);background:transparent;padding:4px 0 4px 17px;margin:26px 0;color:var(--fg2)}.callout strong{color:var(--fg)}.code-note{font:500 11px var(--mono);color:var(--fg3);margin:9px 0 0}.next{display:grid;gap:0;margin-top:20px;border-top:1px solid var(--line)}.next div{border-bottom:1px solid var(--line);padding:12px 0;color:var(--fg2);font-size:14px}.next b{color:var(--accent);font-size:12px;margin-right:5px}.footer{padding:38px 0 50px;color:var(--fg3);font:500 11px var(--mono);display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}[data-lang-panel]{display:none}[data-lang-panel].on{display:block}
@media(max-width:820px){.top-links>a:not(.source){display:none}.facts{grid-template-columns:1fr 1fr}.sec-grid{grid-template-columns:1fr;gap:15px}.sec-no{position:static}.flow{grid-template-columns:1fr 1fr}.proof{grid-template-columns:1fr}}
@media(max-width:520px){.wrap{width:min(var(--max),calc(100% - 1.5rem))}.hero{padding-top:58px}.brand{font-size:11px}.lang button{padding:6px}.facts{grid-template-columns:1fr}.fact{border-right:0;border-bottom:1px solid var(--line);margin:0}.flow{grid-template-columns:1fr}.step{border-right:0;border-bottom:1px solid var(--line);margin:0}.actions{display:grid}.btn{justify-content:center}}
/* /NETDES_DOSSIER_V2 */'''


def migrate_home(path: Path):
    s = path.read_text(encoding="utf-8")
    # Replace the entire legacy site-design layer while preserving the resume portal CSS.
    s = re.sub(r'<style>.*?(?=/\* RESUME_PORTAL_V1 \*/)', '<style>\n' + HOME_CSS + '\n', s, count=1, flags=re.S)
    # Replace the old layered faculty override with a small resume-only identity accent.
    s = re.sub(r'/\* FACULTY_ACCENT_V1 \*/.*?/\* /FACULTY_ACCENT_V1 \*/', RESUME_ACCENT, s, count=1, flags=re.S)

    # Remove decorative AI/dev-template UI artifacts.
    s = re.sub(r'\n?<div id="spot"[^>]*></div>', '', s)
    s = re.sub(r'\n?<div id="prog"[^>]*></div>', '', s)
    s = s.replace('<span class="pill"><span class="dot"></span><span data-i="pill">Open to internships · 2027</span></span>', '<span class="availability" data-i="pill">Open to internships · 2027</span>')
    s = re.sub(r'<span class="scan"[^>]*></span>', '', s)
    s = re.sub(r'<span class="ret [^"]+"[^>]*></span>', '', s)
    s = re.sub(r'<span class="n">\d+</span>', '', s)
    s = re.sub(r'\s*<span class="idx">\d+</span>', '', s)

    # Human/editorial terminology instead of terminal cosplay.
    s = s.replace('<a href="#about" data-sc>whoami</a>', '<a href="#about" data-sc>profile</a>')
    s = s.replace('<div class="shead"><h2 data-sc>whoami</h2>', '<div class="shead"><h2 data-sc>profile</h2>')
    s = s.replace('<div class="shead"><h2 data-sc>focus</h2>', '<div class="shead"><h2 data-sc>engineering focus</h2>')
    s = s.replace('<div class="shead"><h2 data-sc>work</h2>', '<div class="shead"><h2 data-sc>selected work</h2>')
    s = s.replace('<div class="shead"><h2 data-sc>core skills</h2>', '<div class="shead"><h2 data-sc>capabilities</h2>')

    # Static professional role: keep language switching, remove typewriter behavior.
    s = re.sub(r'<p class="role" id="role"[^>]*></p>', '<p class="role" id="role">Network Engineering · Infrastructure · Security</p>', s, count=1)
    s = re.sub(r'\n\s*/\* typing headline \*/.*?(?=\n\n\s*/\* ── i18n:)', '\n\n  /* professional role */\n  var el = document.getElementById(\'role\');\n  var ROLES = [\'Network Engineering · Infrastructure · Security\'];\n', s, count=1, flags=re.S)
    s = s.replace("    if (reduce && el) el.firstChild ? el.firstChild.nodeValue = ROLES[0] : el.textContent = ROLES[0];", "    if (el) el.textContent = ROLES[0];")
    s = re.sub(r'\n\s*/\* text scramble \*/.*?(?=\n\s*/\* reveal \*/)', '\n', s, count=1, flags=re.S)
    s = re.sub(r'\n\s*/\* scroll progress \*/.*?(?=\n\s*/\* spotlight \+ card glow \*/)', '\n', s, count=1, flags=re.S)
    s = re.sub(r'\n\s*/\* spotlight \+ card glow \*/.*?(?=\n\s*/\* copy email \*/)', '\n', s, count=1, flags=re.S)
    # Reveal remains, but without scramble callbacks.
    s = re.sub(r'\n\s*var h = e\.target\.querySelector\(\'h2\[data-sc\]\'\);\n\s*if\(h\) setTimeout\(function\(\)\{ scramble\(h\); \}, 200\);', '', s)

    path.write_text(s, encoding="utf-8")


def migrate_netdes(path: Path):
    s = path.read_text(encoding="utf-8")
    s = re.sub(r'<style>.*?</style>', '<style>\n' + NETDES_CSS + '\n</style>', s, count=1, flags=re.S)
    # Remove decorative ordinal numbering from every translated panel.
    s = re.sub(r'<div class="sec-no"><b>\d+</b>', '<div class="sec-no">', s)
    # The period after the title is a retained brand punctuation detail; no fake terminal/HUD treatments remain.
    path.write_text(s, encoding="utf-8")


migrate_home(Path("index.html"))
migrate_netdes(Path("projects/netdes/index.html"))
print("Applied Portfolio System V2 to homepage and NETDES case study")
