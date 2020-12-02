numeroIntroducido = (input("introduzca numeros separados por coma: "))
numeros = numeroIntroducido.split(",")
numero_de_usuario_limpios = []

for numero in numeros:
    numero_de_usuario_limpios.append(int(numero))


numeroMax = numeros[0]
numeroMin = numeros[0]

for numero in numeros[1:]:
    if numeroMin > numero:
        numeroMin = numero

    if numeroMax < numero:
        numeroMax = numero

print("Numero grande: {}, Numero pequeño: {}".format(numeroMax, numeroMin))