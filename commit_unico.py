# Declaração de Dicionários
nomes_dict = {
    1: 'Leonardo', 
    2: 'Pablo', 
    3: 'Pedro', 
    4: 'Ruan', 
    5: 'Thales'
}  

def execute_message_sender():
    respostas_dict = {
        1: " - A Tarefa teve o Merge Rejeitado.\nPor favor, resolva os problemas referentes a sua tarefa.",
        2: " - Está sendo revisado.",
        3: " - Foi mergeada para o Homolog.\nAtualizem as Branches de Trabalho :)",
        4: " - Está precisando de Teste no Homolog.",
        5: " - Está na fila para subida.",
        6: " - Foi subida para a produção.\nExecute os testes necessários.",
    }

    # Mensagem final
    final_message = ""

    while True:
        try:
            # Captura de entrada do usuário
            print("Bem vindo ao Message Sender (V.0.0.1)")
            print("-------------------")
            num_task_input = input("Insira o número da Task: ")

            print("-------------------")
            print("Integrantes da T.I:")
            print("-------------------")
            for key, value in nomes_dict.items():
                print(f"    {key} - {value}")

            # Solicita o usuário a escolher um número para o Nome da Pessoa '@'
            print("-------------------")
            at_input_alias = int(input("Escolha um número para o Nome da Pessoa: "))

            # Verifica se o número está entre as opções disponíveis
            if at_input_alias not in nomes_dict:
                print("Número inválido. Por favor, escolha um número válido.")
                continue

            at_input = nomes_dict[at_input_alias]

            # Apresenta as opções de mensagens
            print("-------------------")
            print("\nSelecione a mensagem (1 - 6):")
            print("-------------------")
            for key, value in respostas_dict.items():
                print(f"    {key} - {value}")

            # Solicita o usuário a escolher um número para a mensagem
            print("-------------------")        
            mensagem_alias = int(input("Digite o número correspondente à mensagem desejada: "))

            # Verifica se o número está entre as opções disponíveis
            if mensagem_alias not in respostas_dict:
                print("Número inválido. Por favor, escolha um número de mensagem válido.")
                continue

            resultado_mensagem = respostas_dict[mensagem_alias]

            # Constrói a mensagem
            final_message = f"\n\n==============================\nTask #{num_task_input} - @{at_input}{resultado_mensagem}\n=============================="
            print(final_message)

            # Retorna a mensagem final
            return final_message

        except ValueError:
            # Mensagem de entrada inválida
            print("Entrada inválida. Por favor, digite um número inteiro.")
