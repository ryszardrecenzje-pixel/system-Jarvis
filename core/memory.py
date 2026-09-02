# core/memory.py
import os
import json
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "data", "logs")
MEMORY_DIR = os.path.join(BASE_DIR, "data", "memory")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)

def log_interaction(user_input: str, response: str) -> None:
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "user_input": user_input,
        "response": response,
    }

    logfile = os.path.join(LOGS_DIR, "interactions.log")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def save_memory(key: str, value: str) -> str:
    filepath = os.path.join(MEMORY_DIR, f"{key}.json")
    data = {
        "key": key,
        "value": value,
        "saved_at": datetime.now().isoformat(),
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return f"Zapisałem pamięć pod kluczem: {key}"

def load_memory(key: str) -> str:
    filepath = os.path.join(MEMORY_DIR, f"{key}.json")
    if not os.path.exists(filepath):
        return f"Nie mam zapisanej pamięci pod kluczem: {key}"

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("value", "")
