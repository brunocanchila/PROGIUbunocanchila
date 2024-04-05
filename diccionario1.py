perro = {}

perro["nombre"] = "alberto"
perro["color"] = "negro"
perro["raza"] = "pastor aleman"
perro["patas"] = "4" 
perro["edad"] = "9 meses"

estudiante = {
  "nombre":"bruno",
  "apellido":"canchila bahamon",
  "sexo":"masculino",
  "edad":"19 años",
  "estado civil": "comprometido",
  "habilidades":["empatico, flexibilidad"],
  "pais":"colombia",
  "ciudad":"caratgena",
  "direccion":"las gaviotas"
}

print(estudiante)
print(len(perro))
print(estudiante["habilidades"])
estudiante["habilidades"].append("vision")
print(estudiante["habilidades"])
keys = estudiante.keys()
print(keys)
values = estudiante.values()
print(values)
print(estudiante.items())
estudiante.pop("estado civil")
print(estudiante)
print(estudiante.clear())