with open('f:/NagendraKushwaha/scratch_ref/github-stats.svg', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

import re

texts = re.findall(r'<text[^>]*>(.*?)</text>', content, re.DOTALL)
print(f"Total texts: {len(texts)}")
# print prominent text elements (longer than 1 char or not just numbers)
for i, t in enumerate(texts):
    clean = re.sub(r'<[^>]+>', '', t).strip()
    if len(clean) > 2 and not clean.isdigit():
        print(f"  [{i}]: {clean}")
