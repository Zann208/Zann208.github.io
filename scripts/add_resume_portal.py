from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

CSS_MARK='/* RESUME_PORTAL_V1 */'
HTML_MARK='<!-- RESUME_PORTAL_V1 -->'
JS_MARK='// RESUME_PORTAL_V1'

css = r'''
/* RESUME_PORTAL_V1 */
.resume-nav-btn{background:none;border:1px solid var(--bd2);color:var(--fg2);font-family:var(--mono);font-size:var(--t-sm);padding:.42rem .68rem;border-radius:7px;cursor:pointer;display:inline-flex;align-items:center;gap:.38rem;transition:color .2s,background .2s,border-color .2s;white-space:nowrap}
.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{color:var(--ac);background:var(--ac-w);border-color:var(--ac-b)}
.resume-nav-btn svg{width:12px;height:12px;transition:transform .24s var(--ez)}
.resume-nav-btn[aria-expanded="true"] svg{transform:rotate(180deg)}
.resume-backdrop{position:fixed;inset:0;z-index:120;background:rgba(2,6,10,.82);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);display:none;align-items:flex-start;justify-content:center;padding:clamp(1rem,4vw,3rem);overflow:auto}
.resume-backdrop.open{display:flex}
.resume-shell{width:min(940px,100%);background:var(--s1);border:1px solid var(--bd2);border-radius:16px;box-shadow:0 28px 90px rgba(0,0,0,.45);overflow:hidden;animation:resumeIn .28s var(--ez)}
@keyframes resumeIn{from{opacity:0;transform:translateY(12px) scale(.99)}to{opacity:1;transform:none}}
.resume-toolbar{display:flex;align-items:center;gap:1rem;padding:.8rem 1rem;border-bottom:1px solid var(--bd);background:color-mix(in srgb,var(--s1) 92%,var(--ac) 8%);position:sticky;top:0;z-index:2}
.resume-toolbar-copy{min-width:0;flex:1}.resume-toolbar-copy b{display:block;font-family:var(--mono);font-size:var(--t-sm);color:var(--fg)}
.resume-toolbar-copy span{display:block;font-family:var(--mono);font-size:var(--t-xs);color:var(--fg3);margin-top:.08rem}
.resume-actions{display:flex;gap:.45rem;align-items:center}.resume-action{font-family:var(--mono);font-size:var(--t-xs);font-weight:600;padding:.48rem .72rem;border-radius:7px;border:1px solid var(--bd2);background:var(--bg);color:var(--fg2);cursor:pointer;display:inline-flex;align-items:center;gap:.35rem}.resume-action:hover{color:var(--ac);border-color:var(--ac)}
.resume-close{width:32px;height:32px;padding:0;display:grid;place-items:center;font-size:1rem}
.resume-stage{padding:clamp(.75rem,2vw,1.5rem);background:#cfd5db}
.resume-paper{width:min(794px,100%);margin:0 auto;background:#fff;color:#1c232b;box-shadow:0 10px 35px rgba(0,0,0,.18);padding:38px 46px 34px;font-family:Arial,Helvetica,sans-serif;line-height:1.18;font-size:12.6px;min-height:1123px}
.resume-paper *{box-sizing:border-box}.resume-paper a{color:#155d8d;text-decoration:none}.resume-paper a:hover{text-decoration:underline}
.resume-name{text-align:center;color:#9b332f;font-size:27px;line-height:1;font-weight:700;letter-spacing:.01em;margin:0 0 12px}
.resume-title{text-align:center;font-size:13.6px;font-weight:700;margin:0 0 5px;color:#20262c}
.resume-contact{text-align:center;color:#4c5967;font-size:11.8px;margin:0 0 25px}.resume-contact a{white-space:nowrap}
.resume-rule{height:2px;background:#183a59;margin-bottom:10px}
.resume-sec{margin-top:17px}.resume-sec h3{font-size:13px;color:#9b332f;text-transform:uppercase;margin:0 0 10px;padding-bottom:4px;border-bottom:1px solid #c8d3dc;letter-spacing:.01em}
.resume-paper p{margin:0}.resume-profile{line-height:1.3}.resume-entry{margin-top:8px}.resume-entry:first-child{margin-top:0}.resume-entry-head{font-size:12.8px;line-height:1.25}.resume-entry-head strong{font-weight:700}.resume-meta{color:#536171;font-size:11.6px;margin-top:2px}.resume-line{margin-top:4px;line-height:1.3}.resume-skills{display:grid;gap:2px}.resume-skills strong{font-weight:700}.resume-bullets{margin:4px 0 0;padding-left:17px}.resume-bullets li{margin:2px 0;line-height:1.28}.resume-project{margin-top:9px}.resume-project-head{line-height:1.25}.resume-project-head strong{font-weight:700}.resume-project-head .muted{color:#536171}.resume-project-head a{margin-left:4px}
.resume-note{margin-top:10px;font-size:10.5px;color:#6a7580;text-align:center}
@media(max-width:820px){.resume-nav-btn{padding:.42rem .52rem}.resume-nav-btn .resume-word{display:none}.resume-shell{border-radius:12px}.resume-toolbar{gap:.5rem}.resume-toolbar-copy span{display:none}.resume-action .action-word{display:none}.resume-stage{padding:.5rem}.resume-paper{padding:28px 24px 26px;font-size:11.2px;min-height:auto}.resume-name{font-size:23px}.resume-title{font-size:12px}.resume-contact{font-size:10.4px;margin-bottom:19px}.resume-sec{margin-top:14px}.resume-sec h3{font-size:11.8px;margin-bottom:7px}.resume-entry-head,.resume-project-head{font-size:11.4px}.resume-meta{font-size:10.4px}}
@media(max-width:470px){.resume-backdrop{padding:.35rem}.resume-shell{border-radius:9px}.resume-paper{padding:22px 17px}.resume-contact{line-height:1.55}.resume-title{line-height:1.3}.resume-actions{gap:.28rem}.resume-action{padding:.45rem .55rem}}
@media print{body.resume-printing>*:not(#resumePortal){display:none!important}body.resume-printing #resumePortal{position:static!important;display:block!important;background:none!important;padding:0!important;overflow:visible!important}body.resume-printing .resume-shell{width:auto!important;border:0!important;box-shadow:none!important;border-radius:0!important}body.resume-printing .resume-toolbar{display:none!important}body.resume-printing .resume-stage{padding:0!important;background:#fff!important}body.resume-printing .resume-paper{box-shadow:none!important;width:100%!important;min-height:0!important;margin:0!important;padding:.42in .5in!important;font-size:9.1pt!important}body.resume-printing .resume-name{font-size:20pt!important;margin-bottom:8pt!important}body.resume-printing .resume-title{font-size:10pt!important}body.resume-printing .resume-contact{font-size:8.6pt!important;margin-bottom:16pt!important}body.resume-printing .resume-sec{margin-top:10pt!important}body.resume-printing .resume-sec h3{font-size:9.5pt!important;margin-bottom:6pt!important}body.resume-printing .resume-entry-head,body.resume-printing .resume-project-head{font-size:9.2pt!important}body.resume-printing .resume-meta{font-size:8.5pt!important}@page{size:A4;margin:0}}
'''

