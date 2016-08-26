import random

L = int(input("Informe o valor inteiro mínimo da faixa: "))
H = int(input("Informe o valor inteiro máximo da faixa: "))

l1 = int(input("Informe a quantidade de linhas da primeira matriz: "))
c1 = int(input("Informe a quantidade de colunas da primeira matriz: "))

l2 = int(input("Informe a quantidade de linhas da segunda matriz: "))
c2 = int(input("Informe a quantidade de colunas da segunda matriz: "))


def criaMatriz(linhas, colunas, minimo, maximo):
    matriz = []
    for i in range(0, linhas):
        linha = []
        for j in range(0, colunas):
            linha.append(random.randint(minimo, maximo))
        matriz.append(linha)
    return matriz


def imprimeMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end='\t')
        print('')


def somaMatrizes(matriz1, matriz2):
    if len(matriz1) > len(matriz2) or len(matriz2) > len(matriz1) or len(matriz1[0]) > len(matriz2[0]) or len(
            matriz2[0]) > len(matriz1[0]):
        return None

    aux = matriz1
    l = len(aux)
    c = len(aux[0])

    for i in range(l):
        for j in range(c):
            aux[i][j] = matriz1[i][j] + matriz2[i][j]
    return aux


# TODO: Implementar função de multiplicação de matrizes
def multiplicaMatrizes(matriz1, matriz2):
    return 'Não implementado'


matriz1 = criaMatriz(l1, c1, L, H)
matriz2 = criaMatriz(l2, c2, L, H)

imprimeMatriz(matriz1)
print('')  # Linha em branco
imprimeMatriz(matriz2)

soma = somaMatrizes(matriz1, matriz2)

print('')
if (soma == None):
    print('Não é possivel somar matrizes de dimensões diferentes')
else:
    imprimeMatriz(soma)
