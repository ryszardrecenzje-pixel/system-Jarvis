# core/ai.py
from actions.codegen import create_python_file, append_to_file, generate_streamlit_app
from actions.github import git_commit, git_push

def handle_user_input(user_input: str) -> str:
    user_input = user_input.lower()

    # Tworzenie aplikacji Streamlit
    if "stwórz aplikację streamlit" in user_input:
        name = user_input.replace("stwórz aplikację streamlit", "").strip()
        filename, content = generate_streamlit_app(name)
        return f"Utworzono aplikację Streamlit: {filename}"

    # Tworzenie pliku Python
    if "stwórz plik" in user_input:
        parts = user_input.split("stwórz plik")[1].strip().split(" ")
        filename = parts[0]
        content = " ".join(parts[1:])
        return create_python_file(filename, content)

    # Commit
    if "commit" in user_input:
        return git_commit("Automatyczny commit Jarvisa")

    # Push
    if "push" in user_input:
        return git_push()

    return "Nie rozumiem jeszcze tego polecenia, ale mogę się tego nauczyć."
