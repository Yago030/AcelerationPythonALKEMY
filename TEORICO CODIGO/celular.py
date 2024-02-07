class Celular:
    def __init__(self, marca , color):
        self.marca = marca
        self.color = color
        
    def llamar(self, numero):
        return f"Llamando al {numero} ... "
    

class Samsung(Celular): # aqui avisamos que heredaremos atributos de Celular
    
    
    def enviar_mensaje(self, numero):
        return f"Enviando mensjae al {numero} ... "
    
samsung_a30 = Samsung("Samsung","Azul");

print (samsung_a30.llamar(2323232323));
print (samsung_a30.enviar_mensaje(2556654645))
print (samsung_a30.color);