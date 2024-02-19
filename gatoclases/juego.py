from jugador import Jugador
from tablero import Tablero
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
        while not mov:
            print(f"Mueve: {moviendo.nombre}")
            mov = self.tablero.juega_usuario(moviendo)
        self.turnos += 1
        mov = False
        self.tablero.display()
        if self.tablero.revisa_linea_ganadora():
            moviendo.juegos["ganados"] += 1
            en_espera.juegos["perdidos"] += 1
            ganador = True
            print(f"Ganó {moviendo.nombre}")
        self.turnos += 1
        return ganador

    def inicia_juego(self):
        self.tablero.reset_tablero()
        while self.turnos < 9:
            self.tablero.display()
            g = self.jugar(moviendo=self.jugador_a, en_espera=self.jugador_b)
            if not g:
                g = self.jugar(moviendo=self.jugador_b, en_espera=self.jugador_a)
                if g:
                    self.turnos = 9
            else:
                self.turnos = 9

    def game_cycle(self, moviendo: Jugador, en_espera: Jugador):
        score = {moviendo.nombre: 0, en_espera.nombre: 0, "Empates": 0}
        continuar = True
        while continuar:
            tab_dict = {x: str(x) for x in self.tablero.lista_numeros}
            d = self.jugar(tab_dict, moviendo, en_espera)
            self.display_score(score, d)
            continuar = self.jugar_otra_vez()
            os.system("cls")

    def display_score(self, s: dict, d: dict):
        if d["ganador"] != "":
            s[d["ganador"]] += 1
        else:
            s["Empate"] += 1
            print("¡Empate!")
        print(
            f"<<{list(s.keys())[0]}: {list(s.values())[0]}>> <<{list(s.keys())[1]}: {list(s.values())[1]}>> <<Empates: {s['Empates']}>>"
        )

    def jugar_otra_vez(self):
        jugar = True
        otra_vez = input("¿Quieres jugar otra vez? (S/N): ")
        otra_vez = otra_vez.upper()
        if otra_vez != "S":
            jugar = False
            print("¡Gracias por jugar!")
        return jugar