from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# ---------- Positioning / metadata ----------
s = re.sub(r'<title>.*?</title>', '<title>Thu Htoo Zan — Network Engineering &amp; Infrastructure</title>', s, count=1)
s = re.sub(
    r'<meta name="description" content="[^"]*">',
    '<meta name="description" content="Thu Htoo Zan — Information Systems &amp; Network Engineering student at Chiang Mai University focused on network design, infrastructure, troubleshooting and security. Open to internships.">',
    s, count=1
)
s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Thu Htoo Zan — Network Engineering &amp; Infrastructure">', s, count=1)
s = re.sub(
    r'<meta property="og:description" content="[^"]*">',
    '<meta property="og:description" content="Network engineering student at Chiang Mai University building and troubleshooting network, infrastructure and security projects.">',
    s, count=1
)
s = re.sub(
    r'"knowsAbout":\[[^\]]*\]',
    '"knowsAbout":["Network Engineering","Computer Networking","Routing and Switching","VLAN Segmentation","Spanning Tree Protocol","Wireless Networking","Network Troubleshooting","Network Security","Traffic Analysis","Firewall Configuration","Linux Systems Administration","Virtualization"]',
    s, count=1
)

# ---------- Hero ----------
s = re.sub(
    r'<p class="lede" data-i="lede">.*?</p>',
    '''<p class="lede" data-i="lede">
      I design, test and troubleshoot networks and infrastructure, with hands-on work in switching,
      VLAN segmentation, spanning tree, wireless planning, traffic analysis and Linux-based systems.
      Information Systems and Network Engineering student at Chiang Mai University, currently preparing for CCNA.
    </p>''',
    s, count=1, flags=re.S
)
s = re.sub(
    r'<em data-i="n2v">.*?</em>',
    '<em data-i="n2v">Network engineering · infrastructure · security</em>',
    s, count=1
)
s = re.sub(
    r"var ROLES = \[[^\]]*\];",
    "var ROLES = ['network engineering','infrastructure · security','ISNE @ Chiang Mai University'];",
    s, count=1
)

# Update role arrays used after language switches, whichever previous version exists.
for old, new in [
    ("en: ['software · networking · security','building systems that work','ISNE @ Chiang Mai University']", "en: ['network engineering','infrastructure · security','ISNE @ Chiang Mai University']"),
    ("en: ['network & security engineering','building infrastructure that holds','ISNE @ Chiang Mai University']", "en: ['network engineering','infrastructure · security','ISNE @ Chiang Mai University']"),
    ("th: ['ซอฟต์แวร์ · เครือข่าย · ความปลอดภัย','สร้างระบบที่ใช้งานได้จริง','ISNE มหาวิทยาลัยเชียงใหม่']", "th: ['วิศวกรรมเครือข่าย','โครงสร้างพื้นฐาน · ความปลอดภัย','ISNE มหาวิทยาลัยเชียงใหม่']"),
    ("zh: ['软件 · 网络 · 安全','构建真正可用的系统','清迈大学 ISNE']", "zh: ['网络工程','基础设施 · 安全','清迈大学 ISNE']"),
]:
    s = s.replace(old, new)

# ---------- About ----------
s = re.sub(
    r'<p data-i="a1">.*?</p>',
    '''<p data-i="a1">
        My degree is taught in English and focuses on network infrastructure, systems design and
        information security. My main interest is understanding how networks are designed, how traffic
        moves through them, and how to verify that they are operating as intended.
      </p>''',
    s, count=1, flags=re.S
)
s = re.sub(
    r'<p data-i="a2">.*?</p>',
    '''<p data-i="a2">
        I learn through practical labs: building topologies, validating configurations, analysing
        traffic and troubleshooting failures until I can explain the cause and the fix.
      </p>''',
    s, count=1, flags=re.S
)

# ---------- Focus cards ----------
s = s.replace('Three areas that support each other.', 'The areas I am developing most deliberately.')
s = re.sub(
    r'<p data-i="p1d">.*?</p>',
    '<p data-i="p1d">Hands-on with network design and troubleshooting, including VLANs, routing, switching, subnetting, inter-VLAN routing and packet-level analysis.</p>',
    s, count=1
)
s = re.sub(
    r'<p data-i="p2d">.*?</p>',
    '<p data-i="p2d">Focused on practical network security through firewall policy, segmentation, access control and traffic inspection with tools such as Wireshark and Nmap.</p>',
    s, count=1
)
s = re.sub(r'<h3 data-i="p3t">.*?</h3>', '<h3 data-i="p3t">Systems &amp; Infrastructure</h3>', s, count=1)
s = re.sub(
    r'<p data-i="p3d">.*?</p>',
    '<p data-i="p3d">Working with Linux and virtualized lab environments to configure, test and support infrastructure in a reproducible way.</p>',
    s, count=1
)

