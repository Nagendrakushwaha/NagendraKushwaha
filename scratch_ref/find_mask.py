with open('f:/NagendraKushwaha/scratch_ref/header.svg', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'portraitMask' in line or 'portrait' in line or 'g mask=' in line or 'clipPath' in line:
        start = max(0, i - 5)
        end = min(len(lines), i + 15)
        print(f"--- MATCH AT LINE {i} ---")
        for j in range(start, end):
            # shorten base64
            l = lines[j]
            if 'data:' in l:
                l = l[:l.find('data:')] + 'data:..."/>\n'
            print(f"{j+1}: {l}", end='')
        print("\n" + "="*40)
