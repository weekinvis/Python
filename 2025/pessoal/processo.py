import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

grauPolinomio = 1

nome_arquivo = "resultados.dat"

def tratarDados(nome_arquivo, qntLinhas):
    # Abrir o arquivo .dat para leitura
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()  # Lê todas as linhas

    # Abrir o arquivo para escrita, sobrescrevendo o conteúdo
    with open(nome_arquivo, 'w') as arquivo:
        for numero_linha, linha in enumerate(linhas, start=1):
            # Encontrar todos os números na linha
            numeros = re.findall(r'\d+', linha)
            
            # Filtrar números maiores que 30, e manter o primeiro número (matrícula)
            numeros_filtrados = [num for num in numeros if (32 <= int(num) <= 90) or (int(num) > 4000)]  # Filtra números maiores que 30
            
            if len(numeros_filtrados) > 0:
                # Manter o primeiro número como número de matrícula
                resultado = ' '.join([numeros_filtrados[0]] + numeros_filtrados[1:]) + f" {2025 - int((numero_linha - 1) / 90)}"
                arquivo.write(resultado + '\n')  # Escrever no arquivo o resultado filtrado


with open(nome_arquivo, 'r') as fp:
    for qntLinhas, line in enumerate(fp):
        pass


tratarDados(nome_arquivo, qntLinhas)

colunas = ["Num Matricula", "Nota Final", "Ano"]
anosInseridos = [2022, 2023, 2024, 2025]

df_txt = pd.read_csv(nome_arquivo, sep=' ', names=colunas)
minMax = df_txt.groupby('Ano')['Nota Final'].agg(['min', 'max'])

coeficientesMedia = np.polyfit(df_txt["Ano"], df_txt["Nota Final"], grauPolinomio)
polinomioMedia = np.poly1d(coeficientesMedia)

coeficienteCorte = np.polyfit(anosInseridos,minMax['min'], grauPolinomio)
polinomioCorte = np.poly1d(coeficienteCorte)

coeficienteMax = np.polyfit(anosInseridos, minMax['max'], grauPolinomio)
polinomioMax = np.poly1d(coeficienteMax)

valoresX = np.linspace(df_txt["Ano"].min(), df_txt["Ano"].max() + 2, 50)
valoresYcorte = polinomioCorte(valoresX)
valoresYmedia = polinomioMedia(valoresX)
valoresYmax = polinomioMax(valoresX)

plt.figure('a')
plt.plot(valoresX, valoresYmedia, linestyle='solid', color='black', label='Nota media prevista')
plt.plot(valoresX, valoresYcorte, linestyle='-.', color='blue', label='Nota de corte prevista')
plt.plot(valoresX, valoresYmax, linestyle='-.', color='red', label='Nota maxima prevista')
plt.legend()
plt.plot(df_txt["Ano"], df_txt["Nota Final"], 'kx')
plt.xticks(np.arange(df_txt["Ano"].min() - 1, df_txt["Ano"].max() + 2, 1))
plt.grid(True)
plt.show()
