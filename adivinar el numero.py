import random



numero = random.randint(1,10)

numero_elegido = int(input("elige un numero: "))

if numero_elegido == numero:
    print("has ganado! ")

if numero_elegido > 10:
    print("te has pasado un poco, di un numero entre 1 y 10 ")

if numero_elegido < 1:
    print("te has quedado corto ")

print("el numero ganador era: {}".format(numero))