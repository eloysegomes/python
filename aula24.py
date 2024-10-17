# Eloyse Gomes 2C

# Solicita ao usuário um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada do número fornecido
print(f"Tabuada do {numero}:")
for i in range(1, 11):  # de 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")