import matplotlib
import modulo_linea

def main():
    x, m, b = [1, 2, 3], 1.5, 2.0
    coordenadas = modulo_linea.linea(x, b, b)
    print(coordenadas)

if __name__ == "__main__":
    main()