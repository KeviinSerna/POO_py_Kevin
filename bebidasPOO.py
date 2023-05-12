#Completado
#clase
class bebidas:
    #Atributos
    def __init__(self, tipo, sabor, color):
        self.tipo=tipo
        self._sabor=sabor
        self._color=color
    #Metodos
    def saborea(self):
        print(f"La bebida es un {self.tipo} y sabe a {self._sabor} ")
    def observa(self):
        if self._color is not None:
            print(f" Esta bebida tiene un color {self._color}")
        else:
            print("No se conoce el color de esta bebida.")
    
    #getter y setter
    def get_sabor(self):
        return self._sabor
    def set_sabor(self, nuevo_sabor):
        self._sabor= nuevo_sabor
    
    def get_color(self):
        return self._color
    def set_color(self, nuevo_color):
        self._color=nuevo_color
#objetos
primer_trago = bebidas ("cerveza", "café", "dorado")
segundo_trago = bebidas ("jugo", "mora", "rojo")

#Imprimir notas
print("--------------------------------------------------------")
primer_trago.saborea()
primer_trago.observa()
print("---------------------------------")
segundo_trago.saborea()
segundo_trago.observa()
print("---------------------------------")

print("------------------------------------------------------------------------")

#imprimir getter y setter
print(primer_trago.get_sabor())
primer_trago.set_sabor("agua sucia")
print(primer_trago.get_sabor())

print(primer_trago.get_color())
primer_trago.set_color("negro")
print(primer_trago.get_color())

print("--------------------------------------------------------------------")

print("------------------------------------------------------------------------")

print(segundo_trago.get_sabor())
segundo_trago.set_sabor("maracuyá")
print(segundo_trago.get_sabor())

print(segundo_trago.get_color())
segundo_trago.set_color("amarillo")
print(segundo_trago.get_color())

print("--------------------------------------------------------------------")

#imprimir notas con los cambios
primer_trago.saborea()
primer_trago.observa()
print("---------------------------------")
segundo_trago.saborea()
segundo_trago.observa()
print("---------------------------------")

#clase hija
class alcohol(bebidas):
    #atributos
    def __init__(self, tipo, sabor, nivel_alcohol):
        super().__init__(tipo, sabor, color=None)
        self.nivel_alcohol = nivel_alcohol
    #metodos
    def catador(self):
        print(f"Este trago tiene un nivel de {self.nivel_alcohol}% de alcohol")
#objetos
tercer_trago = alcohol("aguardiente", "caña de mi tierra", 12.5)
#imprimir objetos
tercer_trago.catador()
tercer_trago.saborea()
tercer_trago.observa()
print("--------------------------------------------------------------------------")
        