from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# Visual hierarchy: preserve the monochrome base, introduce one semantic green
# highlight used only for important/status/interactive elements.
# -----------------------------------------------------------------------------
POLISH = r'''/* HIERARCHY_POLISH_V2 */
:root{
  --hi:#4ade80;
  --hi2:#22c55e;
  --hi-w:rgba(74,222,128,.085);
  --hi-b:rgba(74,222,128,.30);
  --warn:#d6a84b;
  --warn-w:rgba(214,168,75,.08);
  --warn-b:rgba(214,168,75,.26);
}
[data-theme="light"]{
  --hi:#168a4b;
  --hi2:#0f6f3d;
  --hi-w:rgba(22,138,75,.07);
  --hi-b:rgba(22,138,75,.24);
  --warn:#8a641f;
  --warn-w:rgba(138,100,31,.065);
  --warn-b:rgba(138,100,31,.22);
}

/* Keep normal content neutral. Green is reserved for hierarchy and state. */
#prog{background:var(--hi)}
.brand span{color:var(--hi)}
.nav-links a:hover,.nav-links a.on{color:var(--hi);background:var(--hi-w)}
.lang button[aria-pressed="true"]{background:var(--hi-w);color:var(--hi)}
.tog:hover{color:var(--hi);border-color:var(--hi)}
.shead h2::before{color:var(--hi)}
.pill{color:var(--hi);border-color:var(--hi-b);background:var(--hi-w)}
.dot{background:var(--hi)}
@keyframes pulse{0%{box-shadow:0 0 0 0 var(--hi-b)}70%{box-shadow:0 0 0 8px transparent}100%{box-shadow:0 0 0 0 transparent}}
.role .cur{background:var(--hi)}

/* Focus cards: neutral body, meaningful accent only on icon and interaction. */
.pil::after{background:var(--hi)}
.pil:hover{border-color:var(--hi-b)}
.pil .ic{color:var(--hi)}
.tag:hover{color:var(--hi);border-color:var(--hi-b);background:var(--hi-w)}

/* Projects: indexes stay quiet until the item is active; live status is green. */
.proj:hover{background:linear-gradient(90deg,var(--hi-w),transparent 58%)}
.proj:hover .idx{color:var(--hi)}
.plinks a:hover,.plinks a.src:hover{color:var(--hi)}
.badge-s.live{color:var(--hi);background:var(--hi-w);border-color:var(--hi-b)}
.badge-s.wip{color:var(--warn);background:var(--warn-w);border-color:var(--warn-b)}

/* Credentials: card text stays neutral; the mark carries semantic state. */
.cert{position:relative;overflow:hidden;transition:border-color .25s,background .25s,transform .25s var(--ez)}
.cert:hover{transform:translateY(-2px);background:var(--s2)}
.cert.done:hover{border-color:var(--hi-b)}
.cert.done .mk{color:var(--hi);background:var(--hi-w);border:1px solid var(--hi-b)}
.cert.prog .mk{color:var(--warn);background:var(--warn-w);border:1px solid var(--warn-b)}
.cert.todo .mk{color:var(--fg3);background:var(--s2);border:1px solid var(--bd2)}
.cert .mk{min-width:31px;text-align:center;border-radius:5px;padding:.08rem .28rem}
.cert h4{color:var(--fg)}
.cert span:not(.mk){color:var(--fg3)}

/* Connect cards: platform icon is the highlight; descriptive text stays neutral. */
.lnk:hover{border-color:var(--hi-b)}
.lnk:hover::before{opacity:1;background:radial-gradient(400px circle at var(--mx,50%) var(--my,50%),var(--hi-w),transparent 45%)}
.lnk-top svg.pf{color:var(--hi)}
.lnk:hover .ar{color:var(--hi)}
.lnk .h{color:var(--fg2)}

/* Resume is a recruiter-facing action, so it gets the strongest accent treatment. */
.resume-nav-btn{background:var(--hi);border-color:var(--hi);color:#041108;box-shadow:0 7px 22px color-mix(in srgb,var(--hi) 20%,transparent)}
.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{background:var(--hi2);border-color:var(--hi2);color:#031008;box-shadow:0 9px 28px color-mix(in srgb,var(--hi) 28%,transparent)}
.resume-hero-btn{border-color:var(--hi-b);color:var(--hi);background:var(--hi-w)}
.resume-hero-btn:hover{border-color:var(--hi);color:var(--hi);background:color-mix(in srgb,var(--hi-w) 75%,var(--hi) 8%)}
.resume-action:hover{color:var(--hi);border-color:var(--hi-b)}
/* /HIERARCHY_POLISH_V2 */'''

if '/* HIERARCHY_POLISH_V2 */' in s:
    s = re.sub(r'/\* HIERARCHY_POLISH_V2 \*/.*?/\* /HIERARCHY_POLISH_V2 \*/', POLISH, s, count=1, flags=re.S)
else:
    if '</style>' not in s:
        raise RuntimeError('Style closing tag not found')
    s = s.replace('</style>', '\n' + POLISH + '\n\n</style>', 1)

# -----------------------------------------------------------------------------
# Credentials & training: rebuild the section so ordering, statuses and section
# numbering remain clean and deterministic.
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

# Preserve the normal section sequence after earlier scripts accidentally used
# the credential card count as the section number.
s = s.replace('<h2 data-sc>connect</h2><span class="rule"></span><span class="n">07</span>',
              '<h2 data-sc>connect</h2><span class="rule"></span><span class="n">07</span>', 1)

# Guards.
for course in [
    'Networking Basics',
    'Introduction to Modern AI',
    'Exploring Networking with Cisco Packet Tracer',
]:
    assert course in s
assert '/* HIERARCHY_POLISH_V2 */' in s
assert '<h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span>' in s

path.write_text(s, encoding='utf-8')
print('Applied semantic green hierarchy and added completed Cisco courses')
