
from storage import salvar_tarefas


def cadastrar_tarefa(tarefas):

    titulo = input("\nDigite o título da tarefa: ").strip()

    while not titulo:
        print("\nO título não pode ficar vazio.")
        titulo = input("Digite o título da tarefa: ").strip()

    descricao = input("Digite a descrição da tarefa: ")

    maior_id = 0

    for tarefa_existente in tarefas:
        if tarefa_existente["id"] > maior_id:
            maior_id = tarefa_existente["id"]

    novo_id = maior_id + 1

    tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": False
    }

    tarefas.append(tarefa)

    salvar_tarefas(tarefas)

    print("\nTarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n========== SUAS TAREFAS ==========")

    for tarefa in tarefas:

        if tarefa["concluida"]:
            status = "Concluída"
        else:
            status = "Pendente"

        print(f"\nID: {tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Status: {status}")


def concluir_tarefa(tarefas):

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas)

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa que deseja concluir: "))
    except ValueError:
        print("\nDigite apenas números.")
        return

    for tarefa in tarefas:

        if tarefa["id"] == id_tarefa:

            if tarefa["concluida"]:
                print("\nEssa tarefa já está concluída.")
                return

            tarefa["concluida"] = True

            salvar_tarefas(tarefas)

            print("\nTarefa concluída com sucesso!")
            return

    print("\nTarefa não encontrada.")


def excluir_tarefa(tarefas):

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    listar_tarefas(tarefas)

    try:
        id_tarefa = int(input("\nDigite o ID da tarefa que deseja excluir: "))
    except ValueError:
        print("\nDigite apenas números.")
        return

    for tarefa in tarefas:

        if tarefa["id"] == id_tarefa:

            tarefas.remove(tarefa)

            salvar_tarefas(tarefas)

            print("\nTarefa excluída com sucesso!")
            return

    print("\nTarefa não encontrada.")
