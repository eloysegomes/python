# pede 5 números pro usuário
def solicita_numeros():
    numeros = []
    for i in range(5):
        num = int(input(f"Digite o número {i+1}: "))
        numeros.append(num)
    return numeros

#  mostra o maior, menor e a soma dos números
def analisa_lista(numeros):
    maior = max(numeros)
    menor = min(numeros)
    soma = sum(numeros)
    
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Soma dos números: {soma}")

# programa principal
numeros = solicita_numeros()
analisa_lista(numeros)