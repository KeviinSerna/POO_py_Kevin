#completado
#clase
class animales:
    #atributos
    def __init__(self, nombre, color, origen):
        self.nombre=nombre
        self.color=color
        self._origen=origen
    #metodos
    def presentación(self):
        print(f"Este animal es el {self.nombre}, su color es {self.color} y es originario de {self._origen} ")
    
#objetos
leon = animales("león", "café", "africa")
oso_anteojos = animales("oso de anteojos", "negro", "sudamerica")

#imprimir
leon.presentación()
oso_anteojos.presentación()

#clase hijo
class domesticos(animales):
    def __init__(self, nombre, color, tamaño):
        super().__init__(nombre, color, origen = None )
        self._tamaño = tamaño
    
    def finca(self):
        print(f"En mi finca hay un animal que es un {self.nombre}, es de color {self.color} y su tamaño es {self._tamaño}")

    def get_tamaño(self):
        return self._tamaño
    def set_tamaño(self, nuevo_tamaño):
        self._tamaño = nuevo_tamaño

toro = domesticos("Toro", "blanco", "mediano")
perro = domesticos("Perro", "barcino", "pequeño")

print("--------------------------")
toro.finca()
perro.finca()
print("--------------------------")

print(toro.get_tamaño())
toro.set_tamaño("Grande")
print(toro.get_tamaño())

print("------------------------")

print(perro.get_tamaño())
perro.set_tamaño("Mediano")
print(perro.get_tamaño())

print("--------------------------")

toro.finca()
perro.finca()
print("--------------------------")