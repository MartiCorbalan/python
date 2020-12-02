
numero = int(input("Introduzca un numero: "))

for n in range(1, 11):
    if n % 2 == 0:
        print("{} * {} = {}".format(n, numero, n * numero))