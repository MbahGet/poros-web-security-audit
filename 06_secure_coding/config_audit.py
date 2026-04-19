#!/usr/bin/env python3
"""
Audit konfigurasi CTFd dari perspektif secure coding
"""
import os, json, re

CTFD_PATH = "../04_dependencies/ctfd_source"

checks = []

# Cek apakah SECRET_KEY ada dalam kode (hardcoded = buruk)
for root, _, files in os.walk(CTFD_PATH):
    for fname in files:
        if fname.endswith(".py"):
            fpath = os.path.join(root, fname)
            with open(fpath, encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # Cek hardcoded secret
            if re.search(r'SECRET_KEY\s*=\s*["\'][^"\']{8,}["\']', content):
                checks.append(f"Possible hardcoded SECRET_KEY in {fpath}")
            # Cek debug mode
            if re.search(r'DEBUG\s*=\s*True', content):
                checks.append(f"DEBUG=True found in {fpath}")
            # Cek SQL query manual (bukan ORM)
            if re.search(r'execute\(.*%.*\)', content):
                checks.append(f"Possible raw SQL with % formatting in {fpath}")

if not checks:
    checks.append("Tidak ditemukan konfigurasi berbahaya yang hardcoded")

print("\n".join(checks))
with open("config_audit_results.txt", "w") as f:
    f.write("\n".join(checks))
