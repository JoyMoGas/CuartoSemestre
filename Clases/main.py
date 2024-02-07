from Athlete import Athlete
from Sport import Sport
from Team import Team
import json

def main():
    players = ['Chicharito', 'Piojo', 'Alexis Vega', 'La Tota', 'Chuki', 'Tecatito', 'Cuahutemoc', 'Hermoso', 'Piqué', 'Messi', 'Ochoa']

    players_objects = [Athlete(x) for x in players]
    s = Sport("Soccer", 11, "LaBrisaMarinera")
    t = Team("LaBrisaMarinera", s)
    for a in players_objects:
        t.add_player(a)
    t.display()

    players_b = ["Iniesta", "Xavi", "Neymar", "Hulk", "Lewandoswi", "Puyol", "Miguel", "Aaron", "Francisco", "Maradona", "kaká"]

    s2 = Sport("Soccer", 11, "FIFA")
    t2 = Team("MotoresLocos", s2)
    torneo = { t.name:t.to_json(), t2.name:t2.to_json()}

    with open("torneo_soccer.json", "w") as archivo:
        archivo.dump(torneo,archivo)

def procesa_diccionari(diccionario:dict):
    for k1, v1 in diccionario.items():
        