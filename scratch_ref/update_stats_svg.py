import re

with open('assets/github-stats.svg', 'r', encoding='utf-8') as f:
    svg = f.read()

# 1. Update title / subtitle / header
svg = svg.replace('GitHub stats for Nagendra Kushwaha', 'GitHub Live Stats for Nagendra Kushwaha')
svg = svg.replace(
    '<text x="40" y="78" font-size="14" fill="#8B94B3">Nagendra Kushwaha, Data Scientist &amp; AI Engineer</text>',
    '<text x="40" y="78" font-size="14" fill="#8B94B3">Nagendra Kushwaha · 22 Public Repos · 212+ Contributions · IST (UTC+5:30)</text>'
)

# Add live status indicator badge at top right
live_badge = '''<g transform="translate(1030, 40)">
  <rect x="0" y="0" width="130" height="28" rx="14" fill="#052E16" stroke="#22C55E" stroke-width="1.2"/>
  <circle cx="16" cy="14" r="4.5" fill="#22C55E"/>
  <circle cx="16" cy="14" r="8" fill="none" stroke="#22C55E" stroke-opacity="0.4">
    <animate attributeName="r" values="4;10" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="30" y="19" font-size="11" font-weight="700" fill="#4ADE80" letter-spacing="0.8">LIVE SYNCED</text>
</g>'''

svg = svg.replace('<text x="40" y="54" font-size="27" font-weight="800" fill="#E8ECF8" letter-spacing="-0.4">GitHub stats</text>',
                  '<text x="40" y="54" font-size="27" font-weight="800" fill="#E8ECF8" letter-spacing="-0.4">GitHub stats</text>\n' + live_badge)

# 2. Keyframes for Total Contributions (212)
# k1: digit 2 -> -1209.6px
# k2: digit 1 -> -1108.8px
# k3: digit 2 -> -1209.6px
svg = re.sub(
    r'@keyframes k1\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k1{\1 100%{transform:translateY(-1209.6px)}}',
    svg
)
svg = re.sub(
    r'@keyframes k2\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k2{\1 100%{transform:translateY(-1108.8px)}}',
    svg
)
svg = re.sub(
    r'@keyframes k3\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k3{\1 100%{transform:translateY(-1209.6px)}}',
    svg
)

# Replace initial style transform for k1, k2, k3
svg = svg.replace('style="animation:k1 14.0s infinite;transform:translateY(-1713.6px)"', 'style="animation:k1 14.0s infinite;transform:translateY(-1209.6px)"')
svg = svg.replace('style="animation:k2 14.0s infinite;transform:translateY(-1512.0px)"', 'style="animation:k2 14.0s infinite;transform:translateY(-1108.8px)"')
svg = svg.replace('style="animation:k3 14.0s infinite;transform:translateY(-1209.6px)"', 'style="animation:k3 14.0s infinite;transform:translateY(-1209.6px)"')

# Date label for Total Contributions
svg = svg.replace('Jul 3, 2024 to present', 'Aug 16, 2025 to present')

# 3. Current streak: 3 days (03)
# k4: ring dashoffset
svg = re.sub(
    r'@keyframes k4\{([^}]+)100%\{stroke-dashoffset:[^}]+}}',
    r'@keyframes k4{\1 100%{stroke-dashoffset:222.6}}',
    svg
)
svg = svg.replace('stroke-dashoffset="0" transform="rotate(-90 472 191)" filter="url(#glow)" style="animation:k4 14.0s infinite"',
                  'stroke-dashoffset="222.6" transform="rotate(-90 472 191)" filter="url(#glow)" style="animation:k4 14.0s infinite"')

# k6: digit 0 -> -644.0px
# k7: digit 3 -> -837.2px
svg = re.sub(
    r'@keyframes k6\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k6{\1 100%{transform:translateY(-644.0px)}}',
    svg
)
svg = re.sub(
    r'@keyframes k7\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k7{\1 100%{transform:translateY(-837.2px)}}',
    svg
)
svg = svg.replace('style="animation:k6 14.0s infinite;transform:translateY(-966.0px)"', 'style="animation:k6 14.0s infinite;transform:translateY(-644.0px)"')
svg = svg.replace('style="animation:k7 14.0s infinite;transform:translateY(-837.2px)"', 'style="animation:k7 14.0s infinite;transform:translateY(-837.2px)"')

# Subtitle and note for Current Streak
svg = svg.replace('Jul 4 to Aug 25', 'Oct 4 to Oct 6 (Active)')
svg = svg.replace('Matches the longest streak', '3 days active coding streak')

