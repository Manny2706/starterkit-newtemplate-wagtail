import subprocess
import sys


def run(command, description, fail_ok=False):
    print(f"\n[*] {description}...")
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"[✗] Failed during: {description}")
        if fail_ok:
            return False
        sys.exit(1)


def main():
    print("Initializing NextGen Wagtail Starter Kit...\n")

    # Python dependencies
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        "Installing Python dependencies")

    # Node dependencies are optional for backend-only setup.
    try:
        npm_ok = run(["npm", "ci"], "Installing Node dependencies", fail_ok=True)
        if not npm_ok:
            print("[!] npm install failed, continuing with Django-only setup...")
    except FileNotFoundError:
        print("[!] npm not found or not required, skipping...")

    # Django setup
    run([sys.executable, "manage.py", "migrate"],
        "Applying database migrations")

    run([sys.executable, "manage.py", "createcachetable"],
        "Creating cache table")

    # Try fixture file first, then fallback to custom command.
    demo_loaded = run(
        [sys.executable, "manage.py", "loaddata", "fixtures/demo.json"],
        "Loading demo data",
        fail_ok=True,
    )

    if not demo_loaded:
        run([sys.executable, "manage.py", "load_initial_data"],
            "Loading initial data")

    print("\nSetup complete!")
    print(" Run: python manage.py runserver")


if __name__ == "__main__":
    main()