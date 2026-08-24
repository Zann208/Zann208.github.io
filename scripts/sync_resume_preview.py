from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

CSS = r'''/* RESUME_CLEAN_LAYOUT_V1 */
.resume-stage{background:#d6d6d6}
.resume-paper{width:min(794px,100%);margin:0 auto;background:#fff;color:#171717;box-shadow:0 10px 32px rgba(0,0,0,.16);padding:40px 48px 36px;font-family:Arial,Helvetica,sans-serif;font-size:11.6px;line-height:1.32;min-height:1123px}
.resume-paper,.resume-paper *{box-sizing:border-box}
.resume-paper .resume-sec{padding:0;scroll-margin-top:0;margin-top:15px}
.resume-paper p{margin:0}
.resume-paper a{color:#222;text-decoration:none;border-bottom:1px solid #aaa}
.resume-paper a:hover{color:#000;border-bottom-color:#222}
.resume-head{text-align:center}
.resume-name{margin:0;color:#111;font-size:25px;line-height:1;font-weight:700;letter-spacing:.025em}
.resume-title{margin:7px 0 0;color:#252525;font-size:12.5px;line-height:1.25;font-weight:700}
.resume-contact-line{margin-top:8px;display:flex;align-items:center;justify-content:center;gap:.38rem .5rem;flex-wrap:wrap;color:#555;font-size:10.5px;line-height:1.25}
.resume-contact-line .sep{color:#aaa}
.resume-rule{height:1.5px;background:#171717;margin:14px 0 0}
.resume-sec h3{margin:0 0 7px;padding:0 0 4px;border-bottom:1px solid #999;color:#171717;font-size:10.9px;line-height:1.2;font-weight:700;letter-spacing:.095em;text-transform:uppercase}
.resume-profile{color:#282828;line-height:1.36}
.resume-item,.resume-project{margin-top:8px}
.resume-item:first-of-type,.resume-project:first-of-type{margin-top:0}
.resume-item-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;align-items:baseline}
.resume-item-title{font-size:11.7px;line-height:1.25;color:#171717}
.resume-item-title strong{font-weight:700}
.resume-place{color:#555;font-weight:400}
.resume-date{white-space:nowrap;color:#333;font-size:10.8px;font-weight:700;text-align:right}
.resume-meta{margin-top:2px!important;color:#555;font-size:10.7px;line-height:1.28}
.resume-skill-grid{display:grid;gap:3px}
.resume-skill-row{display:grid;grid-template-columns:148px minmax(0,1fr);gap:8px;align-items:start}
.resume-skill-row b{font-weight:700;color:#1b1b1b}
.resume-skill-row span{color:#333}
.resume-bullets{margin:4px 0 0;padding-left:16px}
.resume-bullets li{margin:2px 0;line-height:1.3;color:#2d2d2d;padding-left:1px}
.resume-project-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;align-items:baseline}
.resume-project-name{font-size:11.7px;font-weight:700;color:#171717}
.resume-project-links{display:flex;gap:6px;white-space:nowrap;font-size:10.2px}
.resume-project-links a{font-weight:600}
.resume-cred-list{display:grid;gap:4px}
.resume-cred-row{display:grid;grid-template-columns:150px minmax(0,1fr);gap:9px;align-items:start}
.resume-cred-row b{color:#1b1b1b;font-weight:700}
.resume-cred-row span{color:#333}
@media(max-width:680px){
  .resume-paper{padding:28px 24px 26px;font-size:11px;min-height:auto}
  .resume-name{font-size:22px}.resume-title{font-size:11.6px}
  .resume-contact-line{font-size:9.8px}
  .resume-item-top,.resume-project-top{grid-template-columns:1fr;gap:2px}
  .resume-date{text-align:left;color:#555}
  .resume-project-links{white-space:normal;flex-wrap:wrap}
  .resume-skill-row,.resume-cred-row{grid-template-columns:1fr;gap:1px}
  .resume-skill-row b,.resume-cred-row b{margin-top:2px}
}
@media print{
  body.resume-printing .resume-paper{padding:.40in .48in!important;font-size:8.9pt!important;line-height:1.28!important;color:#111!important}
  body.resume-printing .resume-name{font-size:19pt!important}
  body.resume-printing .resume-title{font-size:9.7pt!important}
  body.resume-printing .resume-contact-line{font-size:8pt!important;margin-top:5pt!important}
  body.resume-printing .resume-rule{margin-top:9pt!important}
  body.resume-printing .resume-sec{margin-top:8.5pt!important}
  body.resume-printing .resume-sec h3{font-size:8.7pt!important;margin-bottom:4.5pt!important;padding-bottom:2.5pt!important}
  body.resume-printing .resume-item-title,body.resume-printing .resume-project-name{font-size:9pt!important}
  body.resume-printing .resume-date,body.resume-printing .resume-meta{font-size:8.1pt!important}
  body.resume-printing .resume-project-links{font-size:7.8pt!important}
  body.resume-printing .resume-bullets{margin-top:2.5pt!important}
  body.resume-printing .resume-bullets li{margin:1pt 0!important}
  body.resume-printing .resume-skill-row{grid-template-columns:1.32in minmax(0,1fr)!important}
  body.resume-printing .resume-cred-row{grid-template-columns:1.42in minmax(0,1fr)!important}
}
/* /RESUME_CLEAN_LAYOUT_V1 */'''

