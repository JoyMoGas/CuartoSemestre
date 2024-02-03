import random
import board
import os

tablero = [x for x in range(0, 9)]  # 0,1,2,3...8
tab_dict = {x: str(x) for x in tablero}


def display_tablero(tab: dict):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("-----------")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("-----------")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")


def ia(board: dict):
    ocuppied = True
    while ocuppied == True:
        r = random.choice(list(board.keys()))
        if board[r] == str(r):  # Si está libre
            board[r] = "O"
            ocuppied = False


def juega_usuario(tab, player):
    turno_correcto = False
    usuario = input("Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            if player == 1:
                tab[usuario] = "X"
            else:
                tab[usuario] = "O"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto


def check_winner(tab, lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]] == tab[cmb[1]] == tab[cmb[2]]:
            return True
    return False


def game(tab: dict, p1: str, p2: str):
    diccionario = {"ganador": ""}
    lista_combinaciones = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    turnos = 0
    while turnos < 8:
        board.display_tablero(tab)
        correcto = board.juega_usuario(tab, 1)
        if correcto:
            turnos += 1
            gana = check_winner(tab, lista_combinaciones)
            if gana == True:
                diccionario["ganador"] = p1
                # print("¡Ganaste!")
                break
            if p2 == "IA":
                ia(tab)
                gana = check_winner(tab, lista_combinaciones)
                if gana == True:
                    diccionario["ganador"] = "IA"
                    # print("¡Ganó la IA!")
                    break
            turnos += 1
        if p2 != "IA":
            board.display_tablero(tab)
            correcto = board.juega_usuario(tab, 2)
            if correcto:
                turnos += 1
                gana = check_winner(tab, lista_combinaciones)
                if gana == True:
                    diccionario["ganador"] = p2
                    # print("¡Ganaste!")
                    break

    board.display_tablero(tab)
    return diccionario


def jugar_otra_vez():
    jugar = True
    otra_vez = input("¿Quieres jugar otra vez? (S/N): ")
    otra_vez = otra_vez.upper()
    if otra_vez != "S":
        jugar = False
        print("¡Gracias por jugar!")
    return jugar


def display_score(s: dict, d: dict):
    if d["ganador"] != "":
        s[d["ganador"]] += 1
    else:
        s["Empate"] += 1
        print("¡Empate!")
    print(
        f"<<{list(s.keys())[0]}: {list(s.values())[0]}>> <<{list(s.keys())[1]}: {list(s.values())[1]}>> <<Empates: {s['Empates']}>>"
    )


def game_cycle(player1: str, player2: str):
    score = {player1: 0, player2: 0, "Empates": 0}
    continuar = True
    while continuar:
        tab_dict = {x: str(x) for x in tablero}
        d = game(tab_dict, player1, player2)
        display_score(score, d)
        continuar = jugar_otra_vez()
        os.system("cls")
