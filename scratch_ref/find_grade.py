with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

import re
m = re.search(r'<[^>]*id="grade"[^>]*>.*?</[^>]+>', header, re.DOTALL)
if m:
    print(m.group(0))
else:
    # maybe self-closing or linearGradient
    for line in header.splitlines():
        if 'grade' in line:
            print(line)
