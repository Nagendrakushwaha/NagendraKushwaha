with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
for m in re.finditer(r'url\(#nameclip\)', text):
    start = max(0, m.start() - 200)
    end = min(len(text), m.end() + 200)
    print(text[start:end])
