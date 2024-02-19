import os
from juego import juego

def display_menu():
    print("***** ¿Cómo quieres jugar? *****")
    print("** 1. Modo 2 Jugadores")
    print("** 2. Modo 1 jugador \n")
    opcion = input("Ingresa la opción que desees: ")
    return int(opcion)

def run():
    opcion = display_menu()
    os.system("cls")
    if opcion == 1:
        name1 = input("Username para jugador 1:")
        name2 = input("Username para jugador 2:")
        juego.game_cycle(name1, name2)

    elif 2:
        nameP = input("Ingresa tu username:")
        #nameP2 = input("Ingresa el segundo username:")
        juego.game_cycle(nameP, "Máquina")


if __name__ == "__main__":
    run()
