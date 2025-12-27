# 1- parte
num1 = float(input("Digite o primero número: "))
operador = str(input("Digite o operador (+, -, /, *): "))
num2 = float(input("Digite o segundo número: "))

# operações

# Adição:
if operador == "+":
    resultado = num1 + num2
    print(f"{num1:.0f} {operador} {num2:.0f} = {resultado:.0f}")
    
# Subtração:
elif operador == "-":
    resultado = num1 - num2
    print(f"{num1:.0f} {operador} {num2:.0f} = {resultado:.0f}")
    
# Divisão:
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1:.0f} {operador} {num2:.0f} = {resultado:.0f}")
    else:
        print("\033[1;31mERRO:\033[m Não é possível dividir por zero!")

# Multiplicação: 
elif operador == "*":
    resultado = num1 * num2
    print(f"{num1:.0f} {operador} {num2:.0f} = {resultado:.0f}")
    
# nenhuma da opções 
else:
    print("\033[1;31mOperador inválido! Tente novamente\033[m")
    