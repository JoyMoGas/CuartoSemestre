def function(x, m, b):
    resultado = (m*x) + b
    return resultado

def main():
    x = float(input("Introduce el valor de x:"))
    m = 1.5
    b = 2
    print("El resultado es: ", function(x, m, b))
    X = [x for x in range(0,10)]
    Y = [function(x, m, b) for x in X]
    print(X)
    print(Y)
    coords = list(zip(X, Y))
    print(coords)

main()