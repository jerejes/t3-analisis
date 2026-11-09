import math
import random


def generar_punto(a, b):
    return random.uniform(-a, a), random.uniform(-b, b)


def calcular_elipse(x, y, a, b):
    return (x ** 2 / a ** 2) + (y ** 2 / b ** 2) <= 1


def calcular_hiperbola(x, y, c, d):
    return (x ** 2 / c ** 2) - (y ** 2 / d ** 2) >= 1


def leer_dato(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("Ingrese un valor mayor que cero.")
        except ValueError:
            print("Dato incorrecto, vuelva a ingresar.")


def main():
    print("=== AREA DE INTERSECCION POR MONTECARLO ===")

    print("\nIngrese los datos de la elipse:")
    a = leer_dato("Valor de a (semieje horizontal): ")
    b = leer_dato("Valor de b (semieje vertical): ")

    print("\nIngrese los datos de la hiperbola:")
    c = leer_dato("Valor de c: ")
    d = leer_dato("Valor de d: ")

    n = int(leer_dato("\nCantidad de puntos aleatorios a generar: "))

    contador_elipse = 0
    contador_interseccion = 0

    for i in range(n):
        x, y = generar_punto(a, b)

        if calcular_elipse(x, y, a, b):
            contador_elipse += 1

            if calcular_hiperbola(x, y, c, d):
                contador_interseccion += 1

    area_elipse = math.pi * a * b

    if contador_elipse > 0:
        area_interseccion = area_elipse * contador_interseccion / contador_elipse
    else:
        area_interseccion = 0

    print("\n--- RESULTADOS ---")
    print(f"Puntos generados: {n}")
    print(f"Puntos dentro de la elipse: {contador_elipse}")
    print(f"Puntos de interseccion: {contador_interseccion}")
    print(f"Area de la elipse: {area_elipse:.4f}")
    print(f"Area aproximada de interseccion: {area_interseccion:.4f}")


if __name__ == "__main__":
    main()
