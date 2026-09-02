# actions/documentation.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def generate_readme(app_name: str, description: str):
    readme_path = os.path.join(BASE_DIR, "streamlit_apps", app_name, "README.md")

    content = f"""
# {app_name}

{description}

## Uruchamianie

