# ==> Manipulação de Vetores

import random

L = int(input("Informe o valor inteiro mínimo da faixa: "))
H = int(input("Informe o valor inteiro máximo da faixa: "))

N = int(input("Informe a quantidade de valores a serem sorteados: "))


# Função para criar um vetor
def criadorDeVetor(tamanhoVetor, minimo, maximo):
    vetor = [None] * N
    for i in range(0, tamanhoVetor):
        vetor[i] = random.randint(minimo, maximo)
    return vetor


# Função que busca valores mínimo e máximo não duplicados no vetor
def buscarMinMax(vetor):
    unicos = set(vetor) - buscaDuplicados(vetor)
    if len(unicos) == 0:
        return (None, None)

    minimo = min(unicos)
    maximo = max(unicos)
    return (minimo, maximo)


# Função para achar os valores duplicados dentro do vetor.
def buscaDuplicados(vetor):
    valor = set()
    valor_add = valor.add
    duplicados = set(x for x in vetor if x in valor or valor_add(x))

    return duplicados


# Cria um novo vetor utilizando a função de criação.
vetor = criadorDeVetor(N, L, H)

# Imprime um vetor criado
print(vetor)

# Imprime os maiores e menores não duplicados no vetor
print(buscarMinMax(vetor))
