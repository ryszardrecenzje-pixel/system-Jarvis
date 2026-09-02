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


    
    return "unknown"

def plan_steps(intent: str, user_input: str) -> List[Dict]:
    steps = []

    if intent == "create_streamlit_app":
        name = user_input.replace("stwórz aplikację streamlit", "").strip()
        steps.append({"action": "generate_streamlit_app", "name": name})
        steps.append({"action": "git_commit", "message": f"Utworzono aplikację {name}"})
        return steps

    if intent == "create_python_file":
        parts = user_input.split("stwórz plik")[1].strip().split(" ")
        filename = parts[0]
        content = " ".join(parts[1:])
        steps.append({"action": "create_python_file", "filename": filename, "content": content})
        steps.append({"action": "git_commit", "message": f"Utworzono plik {filename}"})
        return steps

    if intent == "git_commit":
        steps.append({"action": "git_commit", "message": "Automatyczny commit Jarvisa"})
        return steps

    if intent == "git_push":
        steps.append({"action": "git_push"})
        return steps

    if intent == "save_memory":
        parts = user_input.replace("zapamiętaj", "").strip().split(" ", 1)
        if len(parts) == 2:
            key, value = parts
            steps.append({"action": "save_memory", "key": key, "value": value})
        return steps

    if intent == "load_memory":
        key = user_input.replace("przypomnij", "").strip()
        steps.append({"action": "load_memory", "key": key})
        return steps

    if intent == "list_directory":
    path = user_input.replace("pokaż katalog", "").strip()
    return [{"action": "list_directory", "path": path}]

    if intent == "create_folder":
        path = user_input.replace("stwórz folder", "").strip()
        return [{"action": "create_folder", "path": path}]
    
    if intent == "delete_file":
        path = user_input.replace("usuń plik", "").strip()
        return [{"action": "delete_file", "path": path}]
    
    if intent == "read_file":
        path = user_input.replace("odczytaj plik", "").strip()
        return [{"action": "read_file", "path": path}]
    
    if intent == "write_file":
        parts = user_input.replace("zapisz plik", "").strip().split(" ", 1)
        path = parts[0]
        content = parts[1] if len(parts) > 1 else ""
        return [{"action": "write_file", "path": path, "content": content}]
        if intent == "load_csv":
    path = user_input.replace("wczytaj csv", "").strip()
    return [{"action": "load_csv", "path": path}]

    if intent == "load_json":
        path = user_input.replace("wczytaj json", "").strip()
        return [{"action": "load_json", "path": path}]
    
    if intent == "load_excel":
        path = user_input.replace("wczytaj excel", "").strip()
        return [{"action": "load_excel", "path": path}]
    
    if intent == "describe_data":
        return [{"action": "describe_data"}]
    
    if intent == "plot_column":
        parts = user_input.replace("wykres", "").strip().split(" ")
        column = parts[-1]
        return [{"action": "plot_column", "column": column}]



    return [{"action": "unknown"}]
