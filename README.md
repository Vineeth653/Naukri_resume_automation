# Naukri Resume Automation (GitHub Actions Attempt)

This repository is an attempt to automate refreshing a resume on [Naukri.com](https://www.naukri.com) using **Selenium** inside **GitHub Actions**.

---

## 📌 What We Tried
- Used **Python + Selenium + ChromeDriver** to log in and upload the latest resume.
- Configured a **GitHub Actions workflow** (`.github/workflows/refresh.yml`) to:
  - Run daily
  - Use repository secrets for credentials
  - Upload resume from the repo
  - Capture screenshots on failure

---

## ❌ Why It Doesn’t Work
Unfortunately, Naukri blocks cloud runner IPs (GitHub, AWS, Azure, etc.) using **Akamai firewall/CDN protection**.  
When the script runs inside GitHub Actions, Naukri responds with: 
```Access Denied – You don't have permission to access this server.```

This means the automation cannot proceed on GitHub-hosted runners.

---

## ✅ Alternatives
1. **Run the script locally** using:
   - Windows Task Scheduler
   - Linux/macOS `cron`
2. **Use a self-hosted GitHub runner** (your own machine → no IP block).
3. (Advanced) Use a **residential proxy** so Naukri doesn’t detect cloud infra.

---

## 🔗 Working Local Version
Since GitHub-hosted runners are blocked, the working **local version** of the script is maintained here:

👉 [Naukri Resume Automation (Local Script)](https://github.com/Vineeth653/Naukri_resume_automation_local)

---

## 📂 Repo Structure
```.
├── refresh_resume.py # Selenium script
├── .github/workflows/ # GitHub Actions workflow
├── resume.pdf # Resume (example)
└── README.md
```
---
