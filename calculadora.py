# -Tratamento de erro
from utils import ler_numero, calcular, limpar_tela

while True:
    num1 = ler_numero("Digite o primero número: ")
    op = str(input("Digite o operador (+, -, /, *): ")).strip()
    num2 = ler_numero("Digite o segundo número: ")
    resultado = calcular(num1, num2, op)
    
    print(f"{num1} {op} {num2} = {resultado}")
    
    opcao = input("Deseja continuar? [s/n]: ").lower()[0:1]
    if opcao != "s":
        break
    limpar_tela()