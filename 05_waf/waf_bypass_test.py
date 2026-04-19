#!/usr/bin/env python3
"""
WAF Response Observation Script
Mengamati bagaimana WAF merespons berbagai pola request
TIDAK melakukan eksploitasi nyata
"""
import requests

TARGET = "https://mirror.porosctf.com"

# Test cases – mengamati kode respons & apakah WAF memblokir
test_cases = [
    # (deskripsi, url, method, data)
    ("Normal GET",          f"{TARGET}/",         "GET",  None),
    ("Admin path",          f"{TARGET}/admin",    "GET",  None),
    ("SQLi pattern in URL", f"{TARGET}/?id=1'",   "GET",  None),
    ("XSS pattern in URL",  f"{TARGET}/?q=<script>", "GET", None),
    ("Path traversal",      f"{TARGET}/../../etc/passwd", "GET", None),
    ("User-Agent: scanner", f"{TARGET}/",         "GET",  None),  # akan set UA khusus
]

results = []
headers_normal = {"User-Agent": "Mozilla/5.0 (compatible; security-research)"}
headers_scanner = {"User-Agent": "sqlmap/1.0"}

print("=== WAF Response Observation ===\n")
for desc, url, method, data in test_cases:
    ua = headers_scanner if "scanner" in desc else headers_normal
    try:
        r = requests.request(method, url, data=data, 
                            headers=ua, timeout=10, allow_redirects=False)
        status = r.status_code
        waf_blocked = status in [403, 429, 503] or "cloudflare" in r.text.lower()
        result = f"[{status}] {'BLOCKED' if waf_blocked else 'ALLOWED'} – {desc}"
    except Exception as e:
        result = f"[ERR] {desc}: {e}"
    print(result)
    results.append(result)

with open("waf_bypass_test_results.txt", "w") as f:
    f.write("\n".join(results))
print("\nSaved to waf_bypass_test_results.txt")
