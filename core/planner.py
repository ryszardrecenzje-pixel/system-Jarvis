# core/planner.py
from typing import List, Dict

def analyze_intent(user_input: str) -> str:
    user_input = user_input.lower()

    if "aplikację streamlit" in user_input:
        return "create_streamlit_app"

    if "stwórz plik" in user_input:
        return "create_python_file"

    if "commit" in user_input:
        return "git_commit"

    if "push" in user_input:
        return "git_push"

    if "zapamiętaj" in user_input:
        return "save_memory"

    if "przypomnij" in user_input:
        return "load_memory"

    if "pokaż katalog" in user_input:
        return "list_directory"

    if "stwórz folder" in user_input:
        return "create_folder"

    if "usuń plik" in user_input:
        return "delete_file"

    if "odczytaj plik" in user_input:
        return "read_file"

    if "zapisz plik" in user_input:
        return "write_file"

    if "wczytaj csv" in user_input:
        return "load_csv"

    if "wczytaj json" in user_input:
        return "load_json"

    if "wczytaj excel" in user_input:
        return "load_excel"

    if "statystyki" in user_input:
        return "describe_data"

    if "wykres" in user_input:
        return "plot_column"

    if "lista aplikacji" in user_input:
        return "list_apps"

    if "stwórz aplikację" in user_input:
        return "create_app"

    if "modyfikuj aplikację" in user_input:
        return "modify_app"

    if "dashboard" in user_input:
        return "generate_dashboard"

    if "readme" in user_input:
        return "generate_readme"

    if "struktura repo" in user_input:
        return "document_repo"

    if "raport techniczny" in user_input:
        return "technical_report"

    if "sugestia workflow" in user_input:
        return "workflow_suggestion"

    if "analiza projektu" in user_input:
        return "analyze_project"

    if "workflow" in user_input:
        return "build_workflow"

    return "unknown"
