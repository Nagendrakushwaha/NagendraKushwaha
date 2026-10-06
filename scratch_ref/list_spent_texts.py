with open('f:/NagendraKushwaha/scratch_ref/spent-my-time.svg', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re

texts = re.findall(r'<text[^>]*>(.*?)</text>', content, re.DOTALL)
print(f"Total texts: {len(texts)}")
for i, t in enumerate(texts):
    clean = re.sub(r'<[^>]+>', '', t).strip()
    print(f"  [{i}]: {clean}")
