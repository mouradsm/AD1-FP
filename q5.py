import random

#  Utilizada para criar uma copia auxiliar de uma matriz
#  sem usar as referências dos objetos existentes
from copy import deepcopy

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

#### SOMA ###############
def somaMatrizes(m1, m2):
    if not comparaMatrizes(m1, m2):
        return None

    aux = deepcopy(m1)
    l = len(aux)
    c = len(aux[0])

    for i in range(l):
        for j in range(c):
            aux[i][j] = m1[i][j] + m2[i][j]
    return aux
#########################
# Verifica se as matrizes tem o mesmo tamanho
def comparaMatrizes(m1, m2):
    if len(m1) > len(m2) or len(m2) > len(m1) or \
                    len(m1[0]) > len(m2[0]) or len(m2[0]) > len(m1[0]):
        return False
    else:
        return True


#### MULTIPLICAÇÃO #####
def multiplicaMatrizes(m1, m2):

    if not comparaMatrizes(m1, m2):
        return None

    aux = deepcopy(m1)
    linhas = len(aux)
    colunas = len(aux[0])


    for i in range(linhas):
        for j in range(colunas):
            val = 0
            for k in range(len(m2)):
                val += matriz1[i][k] * m2[k][j]
            aux[i][j] = val
    return aux
#########################

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

print('')

multi = multiplicaMatrizes(matriz1, matriz2)

if (multi == None):
    print('Não é possível multiplicar matrizes se a quantidade de colunas da primeira é diferente da quantidade de linhas da segunda')
else:
    imprimeMatriz(multi)

