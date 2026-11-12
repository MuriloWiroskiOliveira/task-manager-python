import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DATA_FILE = DATA_DIR / "tasks.json"

def salvar_tarefas(tarefas):

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def carregar_tarefas():

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as erro:
        raise ValueError(
            "O arquivo de tarefas está com conteúdo inválido."
        ) from erro