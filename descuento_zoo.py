
edad = int(input("digame su edad: "))
tipo_de_carnet = input("digame su tipo de carnet (E para Estudiante / P para Pensionista / F para familia numerosa / "
                       "N nada)")
if (25 <= edad <= 35 and tipo_de_carnet == "E") or\
        edad < 10 or \
        (edad > 65 and tipo_de_carnet == "P") or \
        (tipo_de_carnet == "F"):
    print("se te aplica el descuento ")
else:
    print("no se te aplica el descuento")


