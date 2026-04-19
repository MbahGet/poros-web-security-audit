# OWASP Top 10 2021 – Checklist Evaluasi CTFd POROS
**Target:** https://mirror.porosctf.com  
**Platform:** CTFd  
**Tanggal Evaluasi:** April 2026  

---

## A01 – Broken Access Control
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Akses ke /admin diproteksi autentikasi | AMAN | Redirect ke /login |
| Endpoint API /api/v1/challenges/<id> tidak bisa diakses tanpa login | PERLU UJI | Potensi IDOR |
| User biasa tidak bisa akses data user lain | PERLU UJI | /api/v1/users/<id> |
| Flag tidak bisa diakses langsung tanpa solve challenge | AMAN | Terproteksi backend |

## A02 – Cryptographic Failures
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| HTTPS aktif dengan sertifikat valid | AMAN | TLS 1.2/1.3 aktif |
| HTTP redirect ke HTTPS | AMAN | 301 redirect |
| Password di-hash (bukan plaintext) | AMAN | CTFd pakai bcrypt |
| Cookie menggunakan flag Secure | PERLU CEK | Lihat headers.txt |
| Tidak ada data sensitif di URL | AMAN | Token tidak di URL |

## A03 – Injection
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| SQL Injection pada form login | AMAN | SQLAlchemy ORM |
| SQL Injection pada search/filter | AMAN | Parameterized query |
| XSS pada kolom input username | PERLU UJI | Lihat xss_results.txt |
| XSS pada deskripsi challenge | PERLU UJI | Render HTML? |
| Command Injection | AMAN | Tidak ada fitur OS command |

## A04 – Insecure Design
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Rate limiting pada flag submission | PERLU CEK | Brute force flag? |
| Rate limiting pada login | PERLU CEK | Brute force password? |
| Pembatasan jumlah akun per IP | PERLU CEK | Mass registration? |
| Logika skor tidak bisa dimanipulasi | AMAN | Server-side calculation |

## A05 – Security Misconfiguration
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Debug mode dinonaktifkan | PERLU CEK | Flask DEBUG=False? |
| Error message tidak mengekspos stack trace | PERLU CEK | Cek halaman error |
| Server header tidak mengekspos versi | PERLU CEK | Lihat headers.txt |
| Directory listing dinonaktifkan | AMAN | 403 pada /static/ |
| File .env tidak terekspos | AMAN | 404 pada /.env |
| File .git tidak terekspos | AMAN | 404 pada /.git/HEAD |

## A06 – Vulnerable and Outdated Components
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Dependensi Python up-to-date | PERLU UPDATE | Lihat pip_audit_report.txt |
| Dependensi JavaScript up-to-date | PERLU CEK | Lihat npm_audit_report.txt |
| CTFd versi terbaru | PERLU CEK | Cek versi di GitHub |
| Tidak ada CVE kritis pada dependensi | PERLU CEK | Lihat safety_report.txt |

## A07 – Identification and Authentication Failures
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Password policy memadai | PERLU CEK | Minimum length? |
| Session ID di-regenerate setelah login | PERLU CEK | Flask-Login default |
| Session timeout diimplementasikan | PERLU CEK | Konfigurasi CTFd |
| Cookie HttpOnly flag aktif | PERLU CEK | Lihat cookie_analysis.txt |
| Tidak ada default credential | AMAN | Admin dibuat manual |

## A08 – Software and Data Integrity Failures
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Integritas dependensi diverifikasi | PERLU CEK | Hash verification? |
| Update CTFd melalui channel resmi | AMAN | GitHub official repo |
| Subresource Integrity pada CDN assets | PERLU CEK | Cek tag script di HTML |
| CSRF protection aktif | AMAN | Flask-WTF CSRF token |

## A09 – Security Logging and Monitoring Failures
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Login gagal di-log | PERLU CEK | Perlu akses server |
| Aktivitas admin di-log | PERLU CEK | Perlu akses server |
| Alert untuk aktivitas mencurigakan | PERLU CEK | Cloudflare alerting? |
| Log tidak bisa dimodifikasi user | AMAN | Tidak ada akses log |

## A10 – Server-Side Request Forgery (SSRF)
| Item | Status | Bukti/Catatan |
|------|--------|---------------|
| Fitur import/external URL divalidasi | PERLU CEK | CTFd import challenge? |
| Tidak ada fitur fetch URL arbitrary | AMAN | Tidak ada fitur ini |
| Webhook URL divalidasi | PERLU CEK | Jika ada integrasi |

---

## Ringkasan Temuan

| Kategori | Aman | Perlu Uji/Perbaikan |
|----------|------|---------------------|
| A01 Broken Access Control | 2 | 2 |
| A02 Cryptographic Failures | 4 | 1 |
| A03 Injection | 4 | 2 |
| A04 Insecure Design | 1 | 3 |
| A05 Security Misconfiguration | 3 | 3 |
| A06 Vulnerable Components | 0 | 4 |
| A07 Auth Failures | 1 | 4 |
| A08 Data Integrity | 2 | 2 |
| A09 Logging & Monitoring | 1 | 3 |
| A10 SSRF | 1 | 2 |

## Rekomendasi Prioritas Tinggi
1. Update semua dependensi dengan CVE (A06)
2. Implementasi rate limiting pada login dan flag submission (A04)
3. Aktifkan Content-Security-Policy header (A05)
4. Verifikasi cookie flags HttpOnly dan Secure (A07)
5. Implementasi alerting Cloudflare untuk anomali traffic (A09)
