import os
from PIL import Image
import re

source_dir = 'Fotos Habitat'
target_dir = 'habitat_gallery'
html_file = 'index.html'

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

new_html_items = []

for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        filepath = os.path.join(source_dir, filename)
        
        # Open and resize
        try:
            with Image.open(filepath) as img:
                img.thumbnail((800, 800))
                
                # Convert to RGB if needed (for PNG to WEBP)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                new_filename = os.path.splitext(filename)[0] + '.webp'
                new_filepath = f"{target_dir}/{new_filename}" # Use forward slash for HTML
                save_filepath = os.path.join(target_dir, new_filename)
                
                # Save optimized
                img.save(save_filepath, 'WEBP', quality=80)
                
                # Add to HTML
                new_html_items.append(f'                <img src="{new_filepath}" alt="Instalaciones Hábitat Suramérica" class="gallery-item" loading="lazy">')
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Update index.html
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_grid_html = '<div class="gallery-grid">\n' + '\n'.join(new_html_items) + '\n            </div>'

content = re.sub(r'<div class="gallery-grid">.*?</div>', lambda m: new_grid_html, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully processed {len(new_html_items)} images.")
