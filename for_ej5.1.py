



numeroIntroducido = (input("introduzca numeros separados por coma: "))
numeros = numeroIntroducido.split(",")
numero_de_usuario_limpios = []

for numero in numeros:
    numero_de_usuario_limpios.append(int(numero))

print(numero_de_usuario_limpios)