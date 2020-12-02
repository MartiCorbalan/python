
dolar_euro = 0.91
libra_euro = 1.18

opcion = input("Que desea hacer? "
               "A- convertir de dolar a euro\n"
               "B- convertir de euro a dolar\n"
               "C- convertir de libra a euro\n"
               "D- convertir de euro a libra\n")

texto_usuario = " introduzca la cantidad de {} a convertir: "
if opcion == "A":
    cantidad_de_dinero = float(input(texto_usuario.format("dolares")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * dolar_euro))
elif opcion == "B":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en dolares es: {}".format(cantidad_de_dinero / dolar_euro))
elif opcion == "C":
    cantidad_de_dinero = float(input(texto_usuario.format("libras")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero * libra_euro))

elif opcion == "D":
    cantidad_de_dinero = float(input(texto_usuario.format("euros")))
    print("La cantidad en euros es: {}".format(cantidad_de_dinero / libra_euro))

else:
    print("no has elegido una opcion valida")