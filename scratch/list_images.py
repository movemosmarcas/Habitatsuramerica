import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

srcs = set(re.findall(r'src="([^"]+)"', content))
urls = set(re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', content))

print("SRC references:")
for s in sorted(srcs): print(s)
print("\nURL references:")
for u in sorted(urls): print(u)
