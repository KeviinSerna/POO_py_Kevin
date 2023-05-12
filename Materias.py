#completado
class Materias:
    def __init__(self, nombre, nota, horario):
        self.nombre = nombre
        self.nota = nota
        self.horario = horario

        
    def datos(self):
        print(f"La Materia es {self.nombre}, tuvo una nota de {self.nota}, y el horario es {self.horario}")

santiago = Materias("matematicas", 2.99, "diurno")
kevin = Materias("matemáticas", 5.0, "nocturno")

santiago.datos()
kevin.datos()
print("---------------------------------------------------------")

class diplomado(Materias):
    def __init__(self, nombre, nota, horario, dificultad):
        super().__init__(nombre, nota, horario)
        self._dificultad = dificultad
    
    def datos2(self):
        print(f"El diplomado es {self.nombre}, tuvo una nota de {self.nota}, y el horario es {self.horario}, y su dificultad es {self._dificultad} ")
    
    def get_dificultad(self):
        return self._dificultad
    def set_dificultad(self, nueva_dificultad):
        self._dificultad = nueva_dificultad

    
david = diplomado("fracciones", 3.9, "nocturno", "media")

david.datos2()

print("------------------------------------------------------------------------")

print(david.get_dificultad())
david.set_dificultad("alta")
print(david.get_dificultad())

print("--------------------------------------------------------------------")

david.datos2()
        