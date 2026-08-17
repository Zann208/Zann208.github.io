from pathlib import Path
import re

path = Path("index.html")
s = path.read_text(encoding="utf-8")

# Broaden positioning while preserving the current UI/UX.
s = re.sub(
    r"<title>.*?</title>",
    "<title>Thu Htoo Zan — Software, Network &amp; Security Engineering</title>",
    s,
    count=1,
)
s = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Thu Htoo Zan — Information Systems &amp; Network Engineering student at Chiang Mai University building software, backend, networking and security projects. Open to internships.">',
    s,
    count=1,
)
s = re.sub(
    r'<meta property="og:title" content="[^"]*">',
    '<meta property="og:title" content="Thu Htoo Zan — Software, Network &amp; Security Engineering">',
    s,
    count=1,
)
s = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta property="og:description" content="ISNE @ Chiang Mai University. Building software, backend, networking and security projects — and documenting the decisions behind them.">',
    s,
    count=1,
)
s = s.replace(
    '"jobTitle":"Network & Security Engineering Student"',
    '"jobTitle":"Information Systems & Network Engineering Student"',
    1,
)
s = re.sub(
    r'"knowsAbout":\[[^\]]*\]',
    '"knowsAbout":["Software Engineering","Backend Development","Computer Networking","Network Security","Information Security","Technical Documentation","Requirements Engineering","Linux Systems Administration","Firebase","VLAN Segmentation","Firewall Configuration"]',
    s,
    count=1,
)

s = s.replace(
    'aria-label="Network and security engineering student"',
    'aria-label="Information Systems and Network Engineering student"',
    1,
)
s = re.sub(
    r'<p class="lede" data-i="lede">.*?</p>',
    '''<p class="lede" data-i="lede">
      I build practical systems across software, networking, and security — from deployed web
      applications and backend services to network designs and technical documentation. Third-year
      Information Systems and Network Engineering student at Chiang Mai University.
    </p>''',
    s,
    count=1,
    flags=re.S,
)

s = s.replace(
    "en: ['network & security engineering','building infrastructure that holds','ISNE @ Chiang Mai University']",
    "en: ['software · networking · security','building systems that work','ISNE @ Chiang Mai University']",
    1,
)
s = s.replace(
    "th: ['วิศวกรรมเครือข่ายและความปลอดภัย','สร้างโครงสร้างพื้นฐานที่มั่นคง','ISNE มหาวิทยาลัยเชียงใหม่']",
    "th: ['ซอฟต์แวร์ · เครือข่าย · ความปลอดภัย','สร้างระบบที่ใช้งานได้จริง','ISNE มหาวิทยาลัยเชียงใหม่']",
    1,
)
s = s.replace(
    "zh: ['网络与安全工程','构建稳固的基础设施','清迈大学 ISNE']",
    "zh: ['软件 · 网络 · 安全','构建真正可用的系统','清迈大学 ISNE']",
    1,
)

# Keep all three site languages consistent.
i18n_start = s.index("var I18N = { th: {")
zh_start = s.index("}, zh: {", i18n_start)
i18n_end = s.index("};\n  var ROLES_BY", zh_start)
th = s[i18n_start:zh_start]
zh = s[zh_start:i18n_end]


def set_key(block: str, key: str, value: str) -> str:
    updated, n = re.subn(
        rf'({re.escape(key)}:)"[^"]*"',
        lambda m: m.group(1) + '"' + value + '"',
        block,
        count=1,
    )
    if n != 1:
        raise RuntimeError(f"Could not update translation key: {key}")
    return updated


