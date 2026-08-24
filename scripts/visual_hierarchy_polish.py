from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# Visual hierarchy: pure monochrome. Emphasis comes from luminance, weight,
# borders and restrained glow — never from an accent hue.
# -----------------------------------------------------------------------------
POLISH = r'''/* HIERARCHY_POLISH_V2 */
:root{
  --hi:#ffffff;
  --hi2:#dddddd;
  --hi-w:rgba(255,255,255,.055);
  --hi-b:rgba(255,255,255,.24);
  --hi-b2:rgba(255,255,255,.40);
  --glow:rgba(255,255,255,.12);
  --glow-soft:rgba(255,255,255,.055);
}
[data-theme="light"]{
  --hi:#111111;
  --hi2:#333333;
  --hi-w:rgba(0,0,0,.045);
  --hi-b:rgba(0,0,0,.19);
  --hi-b2:rgba(0,0,0,.34);
  --glow:rgba(0,0,0,.10);
  --glow-soft:rgba(0,0,0,.045);
}

/* Baseline hierarchy: normal copy stays gray; important content gets brighter. */
#prog{background:var(--hi)}
.brand span{color:var(--hi);font-weight:700;text-shadow:0 0 12px var(--glow)}
.nav-links a:hover,.nav-links a.on{color:var(--hi);background:var(--hi-w)}
.nav-links a.on{font-weight:600}
.lang button[aria-pressed="true"]{background:var(--hi-w);color:var(--hi);font-weight:700}
.tog:hover{color:var(--hi);border-color:var(--hi-b2);box-shadow:0 0 16px var(--glow-soft)}
.shead h2::before{color:var(--hi);font-weight:600;text-shadow:0 0 10px var(--glow-soft)}
.shead .n{color:var(--fg2);font-weight:600;letter-spacing:.14em}
.pill{color:var(--hi);border-color:var(--hi-b);background:var(--hi-w);font-weight:600;box-shadow:inset 0 0 0 1px rgba(255,255,255,.015)}
.dot{background:var(--hi);box-shadow:0 0 10px var(--glow)}
@keyframes pulse{0%{box-shadow:0 0 0 0 var(--hi-b),0 0 8px var(--glow)}70%{box-shadow:0 0 0 8px transparent,0 0 12px var(--glow-soft)}100%{box-shadow:0 0 0 0 transparent,0 0 8px var(--glow)}}
.role .cur{background:var(--hi);box-shadow:0 0 9px var(--glow)}
.now b{color:var(--fg3)}
.now em{color:var(--hi);font-weight:600}

/* Focus: icons and headings are brighter; body copy remains neutral. */
.pil::after{background:var(--hi);box-shadow:0 0 12px var(--glow-soft)}
.pil:hover{border-color:var(--hi-b2);box-shadow:0 14px 36px rgba(0,0,0,.18),0 0 0 1px var(--glow-soft)}
.pil .ic{color:var(--hi);filter:drop-shadow(0 0 5px var(--glow-soft))}
.pil h3{color:var(--hi);font-weight:700}
.tag:hover{color:var(--hi);border-color:var(--hi-b2);background:var(--hi-w);font-weight:600}

/* Projects: titles and live state get contrast, not color. */
.proj{position:relative}
.proj:hover{background:linear-gradient(90deg,var(--hi-w),transparent 58%)}
.proj:hover .idx{color:var(--hi);font-weight:700;text-shadow:0 0 10px var(--glow-soft)}
.proj h3{color:var(--hi);font-weight:700}
.plinks a{color:var(--fg)}
.plinks a:hover,.plinks a.src:hover{color:var(--hi);text-shadow:0 0 9px var(--glow-soft)}
.badge-s.live{color:var(--hi);background:var(--hi-w);border-color:var(--hi-b2);font-weight:700;box-shadow:0 0 12px var(--glow-soft)}
.badge-s.wip{color:var(--fg2);background:var(--s2);border-color:var(--bd2);font-weight:600}
.badge-s.plan{color:var(--fg3);background:transparent;border-color:var(--bd)}

/* Credentials: completed items are crisp white; progress/planned stay grayscale. */
.cert{position:relative;overflow:hidden;transition:border-color .25s,background .25s,transform .25s var(--ez),box-shadow .25s}
.cert:hover{transform:translateY(-2px);background:var(--s2)}
.cert.done:hover{border-color:var(--hi-b2);box-shadow:0 10px 28px rgba(0,0,0,.18),0 0 18px var(--glow-soft)}
.cert.done .mk{color:var(--hi);background:var(--hi-w);border:1px solid var(--hi-b2);font-weight:800;text-shadow:0 0 9px var(--glow);box-shadow:0 0 12px var(--glow-soft)}
.cert.prog .mk{color:var(--fg2);background:var(--s2);border:1px dashed var(--bd2);font-weight:700}
.cert.todo .mk{color:var(--fg3);background:transparent;border:1px solid var(--bd);font-weight:600}
.cert.membership .mk{font-size:0}
.cert.membership .mk::after{content:"MEM";font-size:var(--t-xs);letter-spacing:.05em}
.cert .mk{min-width:34px;text-align:center;border-radius:5px;padding:.09rem .3rem}
.cert h4{color:var(--hi);font-weight:700;letter-spacing:-.012em}
.cert span:not(.mk){color:var(--fg3)}

/* Connect: icons/labels gain luminance; descriptions remain understated. */
.lnk:hover{border-color:var(--hi-b2);box-shadow:0 12px 32px rgba(0,0,0,.16),0 0 18px var(--glow-soft)}
.lnk:hover::before{opacity:1;background:radial-gradient(400px circle at var(--mx,50%) var(--my,50%),var(--hi-w),transparent 45%)}
.lnk-top svg.pf{color:var(--hi);filter:drop-shadow(0 0 5px var(--glow-soft))}
.lnk-top b{color:var(--hi);font-weight:700}
.lnk:hover .ar{color:var(--hi)}
.lnk .h{color:var(--fg2);font-weight:500}

/* Resume is the clearest recruiter-facing action: solid high-contrast monochrome. */
.resume-nav-btn{background:var(--hi);border-color:var(--hi);color:var(--bg);font-weight:800;box-shadow:0 7px 22px var(--glow-soft)}
.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:var(--hi2);border-color:var(--hi2);color:var(--bg);box-shadow:0 9px 28px var(--glow)}
.resume-hero-btn{border-color:var(--hi-b2);color:var(--hi);background:var(--hi-w);font-weight:700;box-shadow:0 0 14px var(--glow-soft)}
.resume-hero-btn:hover{border-color:var(--hi);color:var(--hi);background:var(--hi-w);box-shadow:0 0 20px var(--glow)}
.resume-action:hover{color:var(--hi);border-color:var(--hi-b2);box-shadow:0 0 14px var(--glow-soft)}
/* /HIERARCHY_POLISH_V2 */'''

