# actions/github.py
import subprocess

def git_commit(message: str) -> str:
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        return "Commit wykonany."
    except Exception as e:
        return f"Błąd commitowania: {e}"

def git_push() -> str:
    try:
        subprocess.run(["git", "push"], check=True)
        return "Push wykonany."
    except Exception as e:
        return f"Błąd pushowania: {e}"
