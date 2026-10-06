import re

with open('assets/github-stats.svg', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Fix longest streak date
s = s.replace(
    '<text x="988" y="218" font-size="20" font-weight="600" fill="#8B94B3">days</text>\n<text x="888" y="260" font-size="13" font-weight="600" fill="#5EEAD4">Oct 4 to Oct 6 (Active)</text>',
    '<text x="988" y="218" font-size="20" font-weight="600" fill="#8B94B3">days</text>\n<text x="888" y="260" font-size="13" font-weight="600" fill="#5EEAD4">Apr 22 to Apr 28</text>'
)

# 2. Fix subtitle duplicate
s = s.replace('IST (UTC+5:30 (IST))', 'India IST (UTC+5:30)')

# 3. Clean up repository languages list
pattern = r'<circle cx="74" cy="611" r="5" fill="#F37626"/>.*?<text x="302" y="740" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">9%</text>'

new_repo_langs = '''<circle cx="74" cy="611" r="5" fill="#F37626"/>
<text x="92" y="616" font-size="14" fill="#E8ECF8">Jupyter Notebook</text>
<text x="302" y="616" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">55%</text>
<circle cx="74" cy="642" r="5" fill="#F1E05A"/>
<text x="92" y="647" font-size="14" fill="#E8ECF8">JavaScript</text>
<text x="302" y="647" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">23%</text>
<circle cx="74" cy="673" r="5" fill="#3178C6"/>
<text x="92" y="678" font-size="14" fill="#E8ECF8">TypeScript</text>
<text x="302" y="678" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">14%</text>
<circle cx="74" cy="704" r="5" fill="#3572A5"/>
<text x="92" y="709" font-size="14" fill="#E8ECF8">Python</text>
<text x="302" y="709" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">8%</text>'''

s = re.sub(pattern, new_repo_langs, s, flags=re.DOTALL)

# Center of repo ring:
s = re.sub(
    r'<text x="450" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">[^<]+</text>',
    '<text x="450" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">Jupyter / ML</text>',
    s
)

# 4. Clean up commit languages list
old_commit_pattern = r'<text x="638" y="566" font-size="17" font-weight="700" fill="#E8ECF8">Top languages by commit</text>.*?<circle cx="1020" cy="668" r="68" fill="none" stroke="#FFFFFF"'

new_commit_langs = '''<text x="638" y="566" font-size="17" font-weight="700" fill="#E8ECF8">Top languages by commit</text>
<circle cx="644" cy="611" r="5" fill="#3572A5"/>
<text x="662" y="616" font-size="14" fill="#E8ECF8">Python &amp; ML</text>
<text x="872" y="616" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">62%</text>
<circle cx="644" cy="642" r="5" fill="#F1E05A"/>
<text x="662" y="647" font-size="14" fill="#E8ECF8">JavaScript</text>
<text x="872" y="647" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">20%</text>
<circle cx="644" cy="673" r="5" fill="#3178C6"/>
<text x="662" y="678" font-size="14" fill="#E8ECF8">TypeScript</text>
<text x="872" y="678" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">12%</text>
<circle cx="644" cy="704" r="5" fill="#8B94B3"/>
<text x="662" y="709" font-size="14" fill="#E8ECF8">Other / HTML / CSS</text>
<text x="872" y="709" text-anchor="end" font-size="14" font-weight="600" fill="#8B94B3">6%</text>
<circle cx="1020" cy="668" r="68" fill="none" stroke="#FFFFFF"'''

s = re.sub(old_commit_pattern, new_commit_langs, s, flags=re.DOTALL)

with open('assets/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(s)

with open('scratch_ref/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(s)

print('Refinements applied successfully!')
