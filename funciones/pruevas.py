from time import sleep


def medir_largo(iterable, *args):
    if args:
        largos = [len(iterable)]
        for a in args:
          largos.append(len(a))
        return largos
    return len(iterable)


def main():
    #palabra de 4 letras
    print(medir_largo("hola"))
    #2 palabras de 4 letras y una de 5
    print(medir_largo("hola", "como", "estas"))


if __name__ == "__main__":
    main()
