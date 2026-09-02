# actions/system.py
import os
import shutil

def list_directory(path: str) -> str:
    if not os.path.exists(path):
        return f"Katalog {path} nie istnieje."

    items = os.listdir(path)
    if not items:
        return f"Katalog {path} jest pusty."

    result = "\n".join(items)
    return f"Zawartość katalogu {path}:\n{result}"


def create_folder(path: str) -> str:
    try:
        os.makedirs(path, exist_ok=True)
        return f"Utworzono folder: {path}"
    except Exception as e:
        return f"Błąd tworzenia folderu: {e}"


def delete_file(path: str) -> str:
    if not os.path.exists(path):
        return f"Plik {path} nie istnieje."

    try:
        os.remove(path)
        return f"Usunięto plik: {path}"
    except Exception as e:
        return f"Błąd usuwania pliku: {e}"


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return f"Plik {path} nie istnieje."

    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Błąd odczytu pliku: {e}"


def write_file(path: str, content: str) -> str:
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Zapisano plik: {path}"
    except Exception as e:
        return f"Błąd zapisu pliku: {e}"
