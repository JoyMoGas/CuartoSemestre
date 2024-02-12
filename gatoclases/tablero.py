from colorama import Fore, Back, Style, Cursor


class Tablero:
    def __init__(self, color_fondo, color_rayas, color_simbolos, color_x, color_o) -> None:
        self.lista_numeros = [x for x in range(0,9)]
        self.dicc_posiciones = {x:str(x)for x in self.lista_numeros}
        self.combos_ganadores = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]
        self.color = {"rayas":color_rayas,
                    "fondo": color_fondo,
                    "numeros": color_numeros,
                    "X": color_x,
                    "O": color_o}

    def display(self):
        ##clear_screen()
        tablero = self.dicc_posiciones
        reset = Style.RESET_ALL
        bg = self.color["fondo"]#Back.WHITE
        blue = self.color["numeros"] #Fore.BLUE
        board_color = self.color["rayas"]
        x_color = self.color["X"] #Fore.RED
        o_color = self.color["O"]  #Fore.GREEN
        X = x_color + "X"
        O = o_color + "O"
        BD = board_color + "------"
        BS = board_color + "|"
        d = {}
        for k, v in tablero.items():
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
