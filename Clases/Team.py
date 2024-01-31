from Athlete import Athlete
from Sport import Sport

class Team:
    def __init__(self, name:str, sport:Sport) -> None:
        self.name = name
        self.sport = sport
        self.players = []

    def add_player(self, athlete:Athlete):
        self.players.append(athlete)

    def display(self):
        print(f"Team {self.name}")
        print(f" {self.sport}")
        for athlete in self.players:
            print(f"{athlete}")

if __name__ == "__main__":
    a = Athlete("Chicharito")
    b = Athlete("Piojo Alvarado")
    s = Sport("Soccer", "11", "LMX")
    t = Team("Chivas de guadalaverga", s)
    t.add_player(a)
    t.add_player(b)
    t.display()
