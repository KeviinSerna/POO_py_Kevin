#completado
class textos():
    def __init__(self, tipo, tamaño, autor):
        self._tipo = tipo
        self._tamaño = tamaño
        self._autor = autor
    
    def libros(self):
        print(f"Este libro es de tipo {self._tipo}, su tamaño es de {self._tamaño} páginas y su autor es {self._autor}.")
    
    def get_tipo(self):
        return self._tipo
    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo
    
    def get_tamaño(self):
        return self._tamaño
    def set_tamaño(self, cantidad_hojas):
        self._tamaño = cantidad_hojas
    
    def get_autor(self):
        return self._autor
    def set_autor(self, autor_real):
        self._autor = autor_real

principito = textos("informativo", "pequeño", "fredy")
iliada = textos("investigativo", "grande", "Camilo")

print("----------------------------")
print("Datos Erroneos")
print("----------------------------")
principito.libros()
iliada.libros()
print("----------------------------")
print("Corrección de los datos")
print("----------------------------")

print(principito.get_tipo())
principito.set_tipo("narrativo")
print(principito.get_tipo())
print("----------------------------")

print(principito.get_tamaño())
principito.set_tamaño("120")
print(principito.get_tamaño())
print("----------------------------")

print(principito.get_autor())
principito.set_autor("Antoine")
print(principito.get_autor())
print("----------------------------")  

print(iliada.get_tipo())
iliada.set_tipo("epopeya")
print(iliada.get_tipo())
print("----------------------------")

print(iliada.get_tamaño())
iliada.set_tamaño(334)
print(iliada.get_tamaño())
print("----------------------------")

print(iliada.get_autor())
iliada.set_autor("Homero")
print(iliada.get_autor())
print("----------------------------")
print("----------------------------")
print("datos correctos")
print("----------------------------")
principito.libros()
iliada.libros()

class periodicos(textos):
    def __init__(self,tipo, tamaño, autor, antiguedad):
        super().__init__(tipo, tamaño, autor)
        self._antiguedad = antiguedad
    def noticias(self):
        print(f"Esta noticia es de tipo {self._tipo}, tiene una longitud de {self._tamaño} palabras, su autor es {self._autor} y tiene una antiguedad de {self._antiguedad} años.")

    def get_antiguedad(self):
        return self._antiguedad
    def set_antiguedad(self, antiguedad_real):
        self._antiguedad = antiguedad_real

print("----------------------------")
print("Datos Erroneos periodico")
print("----------------------------")
espectador = periodicos("narrativo", "pequeño", "David", 1)

espectador.noticias()

print("----------------------------")
print("Corrección de los datos periodico")
print("----------------------------")

print(espectador.get_tipo())
espectador.set_tipo("Informativo")
print(espectador.get_tipo())
print("----------------------------")

print(espectador.get_tamaño())
espectador.set_tamaño("340")
print(espectador.get_tamaño())
print("----------------------------")

print(espectador.get_autor())
espectador.set_autor("Andres Santos")
print(espectador.get_autor())
print("----------------------------")  

print(espectador.get_antiguedad())
espectador.set_antiguedad(3)
print(espectador.get_antiguedad())
print("----------------------------")

print("----------------------------")
print("datos correctos periodico")
print("----------------------------")
espectador.noticias()
print("----------------------------")