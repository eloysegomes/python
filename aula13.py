#13-rent-car.py = escreva um programa que pergunte a quantidade de km
#percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado,
# calcule o preço a pagar, sabendo que o
# carr cuta R$ 60 por dia e R$ 0,15 por km rodado

#variaveis
km_percorridos = float(input("Digite a quantidade de Km percorridos: "))

dias_alugados = int(input("Digite a quantidade de dias alugados: "))

preco_por_dia = 60.00
preco_por_km = 0.15

custo_dias = dias_alugados * preco_por_dia
custo_km = km_percorridos * preco_por_km
custo_total = custo_dias + custo_km

print(f"O total a pagar pelo aluguel do carro é: R$ {custo_total:.2f}")
