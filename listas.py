
planetas = list()
planetas = []
planetas = ["Mercurio", "Venus", "Tierra", "Marte"]
print(type(planetas))
print(planetas)

for i in planetas:
    print(i)

planetas.append("Urano")
planetas.append("Neptuno")

print(planetas)

p = planetas.pop()
print(planetas)
print(p)

pa = planetas.pop(0)
print(planetas)
print(pa)

planetas.insert(0, pa)
print(planetas)

lunas = ["Luna", "Ceres", "Deimos", "Phobos"]
print(lunas[1])
print(lunas[3])

lunas.append("Europa")
lunas.append("Titan")
lunas.append("Ganymede")
lunas.append("Callisto")
lunas.append("Io")
print(lunas)

i = 3
print(lunas[0:i])
print(lunas[i:])
print(lunas[-9])
print(lunas[::2])
print(lunas[::-1])
moons = lunas
print(f"lunas_list {lunas} \nmoons_list {moons}")
moons.append("Triton")
print(f"lunas_list {lunas} \nmoons_list {moons}")
print(f"moons id:{id(moons)}")
print(f"moons id:{id(lunas)}")

moons = lunas.copy()
moons.append("Charon")
print(f"moons id:{id(moons)}")
print(lunas)
print(moons)

planetas_ws = ["Hoth", "Tatooine", "Naboo", "Mustafar", "Endor", "Kamino"]
planetas.extend(planetas_ws)
planetas.sort()
print(planetas)

moons_sw = ["Yavin 4", "Dagobah", "Coruscant", "Kashyyyk", "Geonosis", "Utapau"]
lista_lunas = [lunas, moons_sw]
print(lista_lunas)
print(lista_lunas[1][0])
print("----------------")

for i, planeta in enumerate(planetas):
    print(i, planeta)
    
print(planetas.index("Marte"))
print(planetas)
planetas.reverse()
print(planetas)
print("----------------")
A = []
for i in range(0, 10):
    A.append(i)
print(A)

B = []
for i in range(0, 10):
    if i % 2 == 0:
        B.append(i)
print(B)
print("----------------")
A = [i for i in range(0,10)]
B = [i for i in range(0,10) if i % 2 == 0]
print(f"A: {A} ")
print(f"B: {B} ")
squares = [i**2 for i in range(0,10)]
print(f"squares: {squares}")

