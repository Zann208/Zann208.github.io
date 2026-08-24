from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# 4) Credentials: group related items instead of presenting one long flat grid.
# -----------------------------------------------------------------------------
GROUP_CSS = r'''/* RECRUITER_POLISH_V1 */
.cred-groups{display:grid;gap:1.6rem}
.cred-group{display:grid;gap:.7rem}
.cred-group-head{display:flex;align-items:center;gap:.8rem}
.cred-group-head h3{font-family:var(--mono);font-size:var(--t-xs);font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--fg2);white-space:nowrap}
.cred-group-head::after{content:"";height:1px;flex:1;background:var(--bd)}
.cred-group .certs{grid-template-columns:repeat(auto-fit,minmax(258px,1fr))}
.cred-group.path .cert.prog,.cred-group.path .cert.todo{background:var(--s3)}
.cred-group.membership .cert{max-width:560px}

/* Experience titles carry the hierarchy. Descriptions stay plain and factual. */
.xp h3{color:var(--fg);font-weight:700}
.xp .org{color:var(--fg3)}
.xp p{max-width:68ch}
/* /RECRUITER_POLISH_V1 */'''

if '/* RECRUITER_POLISH_V1 */' in s:
    s = re.sub(r'/\* RECRUITER_POLISH_V1 \*/.*?/\* /RECRUITER_POLISH_V1 \*/', GROUP_CSS, s, count=1, flags=re.S)
else:
    s = s.replace('</style>', '\n' + GROUP_CSS + '\n\n</style>', 1)

credentials = '''<!-- ═══ CREDENTIALS ═══ -->
<section id="certs" class="wrap rev">
  <div class="shead"><h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span></div>
  <div class="cred-groups">

    <div class="cred-group">
      <div class="cred-group-head"><h3 data-i="cgCisco">Cisco Networking Academy</h3></div>
      <div class="certs">
        <div class="cert done course"><span class="mk">[✓]</span><div><h4>Networking Basics</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>
        <div class="cert done course"><span class="mk">[✓]</span><div><h4>Exploring Networking with Cisco Packet Tracer</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>
        <div class="cert done course"><span class="mk">[✓]</span><div><h4>Introduction to Cybersecurity</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>
        <div class="cert done course"><span class="mk">[✓]</span><div><h4>Ethical Hacker</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>
        <div class="cert done course"><span class="mk">[✓]</span><div><h4>Introduction to Modern AI</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>
      </div>
    </div>

    <div class="cred-group">
      <div class="cred-group-head"><h3 data-i="cgTraining">Technical training</h3></div>
      <div class="certs">
        <div class="cert done training"><span class="mk">[✓]</span><div><h4>Practical Network+</h4><span data-i="kNet">KMD College, Yangon · 54 hours</span></div></div>
        <div class="cert done training"><span class="mk">[✓]</span><div><h4>Practical A+</h4><span data-i="kApl">KMD College, Yangon · 40 hours</span></div></div>
      </div>
    </div>

    <div class="cred-group path">
      <div class="cred-group-head"><h3 data-i="cgPath">In progress / planned</h3></div>
      <div class="certs">
        <div class="cert prog"><span class="mk">[~]</span><div><h4>Cisco CCNA</h4><span data-i="cProg">in progress</span></div></div>
        <div class="cert prog"><span class="mk">[~]</span><div><h4>Google Cybersecurity Certificate</h4><span data-i="cProg2">in progress</span></div></div>
        <div class="cert todo"><span class="mk">[ ]</span><div><h4>CompTIA Security+</h4><span data-i="cPlan">planned</span></div></div>
      </div>
    </div>

    <div class="cred-group membership">
      <div class="cred-group-head"><h3 data-i="cgMembership">Professional membership</h3></div>
      <div class="certs">
        <div class="cert done membership"><span class="mk">[M]</span><div><h4>IEEE Student Member</h4><span data-i="mIEEE">Institute of Electrical and Electronics Engineers · Student Member · 2026–present</span></div></div>
      </div>
    </div>

  </div>
</section>

<!-- ═══ CONNECT ═══ -->'''

