# core/ai.py
from actions.codegen import create_python_file, append_to_file, generate_streamlit_app
from actions.github import git_commit, git_push
from core.memory import log_interaction, save_memory, load_memory

def handle_user_input(user_input: str) -> str:
    original_input = user_input
    user_input = user_input.lower()

    # Zapamiętywanie
    if user_input.startswith("zapamiętaj"):
        # przykład: "zapamiętaj projekt1 to jest opis projektu"
        parts = user_input.replace("zapamiętaj", "").strip().split(" ", 1)
        if len(parts) == 2:
            key, value = parts
            response = save_memory(key, value)
            log_interaction(original_input, response)
            return response
        response = "Podaj klucz i wartość, np.: zapamiętaj projekt1 opis projektu."
        log_interaction(original_input, response)
        return response

    # Przypominanie
    if user_input.startswith("przypomnij"):
        # przykład: "przypomnij projekt1"
        key = user_input.replace("przypomnij", "").strip()
        value = load_memory(key)
        response = f"Pamiętam pod {key}: {value}"
        log_interaction(original_input, response)
        return response

    # Tworzenie aplikacji Streamlit
    if "stwórz aplikację streamlit" in user_input:
        name = user_input.replace("stwórz aplikację streamlit", "").strip()
        filename, content = generate_streamlit_app(name)
        response = f"Utworzono aplikację Streamlit: {filename}"
        log_interaction(original_input, response)
        return response

    # Tworzenie pliku Python
    if "stwórz plik" in user_input:
        parts = user_input.split("stwórz plik")[1].strip().split(" ")
        filename = parts[0]
        content = " ".join(parts[1:])
        response = create_python_file(filename, content)
        log_interaction(original_input, response)
        return response

    # Commit
    if "commit" in user_input:
        response = git_commit("Automatyczny commit Jarvisa")
        log_interaction(original_input, response)
        return response

    # Push
    if "push" in user_input:
        response = git_push()
        log_interaction(original_input, response)
        return response

    response = "Nie rozumiem jeszcze tego polecenia, ale mogę się tego nauczyć."
    log_interaction(original_input, response)
    return response
