from jugador import Jugador
from tablero import Tablero
from main import display_menu
import os


class Juego:
    def __init__(self, tablero: Tablero, jugador_a: Jugador, jugador_b: Jugador) -> None:
        self.tablero = tablero
        self.jugador_a = jugador_a
        self.jugador_b = jugador_b
        self.turnos = 0

    def jugar(self, moviendo: Jugador, en_espera: Jugador):
            ganador = False
            mov = False
            while mov == False:
                print(f"Mueve: {moviendo.nombre}")
                mov = self.tablero.juega_usuario(moviendo)
            self.turnos += 1
            mov = False
            self.tablero.display()
            if (self.tablero.revisa_linea_ganadora()):
                moviendo.juegos["ganados"] += 1
                en_espera.juegos["perdidos"] += 1
                ganador = True
                print(f"Ganó {self.jugador_a.nombre}")
            self.turnos += 1
            return ganador


    def inicia_juego(self):
        self.tablero.reset_tablero()
        mov = False
        while self.turnos < 9:
            self.tablero.display()
            g = self.jugar(moviendo=self.jugador_a, en_espera=self.jugador_b)
            if (g != True):
                 g = self.jugar(moviendo=self.jugador_b, en_espera=self.jugador_a)
                 if (g == True):
                      self.turnos = 9
            else:
                 self.turnos = 9

    def game_cycle(self, moviendo: Jugador, en_espera: Jugador):
        score = {moviendo: 0, en_espera: 0, "Empates": 0}
        continuar = True
        while continuar:
            tab_dict = {x: str(x) for x in Tablero}
            d = jugar(tab_dict, moviendo, en_espera)
            display_score(score, d)
            continuar = jugar_otra_vez()
            os.system("cls")

def display_score(s: dict, d: dict):
    if d["ganador"] != "":
        s[d["ganador"]] += 1
    else:
        s["Empate"] += 1
        print("¡Empate!")
    print(
        f"<<{list(s.keys())[0]}: {list(s.values())[0]}>> <<{list(s.keys())[1]}: {list(s.values())[1]}>> <<Empates: {s['Empates']}>>"
    )

def jugar_otra_vez():
    jugar = True
    otra_vez = input("¿Quieres jugar otra vez? (S/N): ")
    otra_vez = otra_vez.upper()
    if otra_vez != "S":
        jugar = False
        print("¡Gracias por jugar!")
    return jugar

if __name__ == "__main__":
    lista = ["X", "O"]
    a = Jugador("Roberto", "X", lista)
    b = Jugador("Francisco", "O", lista)
    tab = Tablero()
    juego = Juego(tab,a,b)
    juego.inicia_juego()            
