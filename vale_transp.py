def calcular_vale_transporte():

    # Passo 1: Insira a quantidade de dias de viagem
    dias_viagem = int(input("Digite a quantidade de dias de viagem: "))

    # Valores padrão das viagens
    valor_primeira_viagem = 5.90
    valor_segunda_viagem = 5.50

    # Passo 4: Retorne o valor total da primeira viagem
    valor_total_primeira_viagem = valor_primeira_viagem * 2 * dias_viagem
    print("O valor total do VT (PND - TRE) é:", valor_total_primeira_viagem)

    # Passo 5: Retorne o valor total da segunda viagem
    valor_total_segunda_viagem = valor_segunda_viagem * 2 * dias_viagem
    print("O valor total do VT (PND - PND) é:", valor_total_segunda_viagem)

    # Passo 6: Retorne o valor total de tudo
    valor_total = valor_total_primeira_viagem + valor_total_segunda_viagem
    print("O valor total é:", valor_total)

calcular_vale_transporte()

# ------------------------------------------------------------------


