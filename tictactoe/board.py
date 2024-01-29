from colorama import Fore, Back, Style, Cursor
tablero = [x for x in range(0,9)] #0,1,2,3...8
tab_dict= {x:str(x) for x in tablero}

def display_tablero(tablero:dict):
    reset = Style.RESET_ALL
    #bg = Back.__ne__
    blue = Fore.BLUE
    board_color = Fore.LIGHTCYAN_EX
    x_color = Fore.RED
    o_color = Fore.GREEN
    X = x_color + "X"
    O = o_color + "O"
    BD = board_color + "------"
    BS = board_color + "|"
    d = {}
    for k,v in tablero.items():
        if v == "X":
            d[k] = X + BS
        elif v == "O":
            d[k] = O + BS
        else:
            d[k] = blue + str(k) + BS
   # posicion = Cursor.POS(10,5)

    print(Cursor.POS(10,5)+f"{BD}{reset}")
    print(Cursor.POS(10,6)+f"{d[0]}{d[1]}{d[2]}{reset}")
    print(Cursor.POS(10,7)+f"{BD}{reset}")
    print(Cursor.POS(10,8)+f"{d[3]}{d[4]}{d[5]}{reset}")
    print(Cursor.POS(10,9)+f"{BD}{reset}")
    print(Cursor.POS(10,10)+f"{d[6]}{d[7]}{d[8]}{reset}")
    print(Cursor.POS(10,11)+f"{BD}{reset}")
    print(Cursor.POS(10,12)+Style.RESET_ALL)

def juega_usuario(tab):
    turno_correcto = False
    usuario = input(Cursor.POS(10,11)+"  Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario]="X"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto    

def check_winner(tab,lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]]==tab[cmb[1]]==tab[cmb[2]]:
            return True
    return False

if __name__ == "__main__":
    display_tablero(tab_dict)
    juega_usuario(tab_dict)