th = set_key(
    th,
    "lede",
    "ผมสร้างระบบที่ใช้งานได้จริงทั้งด้านซอฟต์แวร์ เครือข่าย และความปลอดภัย ตั้งแต่เว็บแอปและบริการแบ็กเอนด์ ไปจนถึงการออกแบบเครือข่ายและเอกสารทางเทคนิค ปัจจุบันเป็นนักศึกษาชั้นปีที่ 3 สาขาวิศวกรรมระบบสารสนเทศและเครือข่าย มหาวิทยาลัยเชียงใหม่",
)
th = set_key(th, "n2v", "ซอฟต์แวร์ · เครือข่าย · ความปลอดภัย")
th = set_key(
    th,
    "wsub",
    "ผลงานที่คัดเลือกจากวิศวกรรมซอฟต์แวร์ เครือข่าย ความปลอดภัย และระบบ",
)
th = set_key(
    th,
    "w3d",
    "เกมยิงเอาชีวิตรอดแบบเลื่อนด้านข้าง 2 มิติที่สร้างด้วย Java และ libGDX ร่วมกับทีม GroupSix สำหรับโปรเจกต์ปลายภาควิชาการเขียนโปรแกรมเชิงวัตถุ ผมได้พัฒนาประสบการณ์ด้านการออกแบบเชิงวัตถุ การทำงานร่วมกัน และการพัฒนาในโค้ดเบสที่ใช้สถาปัตยกรรมร่วมกัน",
)
zh = set_key(
    zh,
    "lede",
    "我构建横跨软件、网络与安全的实用系统，从已部署的 Web 应用和后端服务，到网络设计与技术文档。目前是清迈大学信息系统与网络工程专业三年级学生。",
)
zh = set_key(zh, "n2v", "软件 · 网络 · 安全")
zh = set_key(zh, "wsub", "精选项目，涵盖软件工程、网络、安全与系统。")
zh = set_key(
    zh,
    "w3d",
    "使用 Java 与 libGDX 构建的 2D 横版生存射击游戏，与 GroupSix 团队共同完成，作为面向对象程序设计课程的期末项目。这个项目让我积累了面向对象设计、团队协作以及在共享架构代码库中开发的经验。",
)

if "wCulprit:" not in th:
    th = th.replace(
        "w1d:",
        'wCulprit:"โปรเจกต์วิศวกรรมซอฟต์แวร์แบบทีมสำหรับลูกค้าจริงที่มหาวิทยาลัยเชียงใหม่ ผมรับผิดชอบด้านเอกสาร ดูแล SRS การเชื่อมโยงความต้องการ งานในสปรินต์ บันทึกการประชุม บันทึกการตัดสินใจ และเอกสารการทดสอบให้สอดคล้องกับระบบที่ใช้งานจริง",wPaw:"แพลตฟอร์มโซเชียลสำหรับสัตว์เลี้ยงที่พัฒนาโดยทีมสามคน ผมรับผิดชอบงานแบ็กเอนด์และชั้นข้อมูล รวมถึง Firebase Cloud Functions กฎความปลอดภัยของ Firestore การรองรับการยืนยันตัวตน ระบบแจ้งเตือนและตัวนับ และ service API สำหรับฝั่งหน้าเว็บ",lnCase:"กรณีศึกษาของผม",lnTeamRepo:"รีโพทีม",lnLiveProd:"เว็บไซต์จริง",lnBackend:"ซอร์สแบ็กเอนด์",lnFullRepo:"โปรเจกต์เต็ม",w1d:',
        1,
    )
if "wCulprit:" not in zh:
    zh = zh.replace(
        "w1d:",
        'wCulprit:"面向清迈大学真实客户的软件工程团队项目。我担任文档负责人，负责 SRS、需求追踪、Sprint 记录、会议纪要、决策记录与测试文档，并确保项目记录与实际部署系统保持一致。",wPaw:"三人团队开发的宠物社交平台。我负责后端与数据层工作，包括 Firebase Cloud Functions、Firestore 安全规则、认证支持、通知与计数逻辑以及前端调用的服务 API。",lnCase:"我的案例",lnTeamRepo:"团队仓库",lnLiveProd:"在线产品",lnBackend:"后端源码",lnFullRepo:"完整项目",w1d:',
        1,
    )

s = s[:i18n_start] + th + zh + s[i18n_end:]

s = s.replace(
    '<p class="sub" data-i="wsub">Status is labelled honestly. Everything marked live is online and working right now.</p>',
    '<p class="sub" data-i="wsub">Selected projects across software engineering, networking, security, and systems.</p>',
    1,
)
s = s.replace(
    '<em data-i="n2v">Networks &amp; security</em>',
    '<em data-i="n2v">Software · networks · security</em>',
    1,
)

