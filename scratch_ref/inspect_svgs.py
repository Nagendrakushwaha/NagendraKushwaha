import re
import os

with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    header = f.read()

print("--- HEADER.SVG ---")
for m in re.finditer(r'<image\s+([^>]+)>', header):
    attrs = m.group(1)
    attrs_clean = re.sub(r'(xlink:href|href)="data:[^"]*"', r'\1="[DATA_URI]"', attrs)
    print("<image", attrs_clean, ">")

with open('f:/NagendraKushwaha/scratch_ref/profile-header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    prof = f.read()

print("\n--- PROFILE-HEADER.SVG ---")
for m in re.finditer(r'<image\s+([^>]+)>', prof):
    attrs = m.group(1)
    attrs_clean = re.sub(r'(xlink:href|href)="data:[^"]*"', r'\1="[DATA_URI]"', attrs)
    print("<image", attrs_clean, ">")
