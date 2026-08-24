from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Keep the in-site resume aligned with the downloadable one-page resume.
profile = (
    'Information Systems and Network Engineering student at Chiang Mai University seeking network engineering internships. '
    'Hands-on work with switched LANs, VLAN segmentation, STP/RSTP, inter-VLAN routing, wireless planning, traffic analysis '
    'and troubleshooting. Built technical course tools that connect network concepts with Cisco IOS configuration and verification. '
    'Currently preparing for Cisco CCNA.'
)
s, n = re.subn(
    r'(<section class="resume-sec"><h3>Profile</h3><p class="resume-profile">).*?(</p></section>)',
    lambda m: m.group(1) + profile + m.group(2),
    s,
    count=1,
    flags=re.S,
)
if n != 1:
    raise RuntimeError('Resume profile not found')

s = s.replace(
    '<strong>Network design &amp; switching:</strong> Routing &amp; switching, VLANs, 802.1Q trunking, STP/RSTP, EtherChannel, inter-VLAN routing, IP addressing &amp; subnetting',
    '<strong>Switching &amp; LAN:</strong> VLANs, 802.1Q trunking, STP/RSTP, EtherChannel, inter-VLAN routing, IP addressing &amp; subnetting',
    1,
)

experience = '''<section class="resume-sec"><h3>Selected Experience</h3>
          <div class="resume-entry"><p class="resume-entry-head"><strong>Software Assurance &amp; UX Tester</strong> — Ongkanon AI &nbsp;|&nbsp; <strong>Apr 2025 - Present</strong></p><p class="resume-meta">Part-time</p><ul class="resume-bullets"><li>Test software, document functional and UX issues, report findings to the owning teams, and follow fixes through resolution.</li></ul></div>
        </section>'''

s, n = re.subn(
    r'<section class="resume-sec"><h3>Selected Experience</h3>.*?</section>',
    experience,
    s,
    count=1,
    flags=re.S,
)
if n != 1:
    raise RuntimeError('Selected Experience section not found')

projects = '''<section class="resume-sec"><h3>Networking Projects</h3>
          <div class="resume-project"><p class="resume-project-head"><strong>NETDES - Network Design &amp; Troubleshooting</strong> <a href="https://zann208.github.io/projects/netdes/" target="_blank" rel="noopener">Case Study</a> | <a href="https://zann208.github.io/netdes/" target="_blank" rel="noopener">Live</a> | <a href="https://github.com/Zann208/netdes" target="_blank" rel="noopener">GitHub</a></p><ul class="resume-bullets"><li>Built an offline course console that connects 16 lecture decks and 12 lab workflows with Cisco IOS configuration, verification commands and troubleshooting practice.</li><li>Implemented an IEEE 802.1D port-role solver for root bridge, root port, designated port and blocked-port decisions using path cost, Bridge ID and port ID tie-breaks.</li></ul></div>
          <div class="resume-project"><p class="resume-project-head"><strong>WNET - Wireless Network Planning Console</strong> <a href="https://zann208.github.io/wnet/" target="_blank" rel="noopener">Live</a> | <a href="https://github.com/Zann208/wnet" target="_blank" rel="noopener">GitHub</a></p><ul class="resume-bullets"><li>Developed practical study tools around RF planning, coverage and cell sizing, link budgets, capacity, channel reuse, Wi-Fi security, segmentation and monitoring.</li></ul></div>
        </section>'''

s, n = re.subn(
    r'<section class="resume-sec"><h3>Networking Projects</h3>.*?</section>',
    projects,
    s,
    count=1,
    flags=re.S,
)
if n != 1:
    raise RuntimeError('Networking Projects section not found')

credentials = '''<section class="resume-sec"><h3>Credentials &amp; Memberships</h3><ul class="resume-bullets"><li>Cisco Networking Academy: Networking Basics · Exploring Networking with Cisco Packet Tracer · Introduction to Cybersecurity · Ethical Hacker · Introduction to Modern AI</li><li>KMD College: Practical Network+ Training (54 hours) · Practical A+ Training (40 hours)</li><li>Cisco CCNA - in progress · Google Cybersecurity Certificate - in progress · IEEE Student Member - 2026 to present</li></ul></section>'''

s, n = re.subn(
    r'<section class="resume-sec"><h3>(?:Certifications|Credentials) &amp; Memberships</h3>.*?</section>',
    credentials,
    s,
    count=1,
    flags=re.S,
)
if n != 1:
    raise RuntimeError('Resume credentials section not found')

if '20,000 randomized scenarios' in s or '20,000 randomized' in s:
    raise RuntimeError('Retired NETDES validation claim is still present')

assert 'https://zann208.github.io/projects/netdes/' in s
assert 'NETDES - Network Design &amp; Troubleshooting' in s
assert 'Introduction to Modern AI' in s
assert 'Google Cybersecurity Certificate - in progress' in s
assert 'IT Help Desk Technician' not in s

path.write_text(s, encoding='utf-8')
print('Synced portfolio resume preview with current one-page resume')
