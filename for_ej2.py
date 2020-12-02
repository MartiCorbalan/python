import string

texto_usuario = input("Introduzca un texto: ")

letras_mayus = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayus += 1

print("Las mayusculas son: {}".format(letras_mayus))
