lista_de_la_compra = []
input_de_usuario = None

print("Programa sobre mi lista de la compra\n")

while True:
    input_de_usuario = input("Que desea comprar ? (Q) para salir\n")
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in lista_de_la_compra:
        print("{} ya esta en la lista".format(input_de_usuario))
    else:
        if input("Seguro que quieres añadir {} a la lista de la compra? [S/N]".format(input_de_usuario))=="S":
            lista_de_la_compra.append(input_de_usuario)

print("la lista de la compra es: ")
print(lista_de_la_compra)
