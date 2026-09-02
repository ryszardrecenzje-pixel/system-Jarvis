# core/workflow.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def analyze_project():
    """Analizuje projekt i wykrywa brakujące elementy."""
    missing = []

    # Sprawdź dokumentację repo
    if not os.path.exists(os.path.join(BASE_DIR, "PROJECT_STRUCTURE.md")):
        missing.append("Brak dokumentacji struktury repozytorium.")

    # Sprawdź folder aplikacji Streamlit
    apps_dir = os.path.join(BASE_DIR, "streamlit_apps")
    if not os.path.exists(apps_dir):
        missing.append("Brak folderu streamlit_apps.")
    else:
        apps = os.listdir(apps_dir)
        if not apps:
            missing.append("Brak aplikacji Streamlit.")
        else:
            for app in apps:
                readme = os.path.join(apps_dir, app, "README.md")
                report = os.path.join(apps_dir, app, "REPORT.md")
                if not os.path.exists(readme):
                    missing.append(f"Aplikacja {app} nie ma README.")
                if not os.path.exists(report):
                    missing.append(f"Aplikacja {app} nie ma raportu technicznego.")

    if not missing:
        return "Projekt wygląda kompletnie."

    return "Wykryto braki:\n" + "\n".join(missing)


def suggest_next_steps(user_input: str):
    """Proponuje kolejne kroki na podstawie polecenia użytkownika."""
    if "aplikację" in user_input:
        return [
            "Dodaj README do aplikacji.",
            "Wygeneruj raport techniczny.",
            "Stwórz dashboard na podstawie danych.",
            "Dodaj testy jednostkowe."
        ]

    if "dane" in user_input:
        return [
            "Wygeneruj dashboard.",
            "Stwórz aplikację analityczną.",
            "Zapisz raport danych.",
            "Dodaj wizualizacje."
        ]

    return [
        "Commit zmian.",
        "Push na GitHub.",
        "Wygeneruj dokumentację repozytorium.",
        "Przeprowadź analizę projektu."
    ]


def build_workflow(user_input: str):
    """Tworzy automatyczny workflow na podstawie polecenia."""
    steps = suggest_next_steps(user_input)

    workflow = "# Workflow Jarvisa\n\n"
    workflow += "Polecenie użytkownika:\n"
    workflow += f"- {user_input}\n\n"
    workflow += "Proponowane kroki:\n"

    for step in steps:
        workflow += f"- {step}\n"

    workflow_path = os.path.join(BASE_DIR, "WORKFLOW.md")

    with open(workflow_path, "w", encoding="utf-8") as f:
        f.write(workflow)

    return f"Wygenerowano workflow: {workflow_path}"
