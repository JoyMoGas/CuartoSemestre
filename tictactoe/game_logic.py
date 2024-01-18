'''
    Lógica del programa del gato
'''

tablero = [x for x in range(0,9)]
tab_dict = {x: str(x) for x in tablero}

def display_tablero(tablero: dict):
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("----------")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("----------")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

display_tablero(tablero)
