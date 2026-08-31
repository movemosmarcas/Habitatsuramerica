import os
from PIL import Image
import re

source_dir = 'Fotos Habitat'
target_dir = 'hero_slides'
html_file = 'index.html'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

target_files = [
    '20260210-DEV-GOOGLE-IMAGE-ADS-ENTORNODETALLES idea 6.png',
    'Juegos.jpg',
    '_LEU4760.jpg'
]

new_html_items = []

for i, filename in enumerate(target_files):
    filepath = os.path.join(source_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    try:
        with Image.open(filepath) as img:
            img.thumbnail((1920, 1920))
            
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            new_filename = f"slide_{i+1}.webp"
            save_filepath = os.path.join(target_dir, new_filename)
            html_filepath = f"{target_dir}/{new_filename}"
            
            img.save(save_filepath, 'WEBP', quality=85)
            
            active_class = " active" if i == 0 else ""
            new_html_items.append(f'                <div class="hero-slide{active_class}" style="background-image: url(\'{html_filepath}\');"></div>')
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# Update index.html
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_slideshow_html = '<div class="hero-slideshow">\n' + '\n'.join(new_html_items) + '\n            </div>'

content = re.sub(r'<div class="hero-slideshow">.*?</div>', lambda m: new_slideshow_html, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully processed {len(new_html_items)} hero images.")
