objetos = ["lapis","celular","caneta","apontador","borracha"]

objetos.append("lapis")

print(objetos[1])

ob = objetos.remove("celular")
print(len(objetos))

for objeto in objetos:
    print(objeto)

if "cadeira" in "objetos":
    objetos.remove("cadeira")
else:
    objetos.append("cadeira")
        
print(objetos.sort())
print(objetos)

elemento1 = len(objetos)
elemento2 = objetos[0]
elemento3 = [elemento1 - 1]
print("primeiro",elemento2,"ultimo",elemento3)

objetos.clear()