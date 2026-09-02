# core/ai.py
from actions.codegen import create_python_file, append_to_file, generate_streamlit_app
from actions.github import git_commit, git_push
from core.memory import log_interaction, save_memory, load_memory
from core.planner import analyze_intent, plan_steps
from actions.data_analysis import load_csv, load_json, load_excel, describe_dataframe, plot_column



def handle_user_input(user_input: str) -> str:
    original_input = user_input

    # 1. Analiza intencji
    intent = analyze_intent(user_input)

    # 2. Tworzenie planu
    steps = plan_steps(intent, user_input)

    # 3. Wykonanie kroków
    results = []
    for step in steps:
        action = step["action"]

        if action == "generate_streamlit_app":
            filename, content = generate_streamlit_app(step["name"])
            results.append(f"✔ Utworzono aplikację Streamlit: {filename}")

        elif action == "create_python_file":
            result = create_python_file(step["filename"], step["content"])
            results.append(f"✔ {result}")

        elif action == "git_commit":
            result = git_commit(step["message"])
            results.append(f"✔ Commit: {result}")

        elif action == "git_push":
            result = git_push()
            results.append(f"✔ Push: {result}")

        elif action == "save_memory":
            result = save_memory(step["key"], step["value"])
            results.append(f"✔ {result}")

        elif action == "load_memory":
            value = load_memory(step["key"])
            results.append(f"✔ Pamięć: {value}")
        elif action == "load_csv":
            df = load_csv(step["path"])
            results.append(df)
        
        elif action == "load_json":
            df = load_json(step["path"])
            results.append(df)
        
        elif action == "load_excel":
            df = load_excel(step["path"])
            results.append(df)
        
        elif action == "describe_data":
            if "df" in locals():
                results.append(describe_dataframe(df))
            else:
                results.append("Najpierw wczytaj dane.")
        
        elif action == "plot_column":
            if "df" in locals():
                results.append(plot_column(df, step["column"]))
    else:
        results.append("Najpierw wczytaj dane.")
            

    # 4. Logowanie
    final_response = "\n".join(results)
    log_interaction(original_input, final_response)

    return final_response


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
