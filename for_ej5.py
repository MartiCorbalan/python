
numeros = []

numeroIntroducido = int(input("introduzca un numero en la lista "))
numeros.append(numeroIntroducido)


while input("Desea introduzir mas numeros? [S/N]") == "S":

    numeroIntroducido = int(input("introduzca un numero en la lista "))
    numeros.append(numeroIntroducido)

print(numeros)
