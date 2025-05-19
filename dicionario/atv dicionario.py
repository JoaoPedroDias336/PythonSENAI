perfum = {
    "Marca": "Jean Paul Gaultier",
    "Modelo": "Elixir",
    "Quantidade(ml)": "75ml-125ml",
    "Valor(R$)":520
}

#print(perfum)

perfum2 = {
    "Marca": "Chanel",
    "Modelo": "Bleu de Chanel",
    "Quantidade(ml)": "50ml-150ml",
    "Valor(R$)": 1.265
}

#print(perfum)

perfum3 = {
    "Marca": "Lattafa",
    "Modelo": "khamrah",
    "Quantidade(ml)": "100ml",
    "Valor(R$)": 255
}

#print(perfum)

#exibir uma lista de dicionarios
lista_marca = [perfum, perfum2, perfum3]    
    #escolhando os campos

    
    #exibindo todos
for marca in lista_marca:
    for chave, valor in marca.items():
        print(f"{chave}: {valor}")
        