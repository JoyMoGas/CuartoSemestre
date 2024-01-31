from Athlete import Athlete
from Sport import Sport
from Team import Team

def main():
    players = ['Chicharito', 'Piojo', 'Alexis Vega', 'La Tota', 'Chuki', 'Tecatito', 'Cuahutemoc', 'Hermoso', 'Piqué', 'Messi', 'Ochoa']

    players_objects = [Athlete(x) for x in players]
    s = Sport("Soccer", 11, "LaBrisaMarinera")
    t = Team("LaBrisaMarinera", s)
    for a in players_objects:
        t.add_player(a)
    t.display()