button = r'''      <button class="resume-nav-btn keep" id="resumeOpen" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="resumePortal" title="Preview resume">
        <span class="resume-word">resume</span>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
      </button>
'''

modal = r'''
<!-- RESUME_PORTAL_V1 -->
<div class="resume-backdrop" id="resumePortal" role="dialog" aria-modal="true" aria-labelledby="resumeDialogTitle" aria-hidden="true">
  <div class="resume-shell">
    <div class="resume-toolbar">
      <div class="resume-toolbar-copy">
        <b id="resumeDialogTitle">Network Engineering Resume</b>
        <span>1 page · recruiter-ready · updated Aug 2026</span>
      </div>
      <div class="resume-actions">
        <button class="resume-action" id="resumePrint" type="button" title="Print or save as PDF">
          <span aria-hidden="true">↗</span><span class="action-word">Print / Save PDF</span>
        </button>
        <button class="resume-action resume-close" id="resumeClose" type="button" aria-label="Close resume">×</button>
      </div>
    </div>
    <div class="resume-stage">
      <article class="resume-paper" id="resumePaper" aria-label="Thu Htoo Zan network engineering resume">
        <h1 class="resume-name">THU HTOO ZAN</h1>
        <p class="resume-title">Network Engineering Student | Information Systems &amp; Network Engineering</p>
        <p class="resume-contact">Chiang Mai, Thailand &nbsp;|&nbsp; <a href="mailto:thuhtoozan_1@cmu.ac.th">thuhtoozan_1@cmu.ac.th</a> &nbsp;|&nbsp; <a href="https://zann208.github.io/" target="_blank" rel="noopener">Portfolio</a> &nbsp;|&nbsp; <a href="https://www.linkedin.com/in/thu-htoo-zan-8866ab377/" target="_blank" rel="noopener">LinkedIn</a> &nbsp;|&nbsp; <a href="https://github.com/Zann208" target="_blank" rel="noopener">GitHub</a></p>
        <div class="resume-rule"></div>

        <section class="resume-sec"><h3>Profile</h3><p class="resume-profile">Information Systems and Network Engineering student at Chiang Mai University pursuing network engineering internships. Hands-on academic and project experience with switching, VLAN segmentation, STP, inter-VLAN routing, wireless network planning, traffic analysis and network troubleshooting; currently preparing for Cisco CCNA.</p></section>

        <section class="resume-sec"><h3>Education</h3>
          <div class="resume-entry"><p class="resume-entry-head"><strong>Chiang Mai University</strong> — Faculty of Engineering, Chiang Mai, Thailand</p><p class="resume-meta"><strong>Bachelor of Engineering, Information Systems and Network Engineering</strong> &nbsp;|&nbsp; Expected 2028</p><p class="resume-meta">Relevant study: Computer Network Design &amp; Management · Wireless &amp; Broadband Networks · Operating Systems</p></div>
        </section>

        <section class="resume-sec"><h3>Networking Skills</h3><div class="resume-skills">
          <p><strong>Network design &amp; switching:</strong> Routing &amp; switching, VLANs, 802.1Q trunking, STP/RSTP, EtherChannel, inter-VLAN routing, IP addressing &amp; subnetting</p>
          <p><strong>Wireless:</strong> Coverage and cell sizing, link-budget concepts, channel reuse, Wi-Fi security concepts</p>
          <p><strong>Tools:</strong> Cisco IOS, Packet Tracer, GNS3, Wireshark, Nmap</p>
          <p><strong>Security &amp; systems:</strong> Firewall policy, pfSense/OPNsense, access control, traffic analysis, Linux administration, virtualization</p>
        </div></section>

        <section class="resume-sec"><h3>Selected Experience</h3>
          <div class="resume-entry"><p class="resume-entry-head"><strong>Software Assurance &amp; UX Tester</strong> — Ongkanon AI &nbsp;|&nbsp; <strong>Apr 2025 - Present</strong></p><p class="resume-meta">Part-time</p><ul class="resume-bullets"><li>Test software and document functional and user-experience issues, communicate findings to owning teams, and follow reported issues through resolution.</li></ul></div>
          <div class="resume-entry"><p class="resume-entry-head"><strong>IT Help Desk Technician</strong> — WINOSHE Safety Academy &nbsp;|&nbsp; <strong>Jan 2023 - Apr 2025</strong></p><p class="resume-meta">Myanmar · Full-time</p><ul class="resume-bullets"><li>Handled day-to-day IT support and technical troubleshooting for users and workplace technology.</li></ul></div>
        </section>

        <section class="resume-sec"><h3>Networking Projects</h3>
          <div class="resume-project"><p class="resume-project-head"><strong>NETDES - Network Design Study Console</strong> <span class="muted">— Computer Network Design &amp; Management</span> <a href="https://zann208.github.io/netdes/" target="_blank" rel="noopener">Live</a> | <a href="https://github.com/Zann208/netdes" target="_blank" rel="noopener">GitHub</a></p><ul class="resume-bullets"><li>Built an offline console covering VLANs, 802.1Q trunking, EtherChannel, inter-VLAN routing and STP configuration/troubleshooting workflows.</li><li>Implemented an IEEE 802.1D port-role solver and validated it against four solved lab scenarios plus 20,000 randomized scenarios with zero invariant violations.</li></ul></div>
          <div class="resume-project"><p class="resume-project-head"><strong>WNET - Wireless Networks Study Console</strong> <span class="muted">— Wireless &amp; Broadband Networks</span> <a href="https://zann208.github.io/wnet/" target="_blank" rel="noopener">Live</a> | <a href="https://github.com/Zann208/wnet" target="_blank" rel="noopener">GitHub</a></p><ul class="resume-bullets"><li>Developed practical study tools around RF planning, coverage and cell sizing, link budgets, capacity, channel reuse, Wi-Fi security, segmentation and monitoring.</li></ul></div>
        </section>

        <section class="resume-sec"><h3>Certifications &amp; Memberships</h3><ul class="resume-bullets"><li>Cisco Networking Academy - Introduction to Cybersecurity</li><li>KMD College - Practical Network+ Training (54 hours) · Practical A+ Training (40 hours)</li><li>IEEE Student Member (2026 - Present) · Cisco CCNA (in progress)</li></ul></section>
      </article>
    </div>
  </div>
</div>
'''