# 4. Longest streak: 7 days (07)
# k8: digit 0 -> -1008.0px
# k9: digit 7 -> -1713.6px
svg = re.sub(
    r'@keyframes k8\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k8{\1 100%{transform:translateY(-1008.0px)}}',
    svg
)
svg = re.sub(
    r'@keyframes k9\{([^}]+)100%\{transform:translateY\([^)]+\)\}\}',
    r'@keyframes k9{\1 100%{transform:translateY(-1713.6px)}}',
    svg
)
svg = svg.replace('style="animation:k8 14.0s infinite;transform:translateY(-1512.0px)"', 'style="animation:k8 14.0s infinite;transform:translateY(-1008.0px)"')
svg = svg.replace('style="animation:k9 14.0s infinite;transform:translateY(-1310.4px)"', 'style="animation:k9 14.0s infinite;transform:translateY(-1713.6px)"')

# Subtitle for Longest Streak (was Jul 4 to Aug 25)
# In section 860:
svg = svg.replace('<text x="888" y="260" font-size="13" font-weight="600" fill="#5EEAD4">Jul 4 to Aug 25</text>',
                  '<text x="888" y="260" font-size="13" font-weight="600" fill="#5EEAD4">Apr 22 to Apr 28</text>')

# 5. Commits by Hour
svg = svg.replace('UTC+5:30', 'UTC+5:30 (IST)')

# Move peak hours highlight to evening/night: 18:00 - 23:00 IST
# In original: <g style="animation:k10 14.0s infinite"><rect x="149.8" y="358" width="122.5" height="118.0" rx="10" fill="#5EEAD4" fill-opacity="0.08"/><text x="211.1" y="374" text-anchor="middle" font-size="12" font-weight="600" fill="#5EEAD4">Peak hours</text></g>
# Shift x to 960 (20:00 - 23:00)
svg = svg.replace('rect x="149.8" y="358" width="122.5" height="118.0"', 'rect x="940.0" y="358" width="165.0" height="118.0"')
svg = svg.replace('text x="211.1" y="374"', 'text x="1022.5" y="374"')

# Make evening bars taller (peak) and morning bars lower
# x=969.1, 1011.9, 1054.8
svg = svg.replace('x="969.1" y="427.8" width="26" height="44.2" rx="5" fill="url(#bar)"', 'x="969.1" y="385.0" width="26" height="87.0" rx="5" fill="url(#barPeak)"')
svg = svg.replace('x="1011.9" y="409.6" width="26" height="62.4" rx="5" fill="url(#bar)"', 'x="1011.9" y="380.0" width="26" height="92.0" rx="5" fill="url(#barPeak)"')
svg = svg.replace('x="1054.8" y="414.8" width="26" height="57.2" rx="5" fill="url(#bar)"', 'x="1054.8" y="382.0" width="26" height="90.0" rx="5" fill="url(#barPeak)"')

# 6. Top Languages by repository
# Jupyter Notebook 55%, JavaScript 23%, TypeScript 14%, Python 8%
svg = svg.replace('>42%</text>', '>55%</text>')  # Jupyter
svg = svg.replace('>Python</text>', '>Jupyter Notebook</text>', 1)
svg = svg.replace('fill="#4F8EF7"/>\n<text x="92" y="616" font-size="14" fill="#E8ECF8">Jupyter Notebook</text>',
                  'fill="#F37626"/>\n<text x="92" y="616" font-size="14" fill="#E8ECF8">Jupyter Notebook</text>')

svg = svg.replace('>22%</text>', '>23%</text>')  # JavaScript
svg = svg.replace('>13%</text>', '>14%</text>')  # TypeScript
svg = svg.replace('>C++</text>', '>TypeScript</text>', 1)
svg = svg.replace('fill="#F34B7D"/>\n<text x="92" y="678" font-size="14" fill="#E8ECF8">TypeScript</text>',
                  'fill="#3178C6"/>\n<text x="92" y="678" font-size="14" fill="#E8ECF8">TypeScript</text>')

svg = svg.replace('>14%</text>', '>8%</text>')   # Python
svg = svg.replace('>Jupyter Notebook</text>', '>Python</text>', 1)

# Center circle text
svg = svg.replace('<text x="450" y="672" text-anchor="middle" font-size="24" font-weight="800" fill="url(#numfill)">42%</text><text x="450" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">Python</text>',
                  '<text x="450" y="672" text-anchor="middle" font-size="24" font-weight="800" fill="url(#numfill)">55%</text><text x="450" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">Jupyter / ML</text>')

# 7. Top Languages by commit
svg = svg.replace('<text x="1020" y="672" text-anchor="middle" font-size="24" font-weight="800" fill="url(#numfill)">52%</text><text x="1020" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">Python</text>',
                  '<text x="1020" y="672" text-anchor="middle" font-size="24" font-weight="800" fill="url(#numfill)">62%</text><text x="1020" y="690" text-anchor="middle" font-size="12" fill="#8B94B3">Python &amp; ML</text>')

# Save back to assets/github-stats.svg
with open('assets/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

# Also sync to scratch_ref/github-stats.svg
with open('scratch_ref/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print("Updated assets/github-stats.svg with Nagendra Kushwaha's live data!")
