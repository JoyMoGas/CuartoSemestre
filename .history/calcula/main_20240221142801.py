'''
Calcula datos estadísticos de una lista, usando
argumentos
'''
import argparse
import calcula

def main(listado: list, operacion: str):
    operacion = operacion.lower()
    if operacion == "suma":
        print(f"Suma:{calcula.suma(listado)}")
    if operacion == "promedio":
        print(f"Promedio:{calcula.promedio(listado)}")
    if operacion == "moda":
        print(f"Moda:{calcula.moda(listado)}")
    if operacion == "todas":
        print(f"Suma:{calcula.suma(listado)}")
        print(f"Promedio:{calcula.promedio(listado)}")
        print(f"Moda:{calcula.moda(listado)}")

if __name__ == "__main__":
    # declaramos nuestro "parser" o procesador de argumentos
    parser = argparse.ArgumentParser(description="Calcula datos estadísticos")
    parser.add_argument("numeros", metavar="N", type=int, nargs="+", help="")
    parser.add_argument("--operacion", "-o", dest="o", type=str, choices=["suma", "promedio", "moda", "todas"])

    args = parser.parse_args()
    print(args.numeros)
    print(args.o)
    main(args.numeros, args.o)

s