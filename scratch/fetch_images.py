import urllib.request
from bs4 import BeautifulSoup
import re

url = 'https://www.habitat-care.com/vsl/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print("Favicons:")
for link in soup.find_all('link', rel=re.compile(r'icon', re.I)):
    print(link.get('href'))

print("\nImages:")
for img in soup.find_all('img'):
    print(img.get('src'))
