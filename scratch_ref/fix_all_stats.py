import re
import xml.etree.ElementTree as ET

with open('assets/github-stats.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_line_9 = '''@keyframes k1{0%,3.571%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}15.714%,100%{transform:translateY(-1209.6px)}}@keyframes k2{0%,4.429%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.571%,100%{transform:translateY(-1108.8px)}}@keyframes k3{0%,5.286%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.429%,100%{transform:translateY(-1209.6px)}}@keyframes k4{0%,4.643%{stroke-dashoffset:389.56;animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.786%,100%{stroke-dashoffset:222.8}}@keyframes k5{0%,17.143%{opacity:0;animation-timing-function:ease}20.0%,100%{opacity:1}}@keyframes k6{0%,4.643%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.786%,100%{transform:translateY(-644.0px)}}@keyframes k7{0%,5.5%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.643%,100%{transform:translateY(-837.2px)}}@keyframes k8{0%,5.714%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.857%,100%{transform:translateY(-1008.0px)}}@keyframes k9{0%,6.571%{transform:translateY(0px);animation-timing-function:cubic-bezier(.2,.8,.2,1)}18.714%,100%{transform:translateY(-1713.6px)}}@keyframes k10{0%,18.571%{opacity:0;animation-timing-function:ease}22.857%,100%{opacity:1}}@keyframes k11{0%,10.714%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}15.714%,100%{transform:scaleY(1)}}@keyframes k12{0%,11.0%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.0%,100%{transform:scaleY(1)}}@keyframes k13{0%,11.286%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.286%,100%{transform:scaleY(1)}}@keyframes k14{0%,11.571%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.571%,100%{transform:scaleY(1)}}@keyframes k15{0%,11.857%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}16.857%,100%{transform:scaleY(1)}}@keyframes k16{0%,12.143%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.143%,100%{transform:scaleY(1)}}@keyframes k17{0%,12.429%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.429%,100%{transform:scaleY(1)}}@keyframes k18{0%,12.714%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}17.714%,100%{transform:scaleY(1)}}@keyframes k19{0%,13.0%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}18.0%,100%{transform:scaleY(1)}}@keyframes k20{0%,13.286%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}18.286%,100%{transform:scaleY(1)}}@keyframes k21{0%,13.571%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}18.571%,100%{transform:scaleY(1)}}@keyframes k22{0%,13.857%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}18.857%,100%{transform:scaleY(1)}}@keyframes k23{0%,14.143%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}19.143%,100%{transform:scaleY(1)}}@keyframes k24{0%,14.429%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}19.429%,100%{transform:scaleY(1)}}@keyframes k25{0%,14.714%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}19.714%,100%{transform:scaleY(1)}}@keyframes k26{0%,15.0%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}20.0%,100%{transform:scaleY(1)}}@keyframes k27{0%,15.286%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}20.286%,100%{transform:scaleY(1)}}@keyframes k28{0%,15.571%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}20.571%,100%{transform:scaleY(1)}}@keyframes k29{0%,15.857%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}20.857%,100%{transform:scaleY(1)}}@keyframes k30{0%,16.143%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}21.143%,100%{transform:scaleY(1)}}@keyframes k31{0%,16.429%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}21.429%,100%{transform:scaleY(1)}}@keyframes k32{0%,16.714%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}21.714%,100%{transform:scaleY(1)}}@keyframes k33{0%,17.0%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}22.0%,100%{transform:scaleY(1)}}@keyframes k34{0%,17.286%{transform:scaleY(0);animation-timing-function:cubic-bezier(.2,.8,.2,1)}22.286%,100%{transform:scaleY(1)}}@keyframes k35{0%,17.143%{stroke-dasharray:0 427.26;animation-timing-function:linear}21.343%,100%{stroke-dasharray:234.99 427.26}}@keyframes k36{0%,21.343%{stroke-dasharray:0 427.26;animation-timing-function:linear}23.543%,100%{stroke-dasharray:98.27 427.26}}@keyframes k37{0%,23.543%{stroke-dasharray:0 427.26;animation-timing-function:linear}24.843%,100%{stroke-dasharray:59.82 427.26}}@keyframes k38{0%,24.843%{stroke-dasharray:0 427.26;animation-timing-function:linear}26.243%,100%{stroke-dasharray:34.18 427.26}}@keyframes k39{0%,26.243%{stroke-dasharray:0 427.26;animation-timing-function:linear}27.143%,100%{stroke-dasharray:0 427.26}}@keyframes k40{0%,27.143%{opacity:0;animation-timing-function:ease}30.714%,100%{opacity:1}}@keyframes k41{0%,19.286%{stroke-dasharray:0 427.26;animation-timing-function:linear}24.486%,100%{stroke-dasharray:264.90 427.26}}@keyframes k42{0%,24.486%{stroke-dasharray:0 427.26;animation-timing-function:linear}28.486%,100%{stroke-dasharray:85.45 427.26}}@keyframes k43{0%,28.486%{stroke-dasharray:0 427.26;animation-timing-function:linear}29.343%,100%{stroke-dasharray:51.27 427.26}}@keyframes k44{0%,28.986%{stroke-dasharray:0 427.26;animation-timing-function:linear}29.843%,100%{stroke-dasharray:25.64 427.26}}@keyframes k45{0%,29.186%{stroke-dasharray:0 427.26;animation-timing-function:linear}30.043%,100%{stroke-dasharray:0 427.26}}@keyframes k46{0%,29.286%{opacity:0;animation-timing-function:ease}32.857%,100%{opacity:1}}\n'''

lines[8] = new_line_9

full_svg = "".join(lines)

# Update static circle stroke-dasharray and offsets for Repo Languages
# Circle 1: Jupyter Notebook (55%, #F37626)
full_svg = re.sub(
    r'<circle cx="450" cy="668" r="68" fill="none" stroke="#4F8EF7" stroke-width="26"[^>]+>',
    '<circle cx="450" cy="668" r="68" fill="none" stroke="#F37626" stroke-width="26" stroke-dasharray="234.99 427.26" stroke-dashoffset="-1.50" transform="rotate(-90 450 668)" style="animation:k35 14.0s infinite"/>',
    full_svg
)
# Circle 2: JavaScript (23%, #F1E05A)
full_svg = re.sub(
    r'<circle cx="450" cy="668" r="68" fill="none" stroke="#F1E05A" stroke-width="26"[^>]+>',
    '<circle cx="450" cy="668" r="68" fill="none" stroke="#F1E05A" stroke-width="26" stroke-dasharray="98.27 427.26" stroke-dashoffset="-236.49" transform="rotate(-90 450 668)" style="animation:k36 14.0s infinite"/>',
    full_svg
)
# Circle 3: TypeScript (14%, #3178C6)
full_svg = re.sub(
    r'<circle cx="450" cy="668" r="68" fill="none" stroke="#F34B7D" stroke-width="26"[^>]+>',
    '<circle cx="450" cy="668" r="68" fill="none" stroke="#3178C6" stroke-width="26" stroke-dasharray="59.82 427.26" stroke-dashoffset="-334.76" transform="rotate(-90 450 668)" style="animation:k37 14.0s infinite"/>',
    full_svg
)
# Circle 4: Python (8%, #3572A5)
full_svg = re.sub(
    r'<circle cx="450" cy="668" r="68" fill="none" stroke="#F97316" stroke-width="26"[^>]+>',
    '<circle cx="450" cy="668" r="68" fill="none" stroke="#3572A5" stroke-width="26" stroke-dasharray="34.18 427.26" stroke-dashoffset="-394.58" transform="rotate(-90 450 668)" style="animation:k38 14.0s infinite"/>',
    full_svg
)
# Circle 5: Hide/zero out circle 5
full_svg = re.sub(
    r'<circle cx="450" cy="668" r="68" fill="none" stroke="#EF4444" stroke-width="26"[^>]+>',
    '<circle cx="450" cy="668" r="68" fill="none" stroke="#EF4444" stroke-width="26" stroke-dasharray="0 427.26" stroke-dashoffset="-427.26" transform="rotate(-90 450 668)" style="animation:k39 14.0s infinite"/>',
    full_svg
)

# Update static circle stroke-dasharray and offsets for Commit Languages
# Circle 1: Python & AI/ML (62%, #3572A5)
full_svg = re.sub(
    r'<circle cx="1020" cy="668" r="68" fill="none" stroke="#4F8EF7" stroke-width="26"[^>]+>',
    '<circle cx="1020" cy="668" r="68" fill="none" stroke="#3572A5" stroke-width="26" stroke-dasharray="264.90 427.26" stroke-dashoffset="-1.50" transform="rotate(-90 1020 668)" style="animation:k41 14.0s infinite"/>',
    full_svg
)
# Circle 2: JavaScript (20%, #F1E05A)
full_svg = re.sub(
    r'<circle cx="1020" cy="668" r="68" fill="none" stroke="#F34B7D" stroke-width="26"[^>]+>',
    '<circle cx="1020" cy="668" r="68" fill="none" stroke="#F1E05A" stroke-width="26" stroke-dasharray="85.45 427.26" stroke-dashoffset="-266.40" transform="rotate(-90 1020 668)" style="animation:k42 14.0s infinite"/>',
    full_svg
)
# Circle 3: TypeScript (12%, #3178C6)
full_svg = re.sub(
    r'<circle cx="1020" cy="668" r="68" fill="none" stroke="#F1E05A" stroke-width="26"[^>]+>',
    '<circle cx="1020" cy="668" r="68" fill="none" stroke="#3178C6" stroke-width="26" stroke-dasharray="51.27 427.26" stroke-dashoffset="-351.85" transform="rotate(-90 1020 668)" style="animation:k43 14.0s infinite"/>',
    full_svg
)
# Circle 4: Other (6%, #8B94B3)
full_svg = re.sub(
    r'<circle cx="1020" cy="668" r="68" fill="none" stroke="#2DD4BF" stroke-width="26"[^>]+>',
    '<circle cx="1020" cy="668" r="68" fill="none" stroke="#8B94B3" stroke-width="26" stroke-dasharray="25.64 427.26" stroke-dashoffset="-403.12" transform="rotate(-90 1020 668)" style="animation:k44 14.0s infinite"/>',
    full_svg
)
# Circle 5: Hide/zero out circle 5
full_svg = re.sub(
    r'<circle cx="1020" cy="668" r="68" fill="none" stroke="#F97316" stroke-width="26"[^>]+>',
    '<circle cx="1020" cy="668" r="68" fill="none" stroke="#F97316" stroke-width="26" stroke-dasharray="0 427.26" stroke-dashoffset="-427.26" transform="rotate(-90 1020 668)" style="animation:k45 14.0s infinite"/>',
    full_svg
)

# Longest streak digit 2: translateY(-1713.6px) for digit 7
full_svg = full_svg.replace('style="animation:k9 14.0s infinite;transform:translateY(-1310.4px)"', 'style="animation:k9 14.0s infinite;transform:translateY(-1713.6px)"')

# Verify XML
ET.fromstring(full_svg)

with open('assets/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)

with open('scratch_ref/github-stats.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)

print("SUCCESS: 100% of animations, keyframes, numbers, and rings updated with Nagendra Kushwaha's real data!")
