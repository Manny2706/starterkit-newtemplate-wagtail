import subprocess
import sys


def run(command, description):
    print(f"\n[*] {description}...")
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"[✗] Failed during: {description}")
        sys.exit(1)


def main():
    print("🚀 Initializing NextGen Wagtail Starter Kit...\n")

    # Python dependencies
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        "Installing Python dependencies")

    # Node dependencies (if package.json exists)
    try:
        run(["npm", "ci"], "Installing Node dependencies")
    except FileNotFoundError:
        print("[!] npm not found or not required, skipping...")

    # Django setup
    run([sys.executable, "manage.py", "migrate"],
        "Applying database migrations")

    run([sys.executable, "manage.py", "createcachetable"],
        "Creating cache table")

    # Try demo data first, fallback to custom command
    try:
        run([sys.executable, "manage.py", "loaddata", "demo.json"],
            "Loading demo data")
    except SystemExit:
        run([sys.executable, "manage.py", "load_initial_data"],
            "Loading initial data")

    print("\n✅ Setup complete!")
    print("👉 Run: python manage.py runserver")


if __name__ == "__main__":
    main()