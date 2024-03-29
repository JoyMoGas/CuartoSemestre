class Jugador:
    def __init__(self, nombre, simbolo, lista_simbolos) -> None:
        self.nombre = nombre
        simbolo = str(simbolo).upper()
        if len(lista_simbolos) == 1:
            self.simbolo = lista_simbolos.pop()
        else:
            if simbolo not in lista_simbolos:
                self.simbolo = lista_simbolos.pop()
            else:
                idx = lista_simbolos.index(simbolo)
                self.simbolo = lista_simbolos.pop(idx)

        self.juegos = {'ganados': 0,
                       'perdidos': 0,
                       'empatados': 0}

    def __str__(self) -> str:
        g = self.juegos["ganados"]
        p = self.juegos["perdidos"]
        e = self.juegos["empatados"]
        return f"Jugador: {self.nombre} Símbolo: {self.simbolo} g: {g} p: {p} e: {e}"

if __name__ == "__main__":
    simbolos = ["X", "O"]
    j1 = Jugador("Bob", "123", simbolos)
    j2 = Jugador("Patrick", "456", simbolos)
    print(j1)
    print(j2)
    print(simbolos)
