from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

needle = '.resume-sec{margin-top:17px}'
replacement = '.resume-paper .resume-sec{padding:0;scroll-margin-top:0;margin-top:17px}'

if replacement not in s:
    if needle not in s:
        raise RuntimeError('Resume section CSS marker not found')
    s = s.replace(needle, replacement, 1)

path.write_text(s, encoding='utf-8')
print('Resume preview spacing fixed')
