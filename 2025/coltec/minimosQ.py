import numpy as np
import matplotlib.pyplot as plt

X = 0
Y = 1

def calculaMediaX(num, pontos):
    i = 0
    soma = 0.0
    
    for i in range(num):
        soma += pontos[i][0]
    return soma / (i + 1)
    
def calculaMediaY(num, pontos):
    i = 0
    soma = 0.0
    
    for i in range(num):
        soma += pontos[i][1]
    return soma / (i + 1)
    
def calculaSxy(num, pontos, mediaX, mediaY):
    soma = 0.0
    i = 0
    
    for i in range(num):
        soma += (pontos[i][0] - mediaX) * (pontos[i][1] - mediaY)
    return soma

def calculaSxx(num, pontos, mediaX):
    soma = 0.0
    i = 0
    
    for i in range(num):
        soma += (pontos[i][0] - mediaX) * (pontos[i][0] - mediaX)
    return soma
    

def main():
    num = int(input("Digite a quantidade de pontos: "))
    pontos = np.zeros((num, 2))
    
    for i in range(num):
        pontos[i][X] = float(input("X %i: "% (i + 1)))
        pontos[i][Y] = float(input("Y %i: "% (i + 1)))
        plt.plot(pontos[i][X], pontos[i][Y], 'o', color = 'blue')

    mediaX = calculaMediaX(num, pontos)
    mediaY = calculaMediaY(num, pontos)
    Sxy = calculaSxy(num, pontos, mediaX, mediaY)
    Sxx = calculaSxx(num, pontos, mediaX)
    
    a = Sxy / Sxx
    b = mediaY - (mediaX * a)
    
    plt.plot([pontos[0][X], pontos[num - 1][X]], [(pontos[0][X] * a + b), (pontos[num - 1][X] * a + b)], color = 'black', linestyle = 'solid')
    plt.grid()
    plt.show()

    print(mediaX, mediaY, Sxy, Sxx)
    
       

main()
