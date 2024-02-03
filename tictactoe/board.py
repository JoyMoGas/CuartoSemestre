from colorama import Fore, Back, Style, Cursor
import os


def clear_screen():
    os.system("cls")


def juega_usuario(tab, player: int):
    turno_correcto = False
    usuario = input("Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            if player == 1:
                tab[usuario] = "X"
            elif 2:
                tab[usuario] = "O"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto


def display_tablero(tab: dict):
    ##clear_screen()
    reset = Style.RESET_ALL
    bg = Back.WHITE
    blue = Fore.BLUE
    board_color = Fore.LIGHTCYAN_EX
    x_color = Fore.RED
    o_color = Fore.GREEN
    X = x_color + "X"
    O = o_color + "O"
    BD = board_color + "------"
    BS = board_color + "|"
    d = {}
    for k, v in tab.items():
        if v == "X":
            d[k] = X + BS
        elif v == "O":
            d[k] = O + BS
        else:
            d[k] = blue + str(k) + BS
    Cursor.POS(10, 5)
    ##print(Cursor.POS(10,3)+ f"{bg}{BD}{reset}")
    print(Cursor.POS(10, 3) + f"{bg}{BD}{reset}")
    print(Cursor.POS(10, 4) + f"{bg}{d[0]}{d[1]}{d[2]}{reset}")
    print(Cursor.POS(10, 5) + f"{bg}{BD}{reset}")
    print(Cursor.POS(10, 6) + f"{bg}{d[3]}{d[4]}{d[5]}{reset}")
    print(Cursor.POS(10, 7) + f"{bg}{BD}{reset}")
    print(Cursor.POS(10, 8) + f"{bg}{d[6]}{d[7]}{d[8]}{reset}")
    print(Cursor.POS(10, 9) + f"{bg}{BD}{reset}")
