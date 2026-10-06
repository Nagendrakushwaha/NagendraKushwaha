import re

with open('f:/NagendraKushwaha/assets/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

images = list(re.finditer(r'<image\s+([^>]+)>', text))
print(f"Total <image> tags in header.svg: {len(images)}")
for i, m in enumerate(images):
    tag = m.group(1)
    tag_id = re.search(r'id="([^"]+)"', tag)
    tag_id_str = tag_id.group(1) if tag_id else "NO ID"
    print(f"Image [{i}] ID: {tag_id_str}")
    # print first 100 chars of href
    href_m = re.search(r'(xlink:href|href)="([^"]{0,100})', tag)
    if href_m:
        print(f"   href attr: {href_m.group(1)}, value: {href_m.group(2)}...")
