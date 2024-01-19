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
        r = random.choices(board.keys())
        if board[r] == str(r):
            board[r] = "O"
            ocuppied = False

def game(tab:dict):
    while True:
        display_tablero(tab)
        usuario = input("Escoja celda: ")
        usuario = int(usuario)
        if usuario in tab:
            if tab[usuario] == str(usuario):   
                tab[usuario] = "X"
            else:
                print(f"Posición {usuario} ocupada")
                print("Elija otra opción")

# print(f"tablero :{tablero}")
# print(f"tab_dict :{tab_dict}")
# display_tablero(tab_dict)
if __name__ == "__main__":
    game(tab_dict)
