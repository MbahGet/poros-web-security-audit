#!/usr/bin/env python3
"""
XSS Test Script untuk CTFd POROS
Hanya menguji apakah output di-escape dengan benar — TIDAK melakukan eksploitasi
"""
import requests
import html

TARGET = "https://mirror.porosctf.com"

# Payload yang digunakan untuk cek escaping (bukan eksploitasi)
TEST_PAYLOADS = [
    "<script>alert(1)</script>",
    "<img src=x>",
    "'\"><b>test</b>",
    "{{7*7}}",          # SSTI check
    "${7*7}",           # template injection
]

def check_reflection(url, param, payload):
    """Cek apakah payload di-reflect tanpa encoding"""
    try:
        r = requests.get(url, params={param: payload}, timeout=10)
        escaped = html.escape(payload)
        
        if payload in r.text and escaped not in r.text:
            return "POTENTIAL XSS: payload reflected unescaped"
        elif escaped in r.text:
            return "SAFE: payload properly escaped"
        else:
            return "payload not reflected"
    except Exception as e:
        return f"ERROR: {e}"

print("=== XSS Reflection Test ===\n")
endpoints = [
    (f"{TARGET}/", "q"),
    (f"{TARGET}/register", "name"),
]

results = []
for url, param in endpoints:
    for payload in TEST_PAYLOADS:
        result = check_reflection(url, param, payload)
        line = f"[{param}] {payload[:30]:<30} → {result}"
        print(line)
        results.append(line)

with open("xss_results.txt", "w") as f:
    f.write("\n".join(results))

print("\nResults saved to xss_results.txt")
