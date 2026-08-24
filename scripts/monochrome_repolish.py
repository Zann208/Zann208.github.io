from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# -----------------------------------------------------------------------------
# 1) Monochrome visual system — neutral black/white instead of blue/teal.
# -----------------------------------------------------------------------------
s = s.replace('<meta name="theme-color" content="#080b0f">', '<meta name="theme-color" content="#050505">', 1)
s = s.replace("fill='%23080b0f'/><text y='.87em' x='50%25' text-anchor='middle' font-size='58' font-family='monospace' font-weight='bold' fill='%235eead4'", "fill='%23050505'/><text y='.87em' x='50%25' text-anchor='middle' font-size='58' font-family='monospace' font-weight='bold' fill='%23ffffff'", 1)

old_dark = '''  --bg:#080b0f; --s1:#0d1319; --s2:#111922; --s3:#0a0f14;
  --bd:#1a2430; --bd2:#28353f;
  --fg:#e3eaf1; --fg2:#9cadbd; --fg3:#7d90a3;
  --ac:#5eead4; --ac2:#2dd4bf; --ac-w:rgba(94,234,212,.09); --ac-b:rgba(94,234,212,.28);
  --am:#f2b13d; --am-w:rgba(242,177,61,.11); --am-b:rgba(242,177,61,.3);'''
new_dark = '''  --bg:#050505; --s1:#0a0a0a; --s2:#101010; --s3:#070707;
  --bd:#1d1d1d; --bd2:#303030;
  --fg:#f4f4f4; --fg2:#b7b7b7; --fg3:#7e7e7e;
  --ac:#f5f5f5; --ac2:#d4d4d4; --ac-w:rgba(255,255,255,.06); --ac-b:rgba(255,255,255,.20);
  --am:#bdbdbd; --am-w:rgba(255,255,255,.05); --am-b:rgba(255,255,255,.14);'''
if old_dark in s:
    s = s.replace(old_dark, new_dark, 1)
elif new_dark not in s:
    raise RuntimeError('Dark theme token block not found')

old_light = '''  --bg:#fcfdfe; --s1:#fff; --s2:#f4f7f9; --s3:#eef3f6;
  --bd:#e2e9ee; --bd2:#c8d4dd;
  --fg:#0a1016; --fg2:#4c5e6f; --fg3:#586a7b;
  --ac:#0f766e; --ac2:#115e59; --ac-w:rgba(15,118,110,.07); --ac-b:rgba(15,118,110,.25);
  --am:#9a5b06; --am-w:rgba(154,91,6,.08); --am-b:rgba(154,91,6,.25);'''
new_light = '''  --bg:#f7f7f7; --s1:#ffffff; --s2:#f1f1f1; --s3:#ececec;
  --bd:#dedede; --bd2:#c7c7c7;
  --fg:#111111; --fg2:#555555; --fg3:#777777;
  --ac:#111111; --ac2:#333333; --ac-w:rgba(0,0,0,.045); --ac-b:rgba(0,0,0,.18);
  --am:#555555; --am-w:rgba(0,0,0,.04); --am-b:rgba(0,0,0,.12);'''
if old_light in s:
    s = s.replace(old_light, new_light, 1)
elif new_light not in s:
    raise RuntimeError('Light theme token block not found')

# Reduce the decorative grid slightly for a cleaner, less artifact-like background.
s = s.replace('background-size:64px 64px;opacity:.3;', 'background-size:64px 64px;opacity:.18;', 1)

# -----------------------------------------------------------------------------
# 2) Remove IT Help Desk experience from both the public experience timeline
#    and the embedded resume preview.
# -----------------------------------------------------------------------------
if 'IT Help Desk Technician' in s:
    s, n = re.subn(
        r'\s*<article class="xp">\s*<div class="when">Jan 2023.*?<h3>IT Help Desk Technician</h3>.*?</article>',
        '', s, count=1, flags=re.S
    )
    if n != 1:
        raise RuntimeError('Could not remove IT Help Desk timeline entry')

if 'IT Help Desk Technician' in s:
    s, n = re.subn(
        r'\s*<div class="resume-entry"><p class="resume-entry-head"><strong>IT Help Desk Technician</strong>.*?</div>',
        '', s, count=1, flags=re.S
    )
    if n != 1:
        raise RuntimeError('Could not remove IT Help Desk resume entry')

# Experience count: 4 -> 3 after removing Help Desk.
s = s.replace('<h2 data-sc>experience</h2><span class="rule"></span><span class="n">04</span>',
              '<h2 data-sc>experience</h2><span class="rule"></span><span class="n">03</span>', 1)

# -----------------------------------------------------------------------------
# 3) Add Cisco Networking Academy — Ethical Hacker as a completed credential.
# -----------------------------------------------------------------------------
if '<h4>Ethical Hacker</h4>' not in s:
    intro_card = '''    <div class="cert done"><span class="mk">[✓]</span>
      <div><h4>Introduction to Cybersecurity</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>'''
    ethical_card = '''

    <div class="cert done"><span class="mk">[✓]</span>
      <div><h4>Ethical Hacker</h4><span data-i="cAcad">Cisco Networking Academy</span></div></div>'''
    if intro_card not in s:
        raise RuntimeError('Cisco Introduction to Cybersecurity credential marker not found')
    s = s.replace(intro_card, intro_card + ethical_card, 1)

# Credentials count: 6 -> 7.
s = s.replace('<h2 data-sc>credentials</h2><span class="rule"></span><span class="n">06</span>',
              '<h2 data-sc>credentials</h2><span class="rule"></span><span class="n">07</span>', 1)

# Keep the embedded resume preview in sync.
resume_intro = '<li>Cisco Networking Academy - Introduction to Cybersecurity</li>'
resume_eth = '<li>Cisco Networking Academy - Ethical Hacker</li>'
if resume_eth not in s:
    if resume_intro not in s:
        raise RuntimeError('Resume Cisco credential marker not found')
    s = s.replace(resume_intro, resume_intro + resume_eth, 1)

# -----------------------------------------------------------------------------
# Guards — fail loudly if a future generator regresses these requested changes.
# -----------------------------------------------------------------------------
assert '--bg:#050505' in s
assert '--ac:#f5f5f5' in s
assert 'IT Help Desk Technician' not in s
assert '<h4>Ethical Hacker</h4>' in s
assert 'Cisco Networking Academy - Ethical Hacker' in s

path.write_text(s, encoding='utf-8')
print('Portfolio repolished: monochrome theme, Help Desk removed, Ethical Hacker added')
