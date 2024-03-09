class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return f"¡Guau!" 

class Gato(Animal):
    def hacer_sonido(self):
        return f"¡Miau!"
