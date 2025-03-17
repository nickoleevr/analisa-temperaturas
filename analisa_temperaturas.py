def Executa():
    dados()


def dados():
    dados = []

    for _ in range(12):
        mes = int(input("Informe o número do mês: "))
        while mes < 1 or mes > 12:
            print("Mês inválido, informe um número de 1 a 12.")
            mes = int(input("Informe o número do mês (1 a 12): "))

        temperatura = float(input("Informe a temperatura (-60 a 50°C): ").replace(',', '.'))
        while temperatura < -60 or temperatura > 50:
            print("Temperatura inválida, informe um valor entre -60°C e 50°C.")
            temperatura = float(input("Informe a temperatura (-60 a 50°C): ").replace(',', '.'))

        dados.append((mes, temperatura))
    calcula_dados(dados)


def calcula_dados(dados):
   if dados:

        meses = {
            1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
            5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
            9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
        }

        temperaturas = [temperatura for _, temperatura in dados]
        media_maxima = round(sum(temperaturas) / len(temperaturas), 2)
        meses_temp_maxima =  len([temp for temp in temperaturas if temp > 33])


        maior_temperatura = max(temperaturas)
        menor_temperatura = min(temperaturas)
        mes_mais_quente = None
        mes_mais_frio = None

        for mes, temperatura in dados:
            if temperatura == maior_temperatura:
                mes_mais_quente = mes
            if temperatura == menor_temperatura:
                mes_mais_frio = mes

        retorna_dados(media_maxima, meses_temp_maxima,meses[mes_mais_quente],meses[mes_mais_frio])



def retorna_dados(media_maxima, meses_temp_maxima,mes_mais_quente,mes_mais_frio):

    print("\nResumo das Informações Registradas: \n")
    print(f"A temperatura média máxima do ano é: {media_maxima}°C")
    print(f"O Número de meses com temperatura superior a 33°C: {meses_temp_maxima}")
    print(f"O mês com maior temperatura: {mes_mais_quente}")
    print(f"O mês com menor temperatura: {mes_mais_frio}")

Executa()