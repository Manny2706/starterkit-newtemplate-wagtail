# 🚀 Next-Gen Wagtail Starter Kit (HTMX + Automation Prototype)

An experimental Wagtail starter kit focused on **reducing maintenance overhead, simplifying setup, and improving first-time developer experience (FTDX)**.

## 🎯 Problem Statement

While exploring the official Wagtail starter templates, I identified several issues affecting developer experience and long-term maintainability:

- Multi-step setup process (8+ steps)
- Silent version inconsistencies (e.g. Wagtail downgrade)
- 30+ npm vulnerabilities
- Test suite failures on fresh setup
- High reliance on manual updates

These issues increase friction for new contributors and create ongoing maintenance burden.
## 💡 Approach: Automation + Simplicity

This project experiments with a **subtractive and automation-first approach**:

### 1. Automated Stability
- GitHub Actions (Python + Node matrix)
- Dependabot for dependency updates
- Continuous breakage detection

### 2. Simplified Setup
- One-command project bootstrap
- Reduced manual configuration steps

### 3. Native Onboarding
- Improved demo content (`demo.json`)
- Showcase real Wagtail patterns out of the box
- Avoid external JS onboarding tools


## Highlighted Changes

- Portfolio-focused starter structure
- HTMX-based dynamic projects section
- One-command setup support
- Demo content and screenshots included

## Features

- One-command setup (Windows + Linux/Mac)
- Portfolio-based reusable template
- HTMX-powered dynamic UI (no heavy JS)
- Preloaded demo content
- Cross-platform compatibility
- AI maintenance agent included

## Quick Setup

### 1. Clone

```bash
git clone <repo-url>
cd <project-folder>
```

### 2. Create and activate virtual environment

Windows (PowerShell):

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

Windows (cmd):

```bat
python -m venv env
env\Scripts\activate.bat
```

Linux/Mac:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🚀 One-Command Setup

```bash
python setup.py
```

### 5. Load demo data (optional)

```bash
python manage.py loaddata fixtures/demo.json
```

### 6. Start development server

```bash
python manage.py runserver
```

Open:

- Site: `http://127.0.0.1:8000`
- Admin: `http://127.0.0.1:8000/admin`
- Default credentials: `admin` / `password`

## Screenshots

### Homepage with Dynamic Projects Section (HTMX)

<p align="center">
  <img src="./screenshots/home.png" alt="Homepage with dynamic projects section" width="100%">
</p>

### Wagtail Admin Panel

<p align="center">
  <img src="./screenshots/admin.png" alt="Wagtail admin panel" width="100%">
</p>

### Project Page

<p align="center">
  <img src="./screenshots/project.png" alt="Project page" width="100%">
</p>



## Credits

- [Wagtail](https://wagtail.org)
- [Django](https://www.djangoproject.com/)
- [HTMX](https://htmx.org/)
