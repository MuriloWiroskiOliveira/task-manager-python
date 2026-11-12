
# Task Manager

Um gerenciador de tarefas desenvolvido em Python, executado pelo terminal, com armazenamento persistente em arquivos JSON.

## Sobre o projeto

O Task Manager é uma aplicação de gerenciamento de tarefas que permite ao usuário cadastrar, visualizar, concluir e excluir tarefas.

O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de programação, organização de código, manipulação de arquivos e testes automatizados.

## Funcionalidades

- Cadastrar novas tarefas.
- Listar tarefas cadastradas.
- Marcar tarefas como concluídas.
- Excluir tarefas.
- Gerar identificadores únicos para as tarefas.
- Armazenar dados localmente em formato JSON.
- Recuperar tarefas salvas ao iniciar a aplicação.

## Tecnologias utilizadas

- Python 3
- JSON
- Pytest
- Git
- GitHub

## Estrutura do projeto

```text
task-manager/
│
├── main.py
├── task_manager.py
├── storage.py
│
├── data/
│   └── tasks.json
│
├── tests/
│   └── test_task_manager.py
│
├── README.md
└── .gitignore
```

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd task-manager
```

### 3. Instale as dependências

```bash
pip install pytest
```

### 4. Execute a aplicação

```bash
python main.py
```

## Executando os testes

Para executar os testes automatizados:

```bash
python -m pytest -v
```

## Aprendizados

Durante o desenvolvimento deste projeto, foram trabalhados conceitos como:

- Funções e estruturas de controle.
- Listas e dicionários.
- Modularização e separação de responsabilidades.
- Manipulação de arquivos JSON.
- Persistência de dados.
- Tratamento de exceções.
- Testes automatizados com Pytest.
- Organização de projetos Python.

---

Desenvolvido por **Murilo Wiroski Oliveira**.
