import random

#hecho por Martí Corbalan, estoy intentando aprender python ya que java se me da muy mal :(

print("Bienvenido a mi juego \n"
      "Estas en una nave espacial y has tenido un accidente,\n"
      " debes recoger una herramienta para poder reparar la nave\n"
      "Pero cuidado!, un alienigena se ha colado en la nave\n"
      "si te lo encuentras le puedes meter hasta dejarlo cao y reparar la nave\n"
      "o llevartelo para casita en cuanto este reparada la nave "
      "para reparar la nave a parte de la herramienta tienes que solucionar una operacion matematica")

opcio = input("Tienes dos opciones, A (ir a buscar la herramienta)  o B (intentar recuperar la comunicación)\n")
if opcio == "A":
    print("te has empezado a mover por la nave!")
    opcio = input("Entras en la habitacion principal, te has encontrado la herramienta,\n "
                  "(A) para coger\n "
                  "(B) seguir para buscar al alien y meterle de ostias")
    if opcio == "A":
        herramienta = False
        print("has cogido la herramienta, dirigete al taller para reparar la nave y fugarte")
        opcio = input("(A) ir al taller o (B) seguir buscando ayuda ")
        if opcio == "A":
            opcio = input("estas en el taller, quieres reparar la nave? (S) si (N) no")
            herramienta = True
            if opcio == "S":
                numero = random.randint(1, 50)
                print("has reparado la nave, ya puedes fugarte y te llevas un alien contigo, "
                      "esperemos que no tenga coronavirus, resuelve la suma y te podras ir, 10 * {}.".format(numero))
                opcio = int(input("cual es la respuesta? "))
            if opcio == 10 * numero:
                print("has hacertado, te vas a casa")

            if opcio == "N":
                print("no has reparado la nave, vas a morir ")
        if opcio == "B":
            print("no has cogido la herramienta")
    if opcio == "B":
        print("te has encontrado con el alien, cuidado")
        opcio = input("intentar correr (A) o meterle de ostias (B)")
        if opcio == "A":
            print("has salido corriendo pero no te ha servido de nada, lo siento ")
        elif opcio == "B":
            print("te has intentado pegar con un maldito alien, eres un maldito loco,\n "
                  "has muerto por bobo y no querer andar un poco para buscar la herramienta ")
if opcio == "B":
    print("estas intentando recuperar la comunicacion pero esta muy estropeada,"
          "sigue intentando o busca la herraminta. ")







