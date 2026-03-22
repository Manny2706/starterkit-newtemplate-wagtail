# Wagtail Portfolio Starter Kit (HTMX Powered)

A modern, cross-platform Wagtail starter kit with simplified setup, dynamic UI using HTMX, and improved developer experience.

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

### 4. Run setup

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