# Add missing projects while reusing the existing project-card design.
work_start = s.index('<section id="work" class="wrap rev">')
work_end = s.index('<!-- ═══ EXPERIENCE ═══ -->', work_start)
work = s[work_start:work_end]

if "<h3>Culprit!</h3>" not in work:
    work = re.sub(
        r'<span class="idx">0([123])</span>',
        lambda m: f'<span class="idx">0{int(m.group(1)) + 2}</span>',
        work,
        count=3,
    )

    cards = '''    <article class="proj">
      <span class="idx">01</span>
      <div>
        <div class="proj-top"><h3>Culprit!</h3><span class="badge-s live" data-i="stTeam">team project</span></div>
        <p data-i="wCulprit">A customer-facing Software Engineering project for Chiang Mai University. As Documentation Lead, I manage the SRS, requirements traceability, sprint records, meeting minutes, decision records and test documentation, keeping the project record aligned with the deployed system.</p>
        <div class="plinks">
          <a class="src" href="https://culprit.wyco-dev.com/" target="_blank" rel="noopener" data-i="lnLiveProd">Live product <span class="ar">↗</span></a>
          <a class="src" href="https://github.com/Zann208/Zann208/blob/main/projects/culprit.md" target="_blank" rel="noopener" data-i="lnCase">My case study <span class="ar">↗</span></a>
          <a class="src" href="https://github.com/Wyco68/CulpritWeb" target="_blank" rel="noopener" data-i="lnTeamRepo">Team repo <span class="ar">↗</span></a>
        </div>
        <div class="tags"><span class="tag">Documentation Lead</span><span class="tag">SRS</span><span class="tag">Traceability</span><span class="tag">Scrum</span><span class="tag">Notion</span></div>
      </div>
    </article>

    <article class="proj">
      <span class="idx">02</span>
      <div>
        <div class="proj-top"><h3>PawSnap</h3><span class="badge-s live" data-i="stTeam">team project</span></div>
        <p data-i="wPaw">A pet social platform built by a team of three. I authored backend and data-layer work including Firebase Cloud Functions, Firestore security rules, authentication support, notification and counter logic, and service APIs used by the front end.</p>
        <div class="plinks">
          <a class="src" href="https://github.com/Zann208/pawsnap-backend" target="_blank" rel="noopener" data-i="lnBackend">Backend source <span class="ar">↗</span></a>
          <a class="src" href="https://github.com/MawinSkalet/Petsnaps" target="_blank" rel="noopener" data-i="lnFullRepo">Full project <span class="ar">↗</span></a>
        </div>
        <div class="tags"><span class="tag">Firebase</span><span class="tag">Cloud Functions</span><span class="tag">Firestore</span><span class="tag">Security Rules</span></div>
      </div>
    </article>

'''
    marker = '  <div class="projects">\n\n'
    if marker not in work:
        raise RuntimeError("Could not find projects container")
    work = work.replace(marker, marker + cards, 1)

# Improve the existing Pavovival card instead of duplicating the project.
work = re.sub(
    r'<p data-i="w3d">A 2D side-scrolling survival shooter written in Java with libGDX, built with\s*GroupSix as the final project for Object-Oriented Programming\. My first substantial codebase\s*written to someone else\'s architecture rather than my own\.</p>',
    '<p data-i="w3d">A 2D side-scrolling survival shooter built with Java and libGDX as a GroupSix Object-Oriented Programming final project. I contributed within a shared team architecture, strengthening my experience with object-oriented design, collaboration and working in an established codebase.</p>',
    work,
    count=1,
)

s = s[:work_start] + work + s[work_end:]

# Make the visible stack reflect projects already shown above.
s = s.replace(
    '<h3 data-i="s4">Code</h3>\n      <ul><li>Python</li><li>Bash</li><li>C</li><li>SQL</li><li>Git</li></ul>',
    '<h3 data-i="s4">Software &amp; Backend</h3>\n      <ul><li>Python · JavaScript</li><li>Java · C / C++</li><li>Firebase · Firestore</li><li>Cloud Functions</li><li>SQL · Git</li></ul>',
    1,
)

path.write_text(s, encoding="utf-8")
print("Portfolio content refreshed")
