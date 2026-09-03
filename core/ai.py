# core/ai.py
from actions.codegen import create_python_file, append_to_file, generate_streamlit_app
from actions.github import git_commit, git_push
from core.memory import log_interaction, save_memory, load_memory
from core.planner import analyze_intent, plan_steps
from actions.data_analysis import load_csv, load_json, load_excel, describe_dataframe, plot_column
from actions.streamlit_apps import list_apps, create_app, modify_app, generate_dashboard
from actions.documentation import generate_readme, document_repo_structure, generate_technical_report, workflow_suggestion
from core.workflow import analyze_project, build_workflow
from actions.system import list_directory, create_folder, delete_file, read_file, write_file


def handle_user_input(user_input: str) -> str:
    original_input = user_input

    intent = analyze_intent(user_input)
    steps = plan_steps(intent, user_input)

    results = []
    df = None

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

        # ANALIZA DANYCH
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
            if df is not None:
                results.append(describe_dataframe(df))
            else:
                results.append("Najpierw wczytaj dane.")

        elif action == "plot_column":
            if df is not None:
                results.append(plot_column(df, step["column"]))
            else:
                results.append("Najpierw wczytaj dane.")

        # SYSTEM FILES
        elif action == "list_directory":
            results.append(list_directory(step["path"]))

        elif action == "create_folder":
            results.append(create_folder(step["path"]))

        elif action == "delete_file":
            results.append(delete_file(step["path"]))

        elif action == "read_file":
            results.append(read_file(step["path"]))

        elif action == "write_file":
            results.append(write_file(step["path"], step["content"]))

        # STREAMLIT APPS
        elif action == "list_apps":
            results.append(list_apps())

        elif action == "create_app":
            results.append(create_app(step["name"]))

        elif action == "modify_app":
            results.append(modify_app(step["name"], step["new_code"]))

        elif action == "generate_dashboard":
            if df is not None:
                results.append(generate_dashboard(step["name"], df))
            else:
                results.append("Najpierw wczytaj dane, aby wygenerować dashboard.")

        # DOCUMENTATION
        elif action == "generate_readme":
            results.append(generate_readme(step["app_name"], step["description"]))

        elif action == "document_repo":
            results.append(document_repo_structure())

        elif action == "technical_report":
            results.append(generate_technical_report(step["app_name"]))

        elif action == "workflow_suggestion":
            results.append(workflow_suggestion(step["input"]))

        # WORKFLOW
        elif action == "analyze_project":
            results.append(analyze_project())

        elif action == "build_workflow":
            results.append(build_workflow(step["input"]))

        else:
            results.append("Nie rozumiem tego polecenia.")

    final_response = "\n".join(results)
    log_interaction(original_input, final_response)

    return final_response
