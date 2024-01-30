class Athlete:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Greetings: {self.name}")
        
    def __str__(self) -> str:
        return f"Athlete is '{self.name}'"
    
    def __repr__(self) -> str:
        return f'Athlete(name="{self.name}")'

a = Athlete("Pepe el toro")
a.display()

a.__str__()
print(a)

a = a.__repr__()
b = eval(repr(a))
print(a)
print(b)