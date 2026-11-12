import task_manager
import storage
import pytest

def test_cadastrar_tarefa(monkeypatch):

    tarefas = []

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    entradas = iter([
        "Estudar Python",
        "Aprender testes automatizados"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(entradas)
    )

    task_manager.cadastrar_tarefa(tarefas)

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"
    assert tarefas[0]["descricao"] == "Aprender testes automatizados"
    assert tarefas[0]["id"] == 1
    assert tarefas[0]["concluida"] is False


def test_concluir_tarefa(monkeypatch):

    tarefas = [
        {
            "id": 1,
            "titulo": "Estudar Python",
            "descricao": "Estudar testes automatizados",
            "concluida": False
        }
    ]

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "1"
    )

    task_manager.concluir_tarefa(tarefas)

    assert tarefas[0]["concluida"] is True


def test_excluir_tarefa(monkeypatch):

    tarefas = [
        {
            "id": 1,
            "titulo": "Estudar Python",
            "descricao": "Estudar testes automatizados",
            "concluida": False
        }
    ]

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "1"
    )

    task_manager.excluir_tarefa(tarefas)

    assert len(tarefas) == 0


def test_cadastrar_tarefa_sem_titulo(monkeypatch):

    tarefas = []

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    entradas = iter([
        "",
        "   ",
        "Estudar Python",
        "Aprender validação"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: next(entradas)
    )

    task_manager.cadastrar_tarefa(tarefas)

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Estudar Python"


def test_concluir_tarefa_inexistente(monkeypatch):

    tarefas = [
        {
            "id": 1,
            "titulo": "Estudar Python",
            "descricao": "Praticar programação",
            "concluida": False
        }
    ]

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "99"
    )

    task_manager.concluir_tarefa(tarefas)

    assert tarefas[0]["concluida"] is False


def test_concluir_tarefa_com_id_invalido(monkeypatch):

    tarefas = [
        {
            "id": 1,
            "titulo": "Estudar Python",
            "descricao": "Praticar programação",
            "concluida": False
        }
    ]

    monkeypatch.setattr(
        task_manager,
        "salvar_tarefas",
        lambda tarefas: None
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda mensagem: "abc"
    )

    task_manager.concluir_tarefa(tarefas)

    assert len(tarefas) == 1
    assert tarefas[0]["concluida"] is False



def test_salvar_e_carregar_tarefas(monkeypatch, tmp_path):

    monkeypatch.setattr(storage, "DATA_DIR", tmp_path)
    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        tmp_path / "tasks.json"
    )

    tarefas_originais = [
        {
            "id": 1,
            "titulo": "Estudar Python",
            "descricao": "Aprender armazenamento JSON",
            "concluida": False
        },
        {
            "id": 2,
            "titulo": "Estudar testes",
            "descricao": "Aprender pytest",
            "concluida": True
        }
    ]

    storage.salvar_tarefas(tarefas_originais)

    tarefas_carregadas = storage.carregar_tarefas()

    assert tarefas_carregadas == tarefas_originais


def test_carregar_arquivo_inexistente(monkeypatch, tmp_path):

    monkeypatch.setattr(storage, "DATA_FILE", tmp_path / "inexistente.json")

    tarefas = storage.carregar_tarefas()

    assert tarefas == []

def test_carregar_arquivo_corrompido(monkeypatch, tmp_path):

    arquivo = tmp_path / "corrompido.json"

    arquivo.write_text(
        "{ isso não é um JSON válido }",
        encoding="utf-8"
    )

    monkeypatch.setattr(storage, "DATA_FILE", arquivo)

    with pytest.raises(ValueError):
        storage.carregar_tarefas()