# ---------- Work: networking first ----------
work_start = s.index('<section id="work" class="wrap rev">')
work_end = s.index('<!-- ═══ EXPERIENCE ═══ -->', work_start)
work = s[work_start:work_end]
work = re.sub(
    r'<p class="sub" data-i="wsub">.*?</p>',
    '<p class="sub" data-i="wsub">Selected work, led by networking and infrastructure projects.</p>',
    work, count=1
)

# Strengthen the two networking project cards.
work = work.replace('<h3>Network Design Console</h3>', '<h3>NETDES — Network Design &amp; Troubleshooting</h3>')
work = re.sub(
    r'<p data-i="w1d">.*?</p>',
    '''<p data-i="w1d">A network design and troubleshooting console built around VLANs, 802.1Q trunks,
          EtherChannel, inter-VLAN routing and spanning tree. Includes an IEEE 802.1D solver that determines
          the root bridge, port roles and blocked ports from an entered topology.</p>''',
    work, count=1, flags=re.S
)
work = re.sub(
    r'<div class="tags"><span class="tag">Vanilla JS</span><span class="tag">STP / RSTP</span><span class="tag">Offline-first</span><span class="tag">Single file</span></div>',
    '<div class="tags"><span class="tag">VLANs · 802.1Q</span><span class="tag">STP / RSTP</span><span class="tag">EtherChannel</span><span class="tag">Inter-VLAN routing</span></div>',
    work, count=1
)

# Turn the broad console-suite card into a concrete wireless networking project.
work = work.replace('<h3>Study Console Suite</h3>', '<h3>WNET — Wireless Network Planning</h3>')
work = re.sub(
    r'<p data-i="w2d">.*?</p>',
    '''<p data-i="w2d">A wireless networking console covering RF planning, coverage margin and cell sizing,
          link budgets, capacity, channel reuse, Wi-Fi security, segmentation and monitoring. Built to connect
          wireless design calculations with practical network decisions.</p>''',
    work, count=1, flags=re.S
)
work = re.sub(
    r'<div class="plinks">\s*<a href="https://zann208.github.io/study/".*?</div>',
    '''<div class="plinks">
          <a href="https://zann208.github.io/wnet/" target="_blank" rel="noopener">Open WNET <span class="ar">↗</span></a>
          <a class="src" href="https://github.com/Zann208/wnet" target="_blank" rel="noopener">Source <span class="ar">↗</span></a>
          <a class="src" href="https://zann208.github.io/study/" target="_blank" rel="noopener">Study hub <span class="ar">↗</span></a>
        </div>''',
    work, count=1, flags=re.S
)
work = re.sub(
    r'<div class="tags"><span class="tag">RF planning</span><span class="tag">Data structures</span><span class="tag">C\+\+</span><span class="tag">Entropy</span></div>',
    '<div class="tags"><span class="tag">RF planning</span><span class="tag">Link budgets</span><span class="tag">Channel reuse</span><span class="tag">Wi-Fi security</span></div>',
    work, count=1
)

# Reorder project cards so networking is seen first.
articles = re.findall(r'\s*<article class="proj">.*?</article>', work, flags=re.S)
if len(articles) >= 5:
    def title(card):
        m = re.search(r'<h3>(.*?)</h3>', card, flags=re.S)
        return re.sub(r'<.*?>', '', m.group(1)) if m else ''
    preferred = ['NETDES', 'WNET', 'Culprit!', 'PawSnap', 'Pavovival']
    ordered = []
    for key in preferred:
        for card in articles:
            if key in title(card) and card not in ordered:
                ordered.append(card)
                break
    ordered += [c for c in articles if c not in ordered]
    for i, card in enumerate(ordered, start=1):
        ordered[i-1] = re.sub(r'<span class="idx">\d+</span>', f'<span class="idx">{i:02d}</span>', card, count=1)
    first = work.find(articles[0])
    last = work.find(articles[-1]) + len(articles[-1])
    work = work[:first] + ''.join(ordered) + work[last:]

