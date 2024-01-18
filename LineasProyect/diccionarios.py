ingenieria = {} # CREACION DE DICCIONARIO
ingenieria["ISI"] = "Ingeniería de Sistemas de Información"
ingenieria["IIS"] = "Ingeniería Industrial y de Sistemas"
ingenieria["IME"] = "Ingeniería Mecatrónica"
print(ingenieria)
minas = dict() # CREACION DE DICCIONARIO
minas["IM"] = "Ingeniería de Minas"
minas["IMM"] = "Ingeniería de Minas y Metalurgia"
minas["IME"] = "Ingeniería Mecánica de Suelos"
print(minas)
# CREACION DE DICCIONARIO CON DICCIONARIO
facultad = {"ingeniería": ingenieria, "minas": minas}
print(facultad['ingeniería']['IME'])
print(facultad['minas']['IME'])
print("----------------")

if 'civil' in facultad:
    print(f"Civil: {facultad['civil']}")
else:
    print("No existe la carrera de civil")
print("----------------")

try:
    print(f"Civil: {facultad['civil']}")
except KeyError:
    print("No existe la carrera de civil")
print("----------------")
if 'civil' not in facultad:
    facultad['civil'] = {}
    facultad['civil']['IC'] = 'Ingenieria Civil'
if 'civil' in facultad:
    print(f"Civil: {facultad['civil']}")
print("----------------")

cadena = "El caballo corre por el campo"
diccionario = {}
for letra in cadena:
    if letra not in diccionario:
        diccionario[letra] = 1
    else:
        diccionario[letra] += 1
print(diccionario)
for k, v in diccionario.items():
    print(f"{k}: {v}")
print("----------------")
diccionario_ordenado = sorted(diccionario.items(), key=lambda item: item[1], reverse=True)
print(diccionario_ordenado)
print("----------------")
diccionario_ordenado = dict(diccionario_ordenado)
for k, v in diccionario_ordenado.items():
    print(f"{k}: {v}")
print("----------------")
diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item: item[0]))
for k, v in diccionario_ordenado.items():
    print(f"{k}: {v}")
