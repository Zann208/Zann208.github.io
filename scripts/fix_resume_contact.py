from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')

# Give the contact Resume button its own unique ID.
contact_start = s.find('<section id="contact"')
contact_end = s.find('</section>', contact_start)
if contact_start == -1 or contact_end == -1:
    raise RuntimeError('Contact section not found')

contact = s[contact_start:contact_end]
if 'id="resumeContact"' not in contact:
    if 'id="resumeHero"' not in contact:
        raise RuntimeError('Contact Resume button not found')
    contact = contact.replace('id="resumeHero"', 'id="resumeContact"', 1)
    s = s[:contact_start] + contact + s[contact_end:]

# Wire the contact Resume button to the same modal opener.
hero_var = "  var heroBtn=document.getElementById('resumeHero');"
contact_var = "  var contactBtn=document.getElementById('resumeContact');"
if contact_var not in s:
    if hero_var not in s:
        raise RuntimeError('Resume JS hero binding marker not found')
    s = s.replace(hero_var, hero_var + '\n' + contact_var, 1)

hero_listener = "  if(heroBtn)heroBtn.addEventListener('click',openResume);"
contact_listener = "  if(contactBtn)contactBtn.addEventListener('click',openResume);"
if contact_listener not in s:
    if hero_listener not in s:
        raise RuntimeError('Resume JS hero listener marker not found')
    s = s.replace(hero_listener, hero_listener + '\n' + contact_listener, 1)

# Guard against duplicate IDs breaking event binding again.
if s.count('id="resumeHero"') != 1:
    raise RuntimeError(f'Expected exactly one resumeHero ID, found {s.count("id=\"resumeHero\"")}')
if s.count('id="resumeContact"') != 1:
    raise RuntimeError(f'Expected exactly one resumeContact ID, found {s.count("id=\"resumeContact\"")}')

path.write_text(s, encoding='utf-8')
print('Contact Resume button fixed and validated')
