import os
import argparse


class WagtailMaintenanceAgent:
    def __init__(self, project_path="."):
        self.project_path = project_path
        self.report = []

    def check_requirements(self):
        path = os.path.join(self.project_path, "requirements.txt")

        if not os.path.exists(path):
            self.report.append("❌ requirements.txt not found")
            return

        with open(path, "r") as f:
            content = f.read().lower()

        if "wagtail" in content:
            self.report.append("✔ Wagtail dependency found")
        else:
            self.report.append("⚠️ Wagtail not found in requirements.txt")

    def check_setup_scripts(self):
        makefile = os.path.join(self.project_path, "Makefile")
        bat = os.path.join(self.project_path, "setup.bat")

        if os.path.exists(makefile):
            self.report.append("✔ Makefile exists")
        else:
            self.report.append("⚠️ Missing Makefile (Linux/Mac setup)")

        if os.path.exists(bat):
            self.report.append("✔ setup.bat exists (Windows supported)")
        else:
            self.report.append("⚠️ Missing setup.bat (Windows users may face issues)")
    def check_manage_py(self):
        path = os.path.join(self.project_path, "manage.py")

        if os.path.exists(path):
            self.report.append("✔ Django project detected")
        else:
            self.report.append("❌ manage.py missing (not a Django project)")
    def check_structure(self):
        required_dirs = ["projects", "templates"]

        for d in required_dirs:
            full_path = os.path.join(self.project_path, d)
            if os.path.exists(full_path):
                self.report.append(f"✔ Directory found: {d}")
            else:
                self.report.append(f"⚠️ Missing directory: {d}")

    def check_readme(self):
        readme = os.path.join(self.project_path, "README.md")

        if os.path.exists(readme):
            self.report.append("✔ README.md exists")
        else:
            self.report.append("⚠️ Missing README.md")

    def suggest_improvements(self):
        
        self.report.append("\n💡 Suggestions:")
        self.report.append("- Add CI/CD using GitHub Actions")
        self.report.append("- Add .env support for configuration")
        self.report.append("- Ensure cross-platform compatibility")
        self.report.append("- Keep dependencies updated regularly")

    def run(self):
        
        print("🤖 Wagtail Starter Kit AI Maintenance Report\n")

        self.check_requirements()
        self.check_setup_scripts()
        self.check_structure()
        self.check_readme()
        self.suggest_improvements()

        for item in self.report:
            print(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AI Maintenance Agent for Wagtail Starter Kit"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Path to the project (default: current directory)"
    )

    args = parser.parse_args()

    agent = WagtailMaintenanceAgent(project_path=args.path)
    agent.run()