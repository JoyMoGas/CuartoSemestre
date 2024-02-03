import game_logic
import os


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
        game_logic.game_cycle(name1, name2)

    elif 2:
        nameP = input("Ingresa tu username:")
        game_logic.game_cycle(nameP, "IA")


if __name__ == "__main__":
    run()
