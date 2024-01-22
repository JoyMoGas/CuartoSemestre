'''
    Lógica del programa del gato
'''

import random


tablero = [x for x in range(0,9)]
tab_dict = {x: str(x) for x in tablero}

def display_tablero(tablero: dict):
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("----------")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("----------")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

def ia(board:dict):
    ocuppied = True
    while ocuppied == True:
        r = random.choices(list(board.keys()))
        if board[r] == str(r):
            board[r] = "O"
            ocuppied = False

def check_winner(tab, lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]] == tab[cmb[1]] == tab[cmb[2]]:
            return True
    return False

def game(tab:dict):
    lista_combinaciones = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,4],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    turnos = 0
    while turnos < 10:
        display_tablero(tab)
        correcto = juega_usuario(tab)
        if correcto:
            gana = check_winner(tab, lista_combinaciones)
            if gana == True:
                print("Ganaste!")
                break
            else:
                print("Ganó la IA")
            ia(tab)
        turnos += 1


def juega_usuario(tab):
    turno_correcto = False
    usuario = input("Escoja celda: ")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):   
            tab[usuario] = "X"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Elija otra opción")
    return turno_correcto

# print(f"tablero :{tablero}")
# print(f"tab_dict :{tab_dict}")
# display_tablero(tab_dict)
if __name__ == "__main__":
    game(tab_dict)
