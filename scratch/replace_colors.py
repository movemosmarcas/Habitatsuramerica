import os

# HTML Replacements
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('#2F5933', '#4E8B69')
content = content.replace('#618A60', '#4E8B69')
content = content.replace('#1e3a24', '#4E8B69')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# CSS Replacements
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('#036731', '#4E8B69')
css = css.replace('rgba(36, 76, 54, 0.75)', 'rgba(78, 139, 105, 0.75)')
css = css.replace('rgba(36, 76, 54, 0.4)', 'rgba(78, 139, 105, 0.4)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
