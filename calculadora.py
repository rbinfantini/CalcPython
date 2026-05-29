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

# Interface

MENU = """
╔══════════════════════════════════╗
║      CALCULADORA CIENTÍFICA      ║
╠══════════════════════════════════╣
║  OPERAÇÕES BÁSICAS               ║
║   1. Soma                        ║
║   2. Subtração                   ║
║   3. Multiplicação               ║
║   4. Divisão                     ║
╠══════════════════════════════════╣
║  POTÊNCIA E RAIZ                 ║
║   5. Potência                    ║
║   6. Raiz Quadrada               ║
╠══════════════════════════════════╣
║  TRIGONOMETRIA                   ║
║   7. Seno                        ║
║   8. Cosseno                     ║
║   9. Tangente                    ║
╠══════════════════════════════════╣
║   0. Sair                        ║
╚══════════════════════════════════╝
"""

def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")

def executar_operacao(opcao):
    if opcao in ("1", "2", "3", "4", "5"):
        a = pedir_numero("Primeiro número: ")
        b = pedir_numero("Segundo número: ")
        operacoes = {
            "1": ("Soma", lambda: soma(a, b)),
            "2": ("Subtração", lambda: subtracao(a, b)),
            "3": ("Multiplicação", lambda: multiplicacao(a, b)),
            "4": ("Divisão", lambda: divisao(a, b)),
            "5": ("Potência", lambda: potencia(a, b)),
        }
        nome, fn = operacoes[opcao]
        resultado = fn()
        print(f"\n{nome}: {resultado}")

    elif opcao == "6":
        n = pedir_numero("Número: ")
        print(f"\nRaiz quadrada: {raiz_quadrada(n)}")

    elif opcao in ("7", "8", "9"):
        graus = pedir_numero("Ângulo em graus: ")
        operacoes = {
            "7": ("Seno", lambda: seno(graus)),
            "8": ("Cosseno", lambda: cosseno(graus)),
            "9": ("Tangente", lambda: tangente(graus)),
        }
        nome, fn = operacoes[opcao]
        print(f"\n{nome}: {fn()}")

    else:
        print("Opção inválida.")


def main():
    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Encerrando a calculadora. Até mais!")
            break

        try:
            executar_operacao(opcao)
        except ValueError as e:
            print(f"\n{e}")

        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()