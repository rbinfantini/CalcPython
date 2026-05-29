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

# Trigonometria

def seno(graus):
    return math.sin(math.radians(graus))


def cosseno(graus):
    return math.cos(math.radians(graus))


def tangente(graus):
    if graus % 180 == 90:
        raise ValueError("ERRO: tangente indefinida para esse ângulo.")
    return math.tan(math.radians(graus))