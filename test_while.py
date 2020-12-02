
respuesta = None

while respuesta != "A" and respuesta != "B" and respuesta != "C":
     respuesta = input("que opcion prefieres [A, B, C]?\n ")

if respuesta=="A":
    print("has elegido bien")
elif respuesta == "B":
    print("podrias haber elegido mejor")
elif respuesta == "C":
    print("elegiste mal")
else:
    print("no me has dado una respues con sentido")