if not re.search(r'<!-- ═══ CREDENTIALS ═══ -->.*?<!-- ═══ CONNECT ═══ -->', s, flags=re.S):
    raise RuntimeError('Credentials section not found')
s = re.sub(r'<!-- ═══ CREDENTIALS ═══ -->.*?<!-- ═══ CONNECT ═══ -->', credentials, s, count=1, flags=re.S)

# Add translations for the new group labels. Keep the Cisco brand name unchanged.
if 'cgTraining:' not in s:
    th_marker = 'cProg:"กำลังเรียน"'
    th_value = 'cgCisco:"Cisco Networking Academy",cgTraining:"การฝึกอบรมด้านเทคนิค",cgPath:"กำลังเรียน / วางแผน",cgMembership:"สมาชิกวิชาชีพ",cProg:"กำลังเรียน"'
    zh_marker = 'cProg:"进行中"'
    zh_value = 'cgCisco:"Cisco Networking Academy",cgTraining:"技术培训",cgPath:"进行中 / 计划中",cgMembership:"专业会员",cProg:"进行中"'
    if th_marker not in s or zh_marker not in s:
        raise RuntimeError('I18N credential markers not found')
    s = s.replace(th_marker, th_value, 1)
    s = s.replace(zh_marker, zh_value, 1)

# -----------------------------------------------------------------------------
# 5) Experience: improve only the role for which the site already has factual
# detail. Do not invent descriptions for sparse historical roles.
# -----------------------------------------------------------------------------
s = re.sub(
    r'<p data-i="x1d">.*?</p>',
    '<p data-i="x1d">Test software, document functional and UX issues, report findings to the owning teams, and follow fixes through resolution.</p>',
    s, count=1, flags=re.S
)
# Keep TH/CN translations aligned with the tighter English sentence.
s = s.replace(
    'x1d:"ทดสอบซอฟต์แวร์และเขียนรายงานผลด้านประสบการณ์ผู้ใช้ แจ้งปัญหาไปยังทีมที่รับผิดชอบ และทำงานร่วมกับทีมเหล่านั้นจนกว่าปัญหาจะได้รับการแก้ไข"',
    'x1d:"ทดสอบซอฟต์แวร์ บันทึกปัญหาด้านฟังก์ชันและ UX ส่งผลการทดสอบให้ทีมที่รับผิดชอบ และติดตามการแก้ไขจนเสร็จ"'
)
s = s.replace(
    'x1d:"测试软件并撰写用户体验报告，将问题反馈给相应团队，并与这些团队协作直至问题解决。"',
    'x1d:"测试软件，记录功能和 UX 问题，将结果提交给负责团队，并跟进修复直至问题解决。"'
)

# -----------------------------------------------------------------------------
# NETDES: make the case study the first recruiter-facing entry point.
# -----------------------------------------------------------------------------
case_link = '<a href="/projects/netdes/" data-i="lnCase">Case study <span class="ar">↗</span></a>'
netdes_heading = '<h3>NETDES — Network Design &amp; Troubleshooting</h3>'
start = s.find(netdes_heading)
if start == -1:
    raise RuntimeError('NETDES card not found')
end = s.find('</article>', start)
card = s[start:end]
if '/projects/netdes/' not in card:
    plinks = '<div class="plinks">'
    if plinks not in card:
        raise RuntimeError('NETDES links container not found')
    card = card.replace(plinks, plinks + '\n          ' + case_link, 1)
    s = s[:start] + card + s[end:]

# Guards.
assert 'cred-groups' in s
assert '/projects/netdes/' in s
assert 'Test software, document functional and UX issues' in s
assert 'IT Help Desk Technician' not in s

path.write_text(s, encoding='utf-8')
print('Grouped credentials, tightened experience, and linked NETDES case study')