if '/* RESUME_CLEAN_LAYOUT_V1 */' in s:
    s = re.sub(r'/\* RESUME_CLEAN_LAYOUT_V1 \*/.*?/\* /RESUME_CLEAN_LAYOUT_V1 \*/', CSS, s, count=1, flags=re.S)
else:
    if '</style>' not in s:
        raise RuntimeError('Style closing tag not found')
    s = s.replace('</style>', '\n' + CSS + '\n</style>', 1)

resume = '''<article class="resume-paper" id="resumePaper" aria-label="Thu Htoo Zan network engineering resume">
        <header class="resume-head">
          <h1 class="resume-name">THU HTOO ZAN</h1>
          <p class="resume-title">Network Engineering Student | Information Systems &amp; Network Engineering</p>
          <div class="resume-contact-line">
            <span>Chiang Mai, Thailand</span><span class="sep" aria-hidden="true">•</span>
            <a href="mailto:thuhtoozan_1@cmu.ac.th">thuhtoozan_1@cmu.ac.th</a><span class="sep" aria-hidden="true">•</span>
            <a href="https://zann208.github.io/" target="_blank" rel="noopener">Portfolio</a><span class="sep" aria-hidden="true">•</span>
            <a href="https://www.linkedin.com/in/thu-htoo-zan-8866ab377/" target="_blank" rel="noopener">LinkedIn</a><span class="sep" aria-hidden="true">•</span>
            <a href="https://github.com/Zann208" target="_blank" rel="noopener">GitHub</a>
          </div>
          <div class="resume-rule"></div>
        </header>

        <section class="resume-sec">
          <h3>Profile</h3>
          <p class="resume-profile">Information Systems and Network Engineering student at Chiang Mai University seeking network engineering internships. Hands-on work with switched LANs, VLAN segmentation, STP/RSTP, inter-VLAN routing, wireless planning, traffic analysis and troubleshooting. Built technical course tools that connect network concepts with Cisco IOS configuration and verification. Currently preparing for Cisco CCNA.</p>
        </section>

        <section class="resume-sec">
          <h3>Education</h3>
          <div class="resume-item">
            <div class="resume-item-top">
              <p class="resume-item-title"><strong>Chiang Mai University</strong> <span class="resume-place">· Faculty of Engineering, Chiang Mai, Thailand</span></p>
              <span class="resume-date">Expected 2028</span>
            </div>
            <p class="resume-meta"><strong>Bachelor of Engineering, Information Systems and Network Engineering</strong></p>
            <p class="resume-meta">Relevant study: Computer Network Design &amp; Management · Wireless &amp; Broadband Networks · Operating Systems</p>
          </div>
        </section>

        <section class="resume-sec">
          <h3>Networking Skills</h3>
          <div class="resume-skill-grid">
            <div class="resume-skill-row"><b>Switching &amp; LAN</b><span>VLANs, 802.1Q trunking, STP/RSTP, EtherChannel, inter-VLAN routing, IP addressing &amp; subnetting</span></div>
            <div class="resume-skill-row"><b>Wireless</b><span>Coverage and cell sizing, link-budget concepts, channel reuse, Wi-Fi security concepts</span></div>
            <div class="resume-skill-row"><b>Tools</b><span>Cisco IOS, Packet Tracer, GNS3, Wireshark, Nmap</span></div>
            <div class="resume-skill-row"><b>Security &amp; systems</b><span>Firewall policy, pfSense/OPNsense, access control, traffic analysis, Linux administration, virtualization</span></div>
          </div>
        </section>

        <section class="resume-sec">
          <h3>Selected Experience</h3>
          <div class="resume-item">
            <div class="resume-item-top">
              <p class="resume-item-title"><strong>Software Assurance &amp; UX Tester</strong> <span class="resume-place">· Ongkanon AI</span></p>
              <span class="resume-date">Apr 2025 – Present</span>
            </div>
            <p class="resume-meta">Part-time · Germany</p>
            <ul class="resume-bullets"><li>Test software, document functional and UX issues, report findings to the owning teams, and follow fixes through resolution.</li></ul>
          </div>
        </section>

        <section class="resume-sec">
          <h3>Networking Projects</h3>
          <div class="resume-project">
            <div class="resume-project-top">
              <p class="resume-project-name">NETDES · Network Design &amp; Troubleshooting</p>
              <span class="resume-project-links"><a href="https://zann208.github.io/projects/netdes/" target="_blank" rel="noopener">Case Study</a><a href="https://zann208.github.io/netdes/" target="_blank" rel="noopener">Live</a><a href="https://github.com/Zann208/netdes" target="_blank" rel="noopener">GitHub</a></span>
            </div>
            <ul class="resume-bullets">
              <li>Built an offline course console connecting 16 lecture decks and 12 lab workflows with Cisco IOS configuration, verification commands and troubleshooting practice.</li>
              <li>Implemented an IEEE 802.1D port-role solver for root bridge, root port, designated port and blocked-port decisions using path cost, Bridge ID and port ID tie-breaks.</li>
            </ul>
          </div>
          <div class="resume-project">
            <div class="resume-project-top">
              <p class="resume-project-name">WNET · Wireless Network Planning Console</p>
              <span class="resume-project-links"><a href="https://zann208.github.io/wnet/" target="_blank" rel="noopener">Live</a><a href="https://github.com/Zann208/wnet" target="_blank" rel="noopener">GitHub</a></span>
            </div>
            <ul class="resume-bullets"><li>Developed practical study tools for RF planning, coverage and cell sizing, link budgets, capacity, channel reuse, Wi-Fi security, segmentation and monitoring.</li></ul>
          </div>
        </section>

        <section class="resume-sec">
          <h3>Credentials &amp; Memberships</h3>
          <div class="resume-cred-list">
            <div class="resume-cred-row"><b>Cisco Networking Academy</b><span>Networking Basics · Exploring Networking with Cisco Packet Tracer · Introduction to Cybersecurity · Ethical Hacker · Introduction to Modern AI</span></div>
            <div class="resume-cred-row"><b>Technical training</b><span>Practical Network+ Training (54 hours) · Practical A+ Training (40 hours), KMD College</span></div>
            <div class="resume-cred-row"><b>Current</b><span>Cisco CCNA (in progress) · Google Cybersecurity Certificate (in progress) · IEEE Student Member (2026 – Present)</span></div>
          </div>
        </section>
      </article>'''

pattern = r'<article class="resume-paper" id="resumePaper".*?</article>'
if not re.search(pattern, s, flags=re.S):
    raise RuntimeError('Resume paper not found')
s = re.sub(pattern, resume, s, count=1, flags=re.S)

if '20,000 randomized scenarios' in s or '20,000 randomized' in s:
    raise RuntimeError('Retired NETDES validation claim is still present')

assert 'RESUME_CLEAN_LAYOUT_V1' in s
assert 'resume-item-top' in s
assert 'resume-skill-row' in s
assert 'resume-cred-row' in s
assert 'IT Help Desk Technician' not in s
assert 'Exploring Networking with Cisco Packet Tracer' in s
assert 'Introduction to Modern AI' in s
assert 'Google Cybersecurity Certificate (in progress)' in s

path.write_text(s, encoding='utf-8')
print('Cleaned resume typography, rules, spacing and alignment')
