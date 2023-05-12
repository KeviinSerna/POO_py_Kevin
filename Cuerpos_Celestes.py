#En desarrollo
class cuerpos_celestes:
    def __init__(self, nombre, ubicación, tamaño):
        self.nombre = nombre
        self.ubicación = ubicación
        self.tamaño = tamaño

        
    def via_lactea(self):
        print(f"El planeta se llama {self.nombre}, y está ubicado en la posición {self.ubicación} en la vía lactea ")
        
    def grandes(self):
        print(f"Su tamaño es {self.tamaño}Km de radio.")

Tierra = cuerpos_celestes("tierra", 3, 6371)
Marte = cuerpos_celestes("marte", 4, 3389)

print("--------------------------------------------------")
Tierra.via_lactea()
Tierra.grandes()
print("--------------------------------------------------")
Marte.via_lactea()
Marte.grandes()
print("---------------------------------------------------------")

class lunas(cuerpos_celestes):
    def __init__(self, nombre, ubicación, tamaño, planeta_que_orbita):
        super().__init__(nombre, ubicación, tamaño)
        self._planeta_que_orbita = planeta_que_orbita
    
    def satelite(self):
        print(f" Este satelite se llama {self.nombre}, está ubicado a {self.ubicación}Km del planeta que orbita, el cual es {self._planeta_que_orbita}.")
        
    
    def get_planeta_que_orbita(self):
        return self._planeta_que_orbita
    def set_planeta_que_orbita(self, nuevo_planeta_que_orbita):
        self._planeta_que_orbita = nuevo_planeta_que_orbita

print("Lunas de los planetas")
selene = lunas("selene", 384400, 1737, "marte")

selene.satelite()
selene.grandes()
print("------------------------------------------------------------------------")

print(selene.get_planeta_que_orbita())
selene.set_planeta_que_orbita("tierra")
print(selene.get_planeta_que_orbita())

print("--------------------------------------------------------------------")

selene.satelite()
selene.grandes()
print("--------------------------------------------------")