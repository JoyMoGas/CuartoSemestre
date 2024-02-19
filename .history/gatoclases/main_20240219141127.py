from juego import Juego
from jugador import Jugador
from tablero import Tablero
def run():
    lista = ["X", "O"]
    
    nombre_jugador1 = input("Ingrese el nombre del Jugador 1: ")
    simbolo_jugador1 = input("Ingrese el símbolo del Jugador 1 (X o O): ").upper()
    while simbolo_jugador1 not in lista:
        simbolo_jugador1 = input("Símbolo no válido. Ingrese X o O: ").upper()
    
    nombre_jugador2 = input("Ingrese el nombre del Jugador 2: ")

   
    a = Jugador(nombre_jugador1, simbolo_jugador1, lista)
    b = Jugador(nombre_jugador2, simbolo_jugador1, lista)
    
    tab = Tablero()
    juego = Juego(tab, a, b)
    juego.inicia_juego()
    
    
    
    jugar_de_nuevo = input("¿Desea jugar de nuevo? (Sí/No): ").lower()
    while jugar_de_nuevo not in ['si', 'no']:
        jugar_de_nuevo = input("Respuesta inválida. ¿Desea jugar de nuevo? (Sí/No): ").lower()
    
    if jugar_de_nuevo == 'si':
        run()

if _name_ == "_main_":
    run()