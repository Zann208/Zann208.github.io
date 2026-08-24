from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

CSS = r'''/* RESUME_CLEAN_LAYOUT_V1 */
.resume-stage{background:#d6d6d6;overflow-x:hidden}
.resume-paper{width:min(794px,100%);max-width:100%;min-width:0;margin:0 auto;background:#fff;color:#171717;box-shadow:0 10px 32px rgba(0,0,0,.16);padding:38px 46px 34px;font-family:Arial,Helvetica,sans-serif;font-size:11.4px;line-height:1.31;min-height:1123px;overflow:hidden}
.resume-paper,.resume-paper *{box-sizing:border-box;min-width:0}
.resume-paper .resume-sec{padding:0;scroll-margin-top:0;margin-top:14px}
.resume-paper p{margin:0}
.resume-paper a{color:#222;text-decoration:none;border-bottom:1px solid #aaa}
.resume-paper a:hover{color:#000;border-bottom-color:#222}
.resume-head{text-align:center}
.resume-name{margin:0;color:#111;font-size:25px;line-height:1;font-weight:700;letter-spacing:.025em}
.resume-title{margin:7px 0 0;color:#252525;font-size:12.3px;line-height:1.23;font-weight:700}
.resume-contact-line{margin-top:8px;display:flex;align-items:center;justify-content:center;gap:.32rem .48rem;flex-wrap:wrap;color:#555;font-size:10.3px;line-height:1.25}
.resume-contact-line .sep{color:#aaa}
.resume-rule{height:1.5px;background:#171717;margin:13px 0 0}
.resume-sec h3{margin:0 0 6px;padding:0 0 4px;border-bottom:1px solid #9c9c9c;color:#171717;font-size:10.7px;line-height:1.2;font-weight:700;letter-spacing:.09em;text-transform:uppercase}
.resume-profile{color:#282828;line-height:1.34}
.resume-item,.resume-project{margin-top:7px}
.resume-item:first-of-type,.resume-project:first-of-type{margin-top:0}
.resume-item-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;align-items:baseline}
.resume-item-title{font-size:11.5px;line-height:1.24;color:#171717}
.resume-item-title strong{font-weight:700}
.resume-place{color:#555;font-weight:400}
.resume-date{white-space:nowrap;color:#333;font-size:10.6px;font-weight:700;text-align:right}
.resume-meta{margin-top:2px!important;color:#555;font-size:10.5px;line-height:1.26}
.resume-skill-grid{display:grid;gap:3px}
.resume-skill-row{display:grid;grid-template-columns:136px minmax(0,1fr);gap:8px;align-items:start}
.resume-skill-row b{font-weight:700;color:#1b1b1b}
.resume-skill-row span{color:#333;overflow-wrap:anywhere}
.resume-bullets{margin:3px 0 0;padding-left:16px}
.resume-bullets li{margin:1.5px 0;line-height:1.28;color:#2d2d2d;padding-left:1px}
.resume-project-top{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;align-items:baseline}
.resume-project-name{font-size:11.5px;font-weight:700;color:#171717;overflow-wrap:anywhere}
.resume-project-links{display:flex;gap:6px;white-space:nowrap;font-size:10px}
.resume-project-links a{font-weight:600}

/* Credentials: no separator chains and no fixed text column. */
.resume-cred-stack{display:grid;gap:8px}
.resume-cred-group{display:grid;grid-template-columns:124px minmax(0,1fr);gap:10px;align-items:start;padding-bottom:6px;border-bottom:1px solid #e2e2e2}
.resume-cred-group:last-child{border-bottom:0;padding-bottom:0}
.resume-cred-label{font-size:10.5px;line-height:1.25;font-weight:700;color:#1c1c1c}
.resume-cred-items{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3px 14px}
.resume-cred-items.one{grid-template-columns:1fr}
.resume-cred-item{position:relative;padding-left:9px;color:#333;line-height:1.27;overflow-wrap:anywhere}
.resume-cred-item::before{content:"";position:absolute;left:0;top:.54em;width:3px;height:3px;border-radius:50%;background:#555}
.resume-cred-item strong{color:#222;font-weight:700}
.resume-cred-item small{display:block;margin-top:1px;color:#686868;font-size:9.7px;line-height:1.2}

@media(max-width:680px){
  .resume-paper{padding:27px 22px 25px;font-size:10.9px;min-height:auto}
  .resume-name{font-size:22px}.resume-title{font-size:11.4px}
  .resume-contact-line{font-size:9.6px}
  .resume-item-top,.resume-project-top{grid-template-columns:1fr;gap:2px}
  .resume-date{text-align:left;color:#555}
  .resume-project-links{white-space:normal;flex-wrap:wrap}
  .resume-skill-row{grid-template-columns:1fr;gap:1px}
  .resume-skill-row b{margin-top:2px}
  .resume-cred-group{grid-template-columns:1fr;gap:4px}
  .resume-cred-items{grid-template-columns:1fr}
  .resume-cred-label{font-size:10.3px}
}
@media(max-width:470px){
  .resume-stage{padding:.35rem!important}
  .resume-paper{padding:22px 16px 23px}
  .resume-contact-line{gap:.25rem .38rem}
  .resume-contact-line .sep{display:none}
  .resume-project-links{gap:5px}
}
@media print{
  body.resume-printing .resume-paper{padding:.36in .44in!important;font-size:8.65pt!important;line-height:1.25!important;color:#111!important;overflow:visible!important}
  body.resume-printing .resume-name{font-size:18.5pt!important}
  body.resume-printing .resume-title{font-size:9.4pt!important}
  body.resume-printing .resume-contact-line{font-size:7.8pt!important;margin-top:4.5pt!important}
  body.resume-printing .resume-rule{margin-top:8pt!important}
  body.resume-printing .resume-sec{margin-top:7.5pt!important}
  body.resume-printing .resume-sec h3{font-size:8.5pt!important;margin-bottom:4pt!important;padding-bottom:2.3pt!important}
  body.resume-printing .resume-item-title,body.resume-printing .resume-project-name{font-size:8.8pt!important}
  body.resume-printing .resume-date,body.resume-printing .resume-meta{font-size:7.9pt!important}
  body.resume-printing .resume-project-links{font-size:7.5pt!important}
  body.resume-printing .resume-bullets{margin-top:2pt!important}
  body.resume-printing .resume-bullets li{margin:.8pt 0!important}
  body.resume-printing .resume-skill-row{grid-template-columns:1.22in minmax(0,1fr)!important}
  body.resume-printing .resume-cred-stack{gap:4.5pt!important}
  body.resume-printing .resume-cred-group{grid-template-columns:1.12in minmax(0,1fr)!important;gap:6pt!important;padding-bottom:3.5pt!important}
  body.resume-printing .resume-cred-label{font-size:7.9pt!important}
  body.resume-printing .resume-cred-items{gap:1.5pt 8pt!important}
  body.resume-printing .resume-cred-item{font-size:7.9pt!important;line-height:1.2!important;padding-left:7pt!important}
  body.resume-printing .resume-cred-item small{font-size:7.1pt!important}
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
          <div class="resume-cred-stack">
            <div class="resume-cred-group">
              <p class="resume-cred-label">Cisco Networking Academy</p>
              <div class="resume-cred-items">
                <span class="resume-cred-item">Networking Basics</span>
                <span class="resume-cred-item">Exploring Networking with Cisco Packet Tracer</span>
                <span class="resume-cred-item">Introduction to Cybersecurity</span>
                <span class="resume-cred-item">Ethical Hacker</span>
                <span class="resume-cred-item">Introduction to Modern AI</span>
              </div>
            </div>
            <div class="resume-cred-group">
              <p class="resume-cred-label">Technical Training</p>
              <div class="resume-cred-items">
                <span class="resume-cred-item"><strong>Practical Network+</strong><small>KMD College · 54 hours</small></span>
                <span class="resume-cred-item"><strong>Practical A+</strong><small>KMD College · 40 hours</small></span>
              </div>
            </div>
            <div class="resume-cred-group">
              <p class="resume-cred-label">In Progress</p>
              <div class="resume-cred-items">
                <span class="resume-cred-item">Cisco CCNA</span>
                <span class="resume-cred-item">Google Cybersecurity Certificate</span>
              </div>
            </div>
            <div class="resume-cred-group">
              <p class="resume-cred-label">Membership</p>
              <div class="resume-cred-items one">
                <span class="resume-cred-item"><strong>IEEE Student Member</strong><small>2026 – Present</small></span>
              </div>
            </div>
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
assert 'resume-cred-stack' in s
assert 'resume-cred-group' in s
assert 'resume-cred-items' in s
assert 'IT Help Desk Technician' not in s
assert 'Exploring Networking with Cisco Packet Tracer' in s
assert 'Introduction to Modern AI' in s
assert 'Google Cybersecurity Certificate' in s

path.write_text(s, encoding='utf-8')
print('Applied final clean responsive resume layout')
