import re
import os

svg_files = [
    'header.svg',
    'ai-specialization.svg',
    'profile-header.svg',
    'github-stats.svg',
    'spent-my-time.svg'
]

for fname in svg_files:
    fpath = os.path.join('f:/NagendraKushwaha/assets', fname)
    if not os.path.exists(fpath):
        print(f"{fname}: NOT FOUND")
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    images = list(re.finditer(r'<image\s+([^>]+)>', text))
    print(f"=== {fname} (total <image> tags: {len(images)}) ===")
    for i, m in enumerate(images):
        tag = m.group(1)
        tag_id = re.search(r'id="([^"]+)"', tag)
        tag_id_str = tag_id.group(1) if tag_id else "NO ID"
        clip = re.search(r'clip-path="([^"]+)"', tag)
        clip_str = clip.group(1) if clip else "NO CLIP"
        print(f"   [{i}] id={tag_id_str}, clip={clip_str}")
