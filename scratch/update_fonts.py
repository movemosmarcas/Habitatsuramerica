import glob, re, os

# Update HTML files
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the Google fonts link
    new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">'
    content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=[^>]+>', new_fonts, content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Update style.css
if os.path.exists('style.css'):
    with open('style.css', 'r', encoding='utf-8') as file:
        css = file.read()
        
    css = re.sub(r"--font-primary:\s*[^;]+;", "--font-primary: 'Outfit', sans-serif;", css)
    css = re.sub(r"--font-heading:\s*[^;]+;", "--font-heading: 'Playfair Display', serif;", css)
    
    # Also double check body
    css = re.sub(r"font-family:\s*['\"]Roboto['\"][^;]*;", "font-family: var(--font-primary);", css)
    css = re.sub(r"font-family:\s*['\"]Rufina['\"][^;]*;", "font-family: var(--font-heading);", css)
    
    with open('style.css', 'w', encoding='utf-8') as file:
        file.write(css)
