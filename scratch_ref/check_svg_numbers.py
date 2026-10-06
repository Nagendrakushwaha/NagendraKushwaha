import re

with open('assets/github-stats.svg', 'r', encoding='utf-8') as f:
    c = f.read()

for k in ['k1', 'k2', 'k3', 'k6', 'k7', 'k8', 'k9']:
    km = re.search(rf'@keyframes {k}\{{([^}}]+)\}}', c)
    if km:
        print(f'{k}: {km.group(1)}')

# Check texts around streaks and stats
for m in re.finditer(r'<text[^>]*>([^<]+)</text>', c):
    print(m.group(0))
