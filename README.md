# POROS Web Security Audit
Dokumentasi hands-on analisis keamanan platform CTFd POROS (https://mirror.porosctf.com)

## Struktur Repository
| Folder | Bab | Tools |
|--------|-----|-------|
| 01_fondasi | Fondasi Keamanan Web | curl, testssl.sh |
| 02_scripting | Client/Server Side Scripting | Python, browser devtools |
| 03_recon | Fase Reconnaissance | nmap, whatweb, crt.sh |
| 04_dependencies | Analisis Dependensi | pip-audit, safety |
| 05_waf | Web Application Firewall | wafw00f, curl |
| 06_secure_coding | Secure Coding | bandit, semgrep |
| 07_owasp | OWASP Top 10 | OWASP ZAP, nikto |

## Target
- URL: https://mirror.porosctf.com
- Platform: CTFd
- Tujuan: Analisis keamanan + rekomendasi perbaikan

## Disclaimer
Seluruh pengujian dilakukan secara legal terhadap platform milik
sendiri (POROS). Tidak ada eksploitasi aktif yang dilakukan.