s = s[:work_start] + work + s[work_end:]

# ---------- Skills / capabilities ----------
stack_section = '''<!-- ═══ STACK ═══ -->
<section id="stack" class="wrap rev">
  <div class="shead"><h2 data-sc>core skills</h2><span class="rule"></span><span class="n">05</span></div>
  <p class="sub" data-i="ssub">Practical areas I use across network labs, troubleshooting and infrastructure work.</p>
  <div class="stack">
    <div class="st">
      <h3 data-i="p1t">Networking</h3>
      <ul><li>VLAN design · 802.1Q</li><li>STP / RSTP · EtherChannel</li><li>Inter-VLAN routing</li>
        <li>IP addressing · subnetting</li><li>Cisco IOS</li><li>Packet Tracer · GNS3</li></ul>
    </div>
    <div class="st">
      <h3 data-i="p2t">Security</h3>
      <ul><li>Firewall policy · segmentation</li><li>Wireshark traffic analysis</li><li>Nmap</li>
        <li>pfSense · OPNsense</li><li>Access control</li><li>System hardening</li></ul>
    </div>
    <div class="st">
      <h3 data-i="s3">Systems &amp; Infrastructure</h3>
      <ul><li>Linux administration</li><li>Proxmox · VirtualBox</li><li>Docker</li>
        <li>Windows Server</li><li>Virtualisation</li></ul>
    </div>
  </div>
</section>

<!-- ═══ CREDENTIALS ═══ -->'''
s = re.sub(
    r'<!-- ═══ STACK ═══ -->.*?<!-- ═══ CREDENTIALS ═══ -->',
    stack_section,
    s, count=1, flags=re.S
)
s = s.replace('<a href="#stack" data-sc>stack</a>', '<a href="#stack" data-sc>skills</a>')

# ---------- Connect: remove unfinished placeholders ----------
s = s.replace('<p class="d" data-i="l2">Source code for the tools I build.</p>', '<p class="d" data-i="l2">Network labs, technical tools and project source code.</p>')
s = s.replace('<span class="st8" data-i="l2s">first repos soon</span>', '<span class="st8" data-i="l2s">active repositories</span>')
s = re.sub(
    r'\s*<a class="lnk" href="https://www\.instagram\.com/the_zan\.log/".*?</a>',
    '', s, count=1, flags=re.S
)

# ---------- i18n updates ----------
def update_lang_block(text, lang_marker, next_marker, values):
    start = text.find(lang_marker)
    if start == -1:
        return text
    end = text.find(next_marker, start)
    if end == -1:
        return text
    block = text[start:end]
    for key, value in values.items():
        block = re.sub(rf'({re.escape(key)}:)"[^"]*"', lambda m, v=value: m.group(1) + '"' + v + '"', block, count=1)
    return text[:start] + block + text[end:]

