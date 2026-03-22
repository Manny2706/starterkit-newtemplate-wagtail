import os
import sys

def run(command):
    print(f"\nRunning: {command}")
    result = os.system(command)
    if result != 0:
        print(f"Failed: {command}")
        sys.exit(1)

def main():
    print("Setting up Wagtail Starter Kit...\n")

    run("pip install -r requirements.txt")
    run("python manage.py migrate")
    run("python manage.py createcachetable")
    run("python manage.py load_initial_data")

    print("\n✅ Setup complete! Run: python manage.py runserver")

if __name__ == "__main__":
    main()