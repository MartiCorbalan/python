
titulo="Bienvenido al test sobre queso"
print("\n" + titulo + "\n" + "-" * len(titulo)+"\n")

puntuacion = 0

opcion=input("Pregunta 1: Que haces quando ves una tabla de quesos?\n"
             " A - Salgo corriendo\n"
             " B - pruebo uno de los quesos o incluso varios\n"
             " C - No puedo evitar devorarla\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("las opciones posibles son A, B y C")
    exit()

opcion=input("Pregunta 2: Como te gusta la hamburguesa?\n"
             " A - Sin queso\n"
             " B - Con queso\n"
             " C - Pan y queso\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("las opciones posibles son A, B y C")
    exit()


opcion=input("Pregunta 3: Eres intolerante a la lactosa?\n"
             " A - Si\n"
             " B - A veces\n"
             " C - NO\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("las opciones posibles son A, B y C")
    exit()


if puntuacion >= 25:
    print("resultado: felicidades, eres fanatico de los quesos")
elif puntuacion >= 15:
    print("resultado: felicidades, eres una persona que le gusta el queso")
else:
    print("resultado: no te gusta el queso")


print("puntuacion total: "+puntuacion)