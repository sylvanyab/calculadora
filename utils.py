
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("ERRO: Digite um número válido!")
            
def calcular(n1, n2, operador):
    if operador == "+":
        return n1 + n2
    elif operador == "-":
        return n1 - n2
    elif operador == "*":
        return n1 * n2
    elif operador == "/":
        return n1 / n2 if n2 != 0 else "Erro: divisão"
    else:
        return "Operação inválida"
    
def limpar_tela():
    print("\n" * 50)    