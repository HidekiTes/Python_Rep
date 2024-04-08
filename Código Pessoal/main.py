from commit_unico import execute_message_sender as commit_unico
from commit_compilado import compile_commit as commit_compilado

# Importa as bibliotecas necessárias do Selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    print("Bem-vindo ao Message Sender (V.0.0.1)")
    print("Escolha a opção desejada:")
    print("1 - Commit único")
    print("2 - Commit compilado")

    # Solicita ao usuário para escolher a opção desejada
    opcao = input("Opção: ")

    if opcao == '1':
        final_message = commit_unico()
    elif opcao == '2':
        final_message = commit_compilado()
    # elif opcao == '3':
    #     print("Opção selecionada: Cálculo de Vale Transporte")
    #     # Coloque aqui o código anterior ao vale_transp() que deseja executar
    #     dias_viagem = int(input("Digite a quantidade de dias de viagem: "))
    #     valor_primeira_viagem = 5.90
    #     valor_segunda_viagem = 5.50
    #     valor_total_primeira_viagem = valor_primeira_viagem * 2 * dias_viagem
    #     valor_total_segunda_viagem = valor_segunda_viagem * 2 * dias_viagem
    #     valor_total = valor_total_primeira_viagem + valor_total_segunda_viagem
    #     final_message = f"O valor total do VT é: R${valor_total}"
    else:
        print("Opção inválida.")
        return

    # Configuração do navegador Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_service = webdriver.chrome.service.Service(executable='chromedriver')

    # Inicializa o navegador Chrome2
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    # Navega até a página
    browser.get('https://dontpad.com/obsidianhidekites')

    # Espera 2 segundos para garantir que a página tenha carregado completamente
    sleep(2)

    # Insere a mensagem final no campo de texto
    input_element = browser.find_element(By.ID, "text")
    input_element.send_keys(final_message)

    # Dorme por 15 segundos
    sleep(15)

    # Fecha o navegador
    browser.quit()

    print('Processo concluído com sucesso.')

if __name__ == "__main__":
    main()