js = r'''
<script>
// RESUME_PORTAL_V1
(function(){
  var portal=document.getElementById('resumePortal');
  var openBtn=document.getElementById('resumeOpen');
  var closeBtn=document.getElementById('resumeClose');
  var printBtn=document.getElementById('resumePrint');
  if(!portal||!openBtn||!closeBtn) return;
  var lastFocus=null;
  function openResume(){lastFocus=document.activeElement;portal.classList.add('open');portal.setAttribute('aria-hidden','false');openBtn.setAttribute('aria-expanded','true');document.body.style.overflow='hidden';setTimeout(function(){closeBtn.focus()},30)}
  function closeResume(){portal.classList.remove('open');portal.setAttribute('aria-hidden','true');openBtn.setAttribute('aria-expanded','false');document.body.style.overflow='';if(lastFocus&&lastFocus.focus)lastFocus.focus()}
  openBtn.addEventListener('click',function(){portal.classList.contains('open')?closeResume():openResume()});
  closeBtn.addEventListener('click',closeResume);
  portal.addEventListener('click',function(e){if(e.target===portal)closeResume()});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&portal.classList.contains('open'))closeResume()});
  if(printBtn)printBtn.addEventListener('click',function(){document.body.classList.add('resume-printing');window.print();setTimeout(function(){document.body.classList.remove('resume-printing')},400)});
  window.addEventListener('afterprint',function(){document.body.classList.remove('resume-printing')});
})();
</script>
'''

if CSS_MARK not in s:
    if '</style>' not in s: raise RuntimeError('No </style> found')
    s=s.replace('</style>', css+'\n</style>',1)

if 'id="resumeOpen"' not in s:
    anchor='      <div class="lang" id="lang" role="group" aria-label="Site language">'
    if anchor not in s: raise RuntimeError('Nav language anchor not found')
    s=s.replace(anchor, button+anchor,1)

if HTML_MARK not in s:
    if '</main>' not in s: raise RuntimeError('No </main> found')
    s=s.replace('</main>', '</main>\n'+modal,1)

if JS_MARK not in s:
    if '</body>' not in s: raise RuntimeError('No </body> found')
    s=s.replace('</body>', js+'\n</body>',1)

path.write_text(s,encoding='utf-8')
print('Resume portal added')
