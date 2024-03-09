class Coche:
    def __init__(self, marca = "Generica", modelo = "R2", status=False ):
        self.marca = marca
        self.modelo = modelo
        self.status = status
        
    def __str__(self) :
        return f" El auto es de maca:{self.marca} y modelo:{self.modelo} "
    
    def prender(self) :
        self.status = True
        return f" El auto se acaba de prender"
        
    def apagar(self) :
        self.status = False
        return f" El auto se apago de prender"
             
    def conducir(self):
        if self.status :
            return f"Conduciendo el {self.marca} {self.modelo}"
        else :
            return f"Si no se prende primero el carro no se puede conducir"
            
            
        
    
    

