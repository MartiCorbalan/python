from random import randint
import os

print("Bienvenido al combate pokemon entre Pikachu y Squirtle")

VIDA_INICIALPIKACHU = 80
VIDA_INICIALSQUIRTLE = 90

vida_pikachu = VIDA_INICIALPIKACHU
vida_Squirtle = VIDA_INICIALSQUIRTLE

TAMANIO_BARRA_DE_VIDA =20


while vida_pikachu >0 and vida_Squirtle>0:


    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con bola voltio")
        vida_Squirtle -= 10
    else:
        print("Pikachu ataca con Onda trueno")
        vida_Squirtle -= 11

    if  vida_pikachu < 0:
        vida_pikachu =0

    if vida_Squirtle < 0:
        vida_Squirtle = 0


    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_DE_VIDA / VIDA_INICIALPIKACHU)
    print("Pikachu:    [{}{}]".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_DE_VIDA - barras_de_vida_pikachu)),
                                    vida_pikachu, VIDA_INICIALPIKACHU)

    barras_de_vida_squirtle = int(vida_pikachu * TAMANIO_BARRA_DE_VIDA / VIDA_INICIALSQUIRTLE)
    print("Squirtle:   [{}{}]".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_DE_VIDA - barras_de_vida_squirtle)),
                                    vida_Squirtle, VIDA_INICIALSQUIRTLE)


    input("ENTER para continuar...\n\n")
    os.system("cls")
    print("Turno Squirtle")

    ataque_Squirtle = None
    while ataque_Squirtle not in ["P", "A", "B"]:

        ataque_Squirtle = input("que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja: ")

    if ataque_Squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif vida_Squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_Squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_Squirtle < 0:
        vida_Squirtle = 0

    barras_de_vida_pikachu = int(vida_pikachu * TAMANIO_BARRA_DE_VIDA / VIDA_INICIALPIKACHU)
    print("Pikachu:    [{}{}]".format("*" * barras_de_vida_pikachu, " " * (TAMANIO_BARRA_DE_VIDA - barras_de_vida_pikachu)),
                                      vida_pikachu, VIDA_INICIALPIKACHU)

    barras_de_vida_squirtle = int(vida_pikachu * TAMANIO_BARRA_DE_VIDA / VIDA_INICIALSQUIRTLE)
    print("Squirtle:   [{}{}]".format("*" * barras_de_vida_squirtle, " " * (TAMANIO_BARRA_DE_VIDA - barras_de_vida_squirtle)),
          vida_Squirtle, VIDA_INICIALSQUIRTLE)

    input("ENTER para continuar...\n\n")
    os.system("cls")

if vida_pikachu > vida_Squirtle:
    print("Pikachu gana")
else:
    print("Squirtle gana")