s = update_lang_block(s, 'var I18N = { th: {', '}, zh: {', {
    'lede':'ผมมุ่งเน้นการออกแบบ ทดสอบ และแก้ปัญหาเครือข่ายและโครงสร้างพื้นฐาน โดยมีประสบการณ์ลงมือทำกับ switching, VLAN segmentation, spanning tree, การวางแผนเครือข่ายไร้สาย การวิเคราะห์ทราฟฟิก และระบบ Linux ปัจจุบันศึกษาวิศวกรรมระบบสารสนเทศและเครือข่ายที่มหาวิทยาลัยเชียงใหม่และกำลังเตรียมสอบ CCNA',
    'n2v':'วิศวกรรมเครือข่าย · โครงสร้างพื้นฐาน · ความปลอดภัย',
    'a1':'หลักสูตรของผมสอนเป็นภาษาอังกฤษและเน้นโครงสร้างพื้นฐานเครือข่าย การออกแบบระบบ และความปลอดภัยของข้อมูล สิ่งที่ผมสนใจมากที่สุดคือการเข้าใจว่าเครือข่ายถูกออกแบบอย่างไร ทราฟฟิกเดินทางอย่างไร และจะตรวจสอบได้อย่างไรว่าระบบทำงานตามที่ตั้งใจไว้',
    'a2':'ผมเรียนรู้ผ่านแล็บจริง โดยสร้าง topology ตรวจสอบ configuration วิเคราะห์ทราฟฟิก และแก้ปัญหาจนสามารถอธิบายสาเหตุและวิธีแก้ได้',
    'fsub':'ด้านที่ผมพัฒนาอย่างจริงจังที่สุด',
    'p1d':'ลงมือทำด้านการออกแบบและแก้ปัญหาเครือข่าย รวมถึง VLAN, routing, switching, subnetting, inter-VLAN routing และการวิเคราะห์ระดับแพ็กเก็ต',
    'p2d':'มุ่งเน้นความปลอดภัยเครือข่ายเชิงปฏิบัติผ่านนโยบายไฟร์วอลล์ segmentation การควบคุมสิทธิ์ และการตรวจสอบทราฟฟิกด้วย Wireshark และ Nmap',
    'p3t':'ระบบและโครงสร้างพื้นฐาน',
    'p3d':'ทำงานกับ Linux และสภาพแวดล้อม virtualized lab เพื่อกำหนดค่า ทดสอบ และสนับสนุนโครงสร้างพื้นฐานอย่างเป็นระบบและทำซ้ำได้',
    'wsub':'ผลงานที่คัดเลือก โดยให้ความสำคัญกับเครือข่ายและโครงสร้างพื้นฐานเป็นหลัก',
    'ssub':'ทักษะเชิงปฏิบัติที่ใช้ในแล็บเครือข่าย การแก้ปัญหา และงานโครงสร้างพื้นฐาน',
    'l2':'แล็บเครือข่าย เครื่องมือทางเทคนิค และซอร์สโค้ดของโปรเจกต์',
    'l2s':'รีโพที่ใช้งานอยู่',
    'w1d':'คอนโซลด้านการออกแบบและแก้ปัญหาเครือข่าย ครอบคลุม VLAN, 802.1Q trunks, EtherChannel, inter-VLAN routing และ spanning tree พร้อมตัวแก้ IEEE 802.1D ที่คำนวณ root bridge, port roles และ blocked ports จาก topology ที่ป้อนเข้าไป',
    'w2d':'คอนโซลเครือข่ายไร้สายที่ครอบคลุม RF planning, coverage margin และ cell sizing, link budgets, capacity, channel reuse, Wi-Fi security, segmentation และ monitoring เพื่อเชื่อมการคำนวณด้าน wireless design เข้ากับการตัดสินใจด้านเครือข่ายจริง'
})
s = update_lang_block(s, '}, zh: {', '};\n  var ROLES_BY', {
    'lede':'我专注于网络与基础设施的设计、测试和故障排除，并通过交换、VLAN 分段、生成树、无线规划、流量分析和 Linux 系统进行实践。目前就读于清迈大学信息系统与网络工程专业，并正在准备 CCNA。',
    'n2v':'网络工程 · 基础设施 · 安全',
    'a1':'我的课程以英语授课，重点涵盖网络基础设施、系统设计和信息安全。我最关注的是理解网络如何设计、流量如何传输，以及如何验证系统是否按预期运行。',
    'a2':'我通过实践实验学习：搭建拓扑、验证配置、分析流量并排查故障，直到能够解释问题的原因和解决方法。',
    'fsub':'我最有意识持续发展的领域',
    'p1d':'实践网络设计与故障排除，包括 VLAN、路由、交换、子网划分、VLAN 间路由和数据包级分析。',
    'p2d':'专注于实用网络安全，包括防火墙策略、分段、访问控制，以及使用 Wireshark 和 Nmap 进行流量检查。',
    'p3t':'系统与基础设施',
    'p3d':'使用 Linux 和虚拟化实验环境，以可重复的方式配置、测试和支持基础设施。',
    'wsub':'精选项目，以网络和基础设施工作为主。',
    'ssub':'用于网络实验、故障排除和基础设施工作的实用技能。',
    'l2':'网络实验、技术工具和项目源代码。',
    'l2s':'活跃仓库',
    'w1d':'围绕 VLAN、802.1Q Trunk、EtherChannel、VLAN 间路由和生成树构建的网络设计与故障排除控制台，并包含 IEEE 802.1D 求解器，可根据输入拓扑确定根桥、端口角色和阻塞端口。',
    'w2d':'无线网络控制台，涵盖 RF 规划、覆盖裕量与小区规模、链路预算、容量、信道复用、Wi-Fi 安全、分段和监控，将无线设计计算与实际网络决策连接起来。'
})

path.write_text(s, encoding='utf-8')
print('Portfolio refocused on network engineering')
