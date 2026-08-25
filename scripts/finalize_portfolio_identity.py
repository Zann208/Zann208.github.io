from pathlib import Path
import re

home = Path('index.html')
s = home.read_text(encoding='utf-8')

# Align browser chrome/favicon with the canonical charcoal base.
s = s.replace('<meta name="theme-color" content="#050505">', '<meta name="theme-color" content="#080808">', 1)
s = s.replace("fill='%23050505'", "fill='%23080808'", 1)

# Availability should read as information, not a decorative status signal.
s = s.replace('● available', 'available')
s = s.replace('● ว่างรับงาน', 'ว่างรับงาน')
s = s.replace('● 可联系', '可联系')
s = s.replace('● 可接受机会', '可接受机会')

home.write_text(s, encoding='utf-8')

netdes = Path('projects/netdes/index.html')
n = netdes.read_text(encoding='utf-8')
n = n.replace('<meta name="theme-color" content="#050505">', '<meta name="theme-color" content="#080808">', 1)

# The only remaining 01/02/03 markers are decorative ordinals inside the
# translated "next improvements" lists. Remove them in every language while
# preserving semantic quantities such as 16 decks, 12 labs and IEEE 802.1D.
for ordinal in ('01', '02', '03'):
    n = n.replace(f'<b>{ordinal}</b>', '')

netdes.write_text(n, encoding='utf-8')
print('Final multilingual portfolio identity cleanup applied')
