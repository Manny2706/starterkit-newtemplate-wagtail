import click
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path.cwd()
FIXTURE_PATH = BASE_DIR / "fixtures" / "demo.json"


def run(cmd, msg, fail_ok=False):
    click.echo(f"\n[*] {msg}...")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        click.echo(f"[✗] Failed: {msg}")
        if fail_ok:
            return False
        sys.exit(1)


def check_env():
    if sys.prefix == sys.base_prefix:
        click.echo("[✗] Activate virtual environment first")
        sys.exit(1)


def is_db_initialized():
    return (BASE_DIR / "db.sqlite3").exists()


@click.group()
def cli():
    """Wagtail Starter CLI"""
    pass


# -------------------------
# SETUP COMMAND
# -------------------------
@cli.command()
@click.option("--skip-frontend", is_flag=True, help="Skip npm install")
@click.option("--no-data", is_flag=True, help="Skip demo data loading")
def setup(skip_frontend, no_data):
    """Setup full project"""

    click.echo("🚀 Initializing Wagtail Starter Kit...\n")

    check_env()

    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        "Installing Python dependencies")

    if not skip_frontend:
        try:
            run(["npm", "ci"], "Installing Node dependencies", fail_ok=True)
        except FileNotFoundError:
            click.echo("[!] npm not found, skipping frontend")

    if not is_db_initialized():
        run([sys.executable, "manage.py", "migrate"], "Running migrations")
        run([sys.executable, "manage.py", "createcachetable"], "Creating cache table")

        if not no_data and FIXTURE_PATH.exists():
            loaded = run(
                [sys.executable, "manage.py", "loaddata", str(FIXTURE_PATH)],
                "Loading demo data",
                fail_ok=True
            )
            if not loaded:
                run([sys.executable, "manage.py", "load_initial_data"],
                    "Loading fallback data")
    else:
        click.echo("[i] DB already exists, skipping setup")

    click.echo("\n✅ Setup complete!")


# -------------------------
# DEV COMMAND
# -------------------------
@cli.command()
def dev():
    """Run development server"""
    run([sys.executable, "manage.py", "runserver"], "Starting server")


# -------------------------
# RESET COMMAND
# -------------------------
@cli.command()
def reset():
    """Reset database"""
    db = BASE_DIR / "db.sqlite3"
    if db.exists():
        db.unlink()
        click.echo("[!] Database removed")
    else:
        click.echo("[i] No database found")


if __name__ == "__main__":
    cli()