# Elaborar um algoritmo que solicita 4 notas de usuário.
# o progama deve calcular a média a
# verificafr essa a média é maio ou igual a 80.
# se a média for maior ou igual a 80, o programa
# deve exibir a mensagem "aprovado" e se a média for menor que 
# 80, o programa deve exibir a mensagem "reprovado".

nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média final obtida = {media}") 

if (media >= 80):
  print ("aprovado")
else:
  print("reprovado")