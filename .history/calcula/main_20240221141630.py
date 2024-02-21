'''
Calcula datos estadísticos de una lista, usando
argumentos
'''
import argparse
import calcula

def main(listado: list):
    print(f"Suma:{calcula.suma(listado)}")
    print(f"Promedio:{calcula.promedio(listado)}")
    print(f"Moda:{calcula.moda(listado)}")

if __name__ == "__main__":
    # declaramos nuestro "parser" o procesador de argumentos
    parser = argparse.ArgumentParser(description="Calcula datos estadísticos")
    parser.add_argument("numeros", metavar="N", type=int, nargs="+", help="")
    parser.add_argument(dest="o", type=str)

    args = parser.parse_args()
    print(args.numeros)
    print(args.s)
    main(args.numeros)

