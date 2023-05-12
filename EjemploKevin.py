class Persona:
    #Atributos
    def __init__(self, nombre, edad, color_de_piel):
        self.nombre = nombre
        self.edad = edad
        self.color_de_piel = color_de_piel
    #Métodos  
    def presentarse(self):
        print(f"Me llamo {self.nombre}, tengo {self.edad} años, y soy {self.color_de_piel}.")
    
    def presentarse_en_Medellin(self):
        print("mi nombre es " + self.nombre + " y soy " + self.color_de_piel)
#Objetos     
urrao1 = Persona("Kevin", 25, "canelita")
urrao2 = Persona("Felipe", 22, "blanco")
#Imprimir presentaciones
print("--------------------------------------------------")
print("presentación de urrao1")
urrao1.presentarse()
print("------------------------------------------------------")
print("presentación de urrao2")
urrao2.presentarse()
print("----------------------------------------------------------")
print("presentación de Urrao2 en medellín")
urrao2.presentarse_en_Medellin()
print("--------------------------------------------------------")

class Estudiante(Persona):
    #Atributos
    def __init__(self, nombre, edad, color_de_piel, carrera):
        super().__init__(nombre, edad, color_de_piel)
        self.carrera = carrera
    
    #Métodos  
    def presentarse(self):
        super().presentarse()
        print(f"Estudio {self.carrera}.")

#Objetos     
estudiante1 = Estudiante("Juan", 21, "moreno", "Ingeniería de Sistemas")
estudiante2 = Estudiante("María", 19, "blanca", "Medicina")

# Imprimir presentaciones
print("Presentación de estudiante1:")
estudiante1.presentarse()
print("------------------------------------------------------")
print("Presentación de estudiante2:")
estudiante2.presentarse()