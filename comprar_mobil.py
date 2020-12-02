


opcion = input("iOS o Android? (I/A)\n")

if opcion == "A":
    opcion = input("tienes dinero? (S/N)")
    if opcion == "S":
        opcion = input("te importa la camara del movil? (S/N)")
        if opcion == "S":
            opcion = input("google pixel supercamara")
        if opcion == "N":
            opcion = input("android calidad-precio")
    if opcion == "N":
        opcion = input("android chino de 100€ ")


elif opcion == "I":
    opcion = input("tienes dinero (S/N)")
    if opcion == "S":
        opcion = input("iphone ultra pro max")
    if opcion == "N":
        opcion = input("iphone segunda mano")
