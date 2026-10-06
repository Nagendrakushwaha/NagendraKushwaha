import urllib.request
import json
from collections import Counter

req = urllib.request.Request('https://api.github.com/users/Nagendrakushwaha/repos?per_page=100', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as res:
        repos = json.loads(res.read().decode())
        print(f"Total repos: {len(repos)}")
        total_stars = sum(r.get('stargazers_count', 0) for r in repos)
        total_forks = sum(r.get('forks_count', 0) for r in repos)
        total_watchers = sum(r.get('watchers_count', 0) for r in repos)
        langs = Counter(r.get('language') for r in repos if r.get('language'))
        print(f"Total Stars: {total_stars}")
        print(f"Total Forks: {total_forks}")
        print(f"Languages: {dict(langs)}")
        for r in sorted(repos, key=lambda x: x.get('stargazers_count', 0), reverse=True):
            print(f"- {r['name']}: stars={r['stargazers_count']}, forks={r['forks_count']}, lang={r['language']}")
except Exception as e:
    print("Error:", e)
