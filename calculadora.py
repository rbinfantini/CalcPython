import math

# Operacoes basicas

def soma(a, b):
    return a+ b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b== 0:
        raise ValueError("ERRO: Divisão por zero não existe.")
    return a / b

# Potencia e raiz

def potencia(base, exp):
    return math.pow(base, exp)


def raiz_quadrada(n):
    if n < 0:
        raise ValueError("ERRO: raiz quadrada de número negativo não existe.")
    return math.sqrt(n)
