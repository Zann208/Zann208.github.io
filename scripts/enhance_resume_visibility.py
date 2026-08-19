from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

old_nav = '.resume-nav-btn{background:none;border:1px solid var(--bd2);color:var(--fg2);font-family:var(--mono);font-size:var(--t-sm);padding:.42rem .68rem;border-radius:7px;cursor:pointer;display:inline-flex;align-items:center;gap:.38rem;transition:color .2s,background .2s,border-color .2s;white-space:nowrap}'
new_nav = '.resume-nav-btn{background:var(--ac);border:1px solid var(--ac);color:var(--bg);font-family:var(--mono);font-size:var(--t-sm);font-weight:700;padding:.46rem .78rem;border-radius:8px;cursor:pointer;display:inline-flex;align-items:center;gap:.42rem;transition:color .2s,background .2s,border-color .2s,transform .2s var(--ez),box-shadow .2s;white-space:nowrap;box-shadow:0 7px 22px color-mix(in srgb,var(--ac) 20%,transparent)}'
if old_nav in s:
    s = s.replace(old_nav, new_nav, 1)

old_hover = '.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{color:var(--ac);background:var(--ac-w);border-color:var(--ac-b)}'
new_hover = '.resume-nav-btn:hover,.resume-nav-btn[aria-expanded="true"]{color:var(--bg);background:var(--ac2);border-color:var(--ac2);transform:translateY(-1px);box-shadow:0 9px 28px color-mix(in srgb,var(--ac) 28%,transparent)}'
if old_hover in s:
    s = s.replace(old_hover, new_hover, 1)

old_mobile = '@media(max-width:820px){.resume-nav-btn{padding:.42rem .52rem}.resume-nav-btn .resume-word{display:none}.resume-shell{border-radius:12px}'
new_mobile = '@media(max-width:820px){.nav-links a[href="#contact"]{display:none}.resume-nav-btn{padding:.42rem .64rem}.resume-shell{border-radius:12px}'
if old_mobile in s:
    s = s.replace(old_mobile, new_mobile, 1)

# Add a visible Resume action in the hero, replacing the redundant GitHub button there.
old_hero = '<a class="btn" href="https://github.com/Zann208" target="_blank" rel="noopener">GitHub <span class="ar">↗</span></a>'
new_hero = '''<button class="btn resume-hero-btn" id="resumeHero" type="button" aria-haspopup="dialog" aria-controls="resumePortal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:15px;height:15px"><path d="M7 3h7l4 4v14H7z"/><path d="M14 3v5h5"/><path d="M10 13h5M10 17h5"/></svg>
        Resume
      </button>'''
if old_hero in s:
    s = s.replace(old_hero, new_hero, 1)

# Hero resume button is highlighted but remains secondary to View work.
css_marker = '.resume-nav-btn[aria-expanded="true"] svg{transform:rotate(180deg)}'
hero_css = '''\n.resume-hero-btn{border-color:var(--ac-b);color:var(--ac);background:var(--ac-w);font-weight:600}\n.resume-hero-btn:hover{border-color:var(--ac);color:var(--ac);background:color-mix(in srgb,var(--ac-w) 72%,var(--ac) 9%)}'''
if '.resume-hero-btn{' not in s and css_marker in s:
    s = s.replace(css_marker, css_marker + hero_css, 1)

# Wire the hero Resume button to the same modal.
js_marker = "var printBtn=document.getElementById('resumePrint');"
js_add = "\n  var heroBtn=document.getElementById('resumeHero');"
if "var heroBtn=document.getElementById('resumeHero');" not in s and js_marker in s:
    s = s.replace(js_marker, js_marker + js_add, 1)

listener_marker = "openBtn.addEventListener('click',function(){portal.classList.contains('open')?closeResume():openResume()});"
listener_add = "\n  if(heroBtn)heroBtn.addEventListener('click',openResume);"
if "heroBtn.addEventListener('click',openResume)" not in s and listener_marker in s:
    s = s.replace(listener_marker, listener_marker + listener_add, 1)

path.write_text(s, encoding='utf-8')
print('Resume visibility enhanced')
