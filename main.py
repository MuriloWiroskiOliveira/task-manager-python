
from task_manager import (
    cadastrar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    excluir_tarefa
)

from storage import carregar_tarefas


def main():

    tarefas = carregar_tarefas()

    while True:

        print("==============================")
        print("       TASK MANAGER")
        print("==============================")

        print("\n1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            excluir_tarefa(tarefas)

        elif opcao == "5":
            print("\nEncerrando o Task Manager...")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