if '/* HIERARCHY_POLISH_V2 */' in s:
    s = re.sub(r'/\* HIERARCHY_POLISH_V2 \*/.*?/\* /HIERARCHY_POLISH_V2 \*/', POLISH, s, count=1, flags=re.S)
else:
    if '</style>' not in s:
        raise RuntimeError('Style closing tag not found')
    s = s.replace('</style>', '\n' + POLISH + '\n\n</style>', 1)

# -----------------------------------------------------------------------------
# Credentials & training. Keep the completed Cisco courses and status structure.
# Section number is 06; it is not a card count.
# -----------------------------------------------------------------------------
credentials_section = '''<!-- ═══ CREDENTIALS ═══ -->
<section id="certs" class="wrap rev">
  <div class="shead"><h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span></div>
  <div class="certs">

    <div class="cert done course"><span class="mk">[✓]</span>
      <div><h4>Networking Basics</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>

    <div class="cert done course"><span class="mk">[✓]</span>
      <div><h4>Exploring Networking with Cisco Packet Tracer</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>

    <div class="cert done course"><span class="mk">[✓]</span>
      <div><h4>Introduction to Cybersecurity</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>

    <div class="cert done course"><span class="mk">[✓]</span>
      <div><h4>Ethical Hacker</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>

    <div class="cert done course"><span class="mk">[✓]</span>
      <div><h4>Introduction to Modern AI</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>

    <div class="cert done training"><span class="mk">[✓]</span>
      <div><h4>Practical Network+</h4><span data-i="kNet">KMD College, Yangon · 54 hours</span></div></div>

    <div class="cert done training"><span class="mk">[✓]</span>
      <div><h4>Practical A+</h4><span data-i="kApl">KMD College, Yangon · 40 hours</span></div></div>

    <div class="cert prog"><span class="mk">[~]</span>
      <div><h4>Cisco CCNA</h4><span data-i="cProg">in progress</span></div></div>

    <div class="cert prog"><span class="mk">[~]</span>
      <div><h4>Google Cybersecurity Certificate</h4><span data-i="cProg2">in progress</span></div></div>

    <div class="cert todo"><span class="mk">[ ]</span>
      <div><h4>CompTIA Security+</h4><span data-i="cPlan">planned</span></div></div>

    <div class="cert done membership"><span class="mk">[M]</span>
      <div><h4>IEEE Student Member</h4><span data-i="mIEEE">Institute of Electrical and Electronics Engineers · Student Member · 2026–present</span></div></div>

  </div>
</section>

<!-- ═══ CONNECT ═══ -->'''

pattern = r'<!-- ═══ CREDENTIALS ═══ -->.*?<!-- ═══ CONNECT ═══ -->'
if not re.search(pattern, s, flags=re.S):
    raise RuntimeError('Credentials section not found')
s = re.sub(pattern, credentials_section, s, count=1, flags=re.S)

# Guards: no colored hierarchy may survive this script.
for course in [
    'Networking Basics',
    'Introduction to Modern AI',
    'Exploring Networking with Cisco Packet Tracer',
]:
    assert course in s
assert '/* HIERARCHY_POLISH_V2 */' in s
assert '--hi:#ffffff' in s
assert '#4ade80' not in s
assert '#22c55e' not in s
assert '<h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span>' in s

path.write_text(s, encoding='utf-8')
print('Applied monochrome luminance hierarchy and preserved Cisco credentials')
