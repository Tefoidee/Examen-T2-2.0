def suma_posiciones(lista, PI, PF):
    if PI == PF:
        return lista[PI - 1]
    return lista[PI - 1] + suma_posiciones(lista, PI + 1, PF)


def obtener_lista():
    entrada = input("Ingresa los elementos de la lista separados por comas: ")
    return [int(x.strip()) for x in entrada.split(",")]


def obtener_posiciones(tamano):
    while True:
        PI = int(input(f"Ingresa la posición inicial PI (1 - {tamano}): "))
        PF = int(input(f"Ingresa la posición final   PF (1 - {tamano}): "))
        if 1 <= PI <= PF <= tamano:
            return PI, PF
        print("Error: Asegúrate de que 1 <= PI <= PF <= tamaño de la lista.")


def mostrar_resultado(lista, PI, PF, resultado):
    elementos = lista[PI - 1 : PF]
    print("\n" + "-" * 45)
    print(f"Lista          : {lista}")
    print(f"Posiciones     : PI={PI}, PF={PF}")
    print(f"Elementos      : {elementos}")
    print(f"Operación      : {' + '.join(map(str, elementos))} = {resultado}")
    print("-" * 45)


def main():

    lista = obtener_lista()
    print(f"Lista cargada  : {lista}  |  Tamaño: {len(lista)}")

    PI, PF = obtener_posiciones(len(lista))
    resultado = suma_posiciones(lista, PI, PF)

    mostrar_resultado(lista, PI, PF, resultado)


if __name__ == "__main__":
    main()