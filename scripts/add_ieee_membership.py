from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

# Present certifications and professional memberships together accurately.
s = s.replace(
    '<!-- ═══ CERTIFICATIONS ═══ -->',
    '<!-- ═══ CREDENTIALS ═══ -->',
    1,
)
s = s.replace(
    '<div class="shead"><h2 data-sc>certifications</h2><span class="rule"></span><span class="n">06</span></div>',
    '<div class="shead"><h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span></div>',
    1,
)

# Add IEEE Student Membership to the credentials grid, without treating it as a certification.
certs_start = s.index('<section id="certs" class="wrap rev">')
certs_end = s.index('<!-- ═══ CONNECT ═══ -->', certs_start)
certs = s[certs_start:certs_end]

if '<h4>IEEE Student Member</h4>' not in certs:
    card = '''
    <div class="cert done"><span class="mk">[M]</span>
      <div><h4>IEEE Student Member</h4><span data-i="mIEEE">Institute of Electrical and Electronics Engineers · Student Member · 2026–present</span></div></div>
'''
    marker = '\n  </div>\n</section>\n\n'
    if marker not in certs:
        raise RuntimeError("Could not find credentials grid closing marker")
    certs = certs.replace(marker, card + marker, 1)

s = s[:certs_start] + certs + s[certs_end:]

# Keep Thai and Chinese versions consistent with the English membership card.
if 'mIEEE:' not in s:
    s = s.replace(
        'cProg2:"กำลังเรียน",cPlan:"วางแผนไว้"',
        'cProg2:"กำลังเรียน",mIEEE:"สถาบันวิศวกรไฟฟ้าและอิเล็กทรอนิกส์ (IEEE) · สมาชิกนักศึกษา · 2026–ปัจจุบัน",cPlan:"วางแผนไว้"',
        1,
    )
    s = s.replace(
        'cProg2:"进行中",cPlan:"计划中"',
        'cProg2:"进行中",mIEEE:"电气电子工程师学会（IEEE）· 学生会员 · 2026–至今",cPlan:"计划中"',
        1,
    )

# Add the professional membership to the Person structured data for search engines.
if '"memberOf"' not in s:
    s = s.replace(
        '  "sameAs":["https://github.com/Zann208"',
        '  "memberOf":{"@type":"Organization","name":"IEEE — Institute of Electrical and Electronics Engineers"},\n  "sameAs":["https://github.com/Zann208"',
        1,
    )

path.write_text(s, encoding="utf-8")
print("IEEE membership added to portfolio credentials")
