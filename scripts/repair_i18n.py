from pathlib import Path
import re

path = Path('index.html')
s = path.read_text(encoding='utf-8')


def update_exact(block: str, key: str, value: str) -> str:
    # Exact object-key match. Prevents `a1` from matching inside `cta1`.
    pattern = rf'(?<![A-Za-z0-9_])({re.escape(key)}:)"[^"]*"'
    updated, count = re.subn(
        pattern,
        lambda m: m.group(1) + '"' + value + '"',
        block,
        count=1,
    )
    if count != 1:
        raise RuntimeError(f'Could not update exact translation key: {key}')
    return updated


def update_block(text: str, start_marker: str, end_marker: str, values: dict[str, str]) -> str:
    start = text.find(start_marker)
    if start == -1:
        raise RuntimeError(f'Missing language block: {start_marker}')
    end = text.find(end_marker, start)
    if end == -1:
        raise RuntimeError(f'Missing language block end: {end_marker}')
    block = text[start:end]
    for key, value in values.items():
        block = update_exact(block, key, value)
    return text[:start] + block + text[end:]


TH = {
    'cta1': 'ดูผลงาน',
    'cta2': 'ติดต่อผม',
    'a1': 'หลักสูตรของผมสอนเป็นภาษาอังกฤษและเน้นโครงสร้างพื้นฐานเครือข่าย การออกแบบระบบ และความปลอดภัยของข้อมูล สิ่งที่ผมสนใจมากที่สุดคือการเข้าใจว่าเครือข่ายถูกออกแบบอย่างไร ทราฟฟิกเดินทางอย่างไร และจะตรวจสอบได้อย่างไรว่าระบบทำงานตามที่ตั้งใจไว้',
    'a2': 'ผมเรียนรู้ผ่านแล็บจริง โดยสร้าง topology ตรวจสอบ configuration วิเคราะห์ทราฟฟิก และแก้ปัญหาจนสามารถอธิบายสาเหตุและวิธีแก้ได้',
    'n2v': 'วิศวกรรมเครือข่าย · โครงสร้างพื้นฐาน · ความปลอดภัย',
    'fsub': 'ด้านที่ผมพัฒนาอย่างจริงจังที่สุด',
    'p1d': 'ลงมือทำด้านการออกแบบและแก้ปัญหาเครือข่าย รวมถึง VLAN, routing, switching, subnetting, inter-VLAN routing และการวิเคราะห์ระดับแพ็กเก็ต',
    'p2d': 'มุ่งเน้นความปลอดภัยเครือข่ายเชิงปฏิบัติผ่านนโยบายไฟร์วอลล์ segmentation การควบคุมสิทธิ์ และการตรวจสอบทราฟฟิกด้วย Wireshark และ Nmap',
    'p3t': 'ระบบและโครงสร้างพื้นฐาน',
    'p3d': 'ทำงานกับ Linux และสภาพแวดล้อม virtualized lab เพื่อกำหนดค่า ทดสอบ และสนับสนุนโครงสร้างพื้นฐานอย่างเป็นระบบและทำซ้ำได้',
    'wsub': 'ผลงานที่คัดเลือก โดยให้ความสำคัญกับเครือข่ายและโครงสร้างพื้นฐานเป็นหลัก',
    'ssub': 'ทักษะเชิงปฏิบัติที่ใช้ในแล็บเครือข่าย การแก้ปัญหา และงานโครงสร้างพื้นฐาน',
    'l2': 'แล็บเครือข่าย เครื่องมือทางเทคนิค และซอร์สโค้ดของโปรเจกต์',
    'l2s': 'รีโพที่ใช้งานอยู่',
    'w1d': 'คอนโซลด้านการออกแบบและแก้ปัญหาเครือข่าย ครอบคลุม VLAN, 802.1Q trunks, EtherChannel, inter-VLAN routing และ spanning tree พร้อมตัวแก้ IEEE 802.1D ที่คำนวณ root bridge, port roles และ blocked ports จาก topology ที่ป้อนเข้าไป',
    'w2d': 'คอนโซลเครือข่ายไร้สายที่ครอบคลุม RF planning, coverage margin และ cell sizing, link budgets, capacity, channel reuse, Wi-Fi security, segmentation และ monitoring เพื่อเชื่อมการคำนวณด้าน wireless design เข้ากับการตัดสินใจด้านเครือข่ายจริง',
}

ZH = {
    'cta1': '查看项目',
    'cta2': '联系我',
    'a1': '我的课程以英语授课，重点涵盖网络基础设施、系统设计和信息安全。我最关注的是理解网络如何设计、流量如何传输，以及如何验证系统是否按预期运行。',
    'a2': '我通过实践实验学习：搭建拓扑、验证配置、分析流量并排查故障，直到能够解释问题的原因和解决方法。',
    'n2v': '网络工程 · 基础设施 · 安全',
    'fsub': '我最有意识持续发展的领域',
    'p1d': '实践网络设计与故障排除，包括 VLAN、路由、交换、子网划分、VLAN 间路由和数据包级分析。',
    'p2d': '专注于实用网络安全，包括防火墙策略、分段、访问控制，以及使用 Wireshark 和 Nmap 进行流量检查。',
    'p3t': '系统与基础设施',
    'p3d': '使用 Linux 和虚拟化实验环境，以可重复的方式配置、测试和支持基础设施。',
    'wsub': '精选项目，以网络和基础设施工作为主。',
    'ssub': '用于网络实验、故障排除和基础设施工作的实用技能。',
    'l2': '网络实验、技术工具和项目源代码。',
    'l2s': '活跃仓库',
    'w1d': '围绕 VLAN、802.1Q Trunk、EtherChannel、VLAN 间路由和生成树构建的网络设计与故障排除控制台，并包含 IEEE 802.1D 求解器，可根据输入拓扑确定根桥、端口角色和阻塞端口。',
    'w2d': '无线网络控制台，涵盖 RF 规划、覆盖裕量与小区规模、链路预算、容量、信道复用、Wi-Fi 安全、分段和监控，将无线设计计算与实际网络决策连接起来。',
}

s = update_block(s, 'var I18N = { th: {', '}, zh: {', TH)
s = update_block(s, '}, zh: {', '};\n  var ROLES_BY', ZH)

# Sanity checks for the exact collision that previously occurred.
assert 'cta1:"ดูผลงาน"' in s
assert 'cta2:"ติดต่อผม"' in s
assert 'cta1:"查看项目"' in s
assert 'cta2:"联系我"' in s

path.write_text(s, encoding='utf-8')
print('Thai and Chinese translations repaired and validated')
