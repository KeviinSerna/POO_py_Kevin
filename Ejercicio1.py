#completado
#clase
class person:
    #atributos
    def __init__(self, name, years, profession):
        self.name=name
        self.years=years
        self.profession=profession
    #métodos
    def greet(self):
        print(f"Hello, my name is {self.name}")
    def presented(self):
        print(f"I am {self.name}, I am {self.years} years old, and I am {self.profession}")
#objetos
carlos=person("Carlos",25,"Engineer")
camilo=person("Camilo",28,"Psychologist")
#Imprimir presentaciones
print("-------------------------------")
carlos.greet()
print("--------------------------------------------")
camilo.greet()
print("-----------------------------------------")
carlos.presented()
print("--------------------------------------------")
camilo.presented()
print("-----------------------------------------------")

#clase hija
class student(person):
    #atributos
    def __init__(self, name, years, degree, study_interest):
        super().__init__(name, years, profession=None)#llamo atributos de la clase padre y con none no heredo profession
        self._degree=degree
        self._study_interest=study_interest
    
    #métodos
    def school(self):
        print(f"we are students of IEENSSF, of the degree {self._degree}")
    def interviewed(self):
        print(f"I am {self.name}, I am {self.years} and I want to study {self._study_interest}. ")
    
    #getter y setter
    def get_degree(self):
        return self._degree
    def set_degree(self, new_degree):
        self._degree = new_degree
        
    def get_study_interest(self):
        return self._study_interest
    def set_study_interest(self, new_study_interest):
        self._study_interest = new_study_interest
    
#Onjetos
andrea=student("Andrea", 12, 7, "economist")
santiago=student("Santiago", 15, 9, "police")
#imprimir presentaciones
print("-----------------------------------------")
andrea.school()
print("---------------------------------------")
andrea.interviewed()
print("-------------------------------------------")
santiago.school()
print("----------------------------------------------------")
santiago.interviewed()
print("---------------------------------------------")

# imprimir cambios en getter y setter
print(andrea.get_degree())
andrea.set_degree(10)
print(andrea.get_degree())

print(andrea.get_study_interest())
andrea.set_study_interest("sales")
print(andrea.get_study_interest())

print("--------------------------")

print(santiago.get_degree())
santiago.set_degree(12)
print(santiago.get_degree())

print(santiago.get_study_interest())
santiago.set_study_interest("policy")
print(santiago.get_study_interest())

print("--------------------------")

#imprimir presentaciones con cambios en los objetos
print("-----------------------------------------")
andrea.school()
print("---------------------------------------")
andrea.interviewed()
print("-------------------------------------------")
santiago.school()
print("----------------------------------------------------")
santiago.interviewed()
print("---------------------------------------------")
