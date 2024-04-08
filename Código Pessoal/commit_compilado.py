# Declaração de Dicionários
nomes_dict = {
    1: 'Leonardo', 
    2: 'Pablo', 
    3: 'Pedro', 
    4: 'Ruan', 
    5: 'Thales'
}  

def print_team_members():
    print("-------------------")
    print("Integrantes da T.I:")
    print("-------------------")
    for key, value in nomes_dict.items():
        print(f"    {key} - {value}")

def compile_commit():
    num_task_input = input("Insira quantas tarefas são: ")

    mensagem_personalizada = ""  # Inicializa a mensagem personalizada aqui
    for _ in range(int(num_task_input)):
        task_number = input("Insira o número da tarefa: ")
        at_input_alias = int(input(f"Insira o número do responsável pela tarefa {task_number}: "))
        if at_input_alias not in nomes_dict:
            print("Número inválido. Por favor, escolha um número válido.")
            continue
        at_input = nomes_dict[at_input_alias]
        # Adiciona cada nova tarefa à mensagem personalizada
        mensagem_personalizada += f"#{task_number} - @{at_input}\n"

    # Seleção do status da mensagem compilada
    print("\nSelecione o status da mensagem compilada:")
    print("1 - Merge Cancelado")
    print("2 - Merge Homolog")
    print("3 - Subida Produção")
    status_input = input("Digite o número correspondente ao status desejado: ")

    if status_input == '1':
        mensagem_personalizada += "\nForam rejeitadas \nor favor resolva os conflitos referentes a suas respectivas tarefas e informe."
    elif status_input == '2':
        mensagem_personalizada += "\nForam mergeadas no homolog, por favor realize os testes necessários e informe.\nAtualizem as Branches de trabalho."
    elif status_input == '3':
        mensagem_personalizada += "\nForam subidas para a produção.\nRealizem os testes necessários e informem."
    else:
        print("Opção inválida.")
        return None

    return "As Tasks:\n" + mensagem_personalizada  # Adiciona "as tarefas:" antes da lista de tarefas

if __name__ == "__main__":
    message = compile_commit()
    if message:
        print(message)
    else:
        print("Erro ao compilar a mensagem.")
