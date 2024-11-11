# balada do dudu
# pergunta a idade da pessoa
idade = int(input("Digite a sua idade: "))

# se idade >= 18
if idade >= 18:
    print("Autorizado")

# se idade >= 16 pergunta sobre autorização dos pais
elif idade >= 16:
    autorizacao_pais = input("Você tem autorização dos pais? (sim/não): ").lower()
    
    if autorizacao_pais == "sim":
        print("Autorizado")
    else:
        print("Não autorizado")

# idade < que 16
else:
    print("Não autorizado")