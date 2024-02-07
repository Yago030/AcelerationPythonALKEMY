class Animal:
    def __init__(self,  cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas;
        self.tipo = tipo;
        
        
    def comer(self):
        return "Estoy comiendo...";
    
    
class Perro(Animal):
    def __init__ (self,  cantidad_patas, tipo, nombre, raza): #cuando invoco  los atributos tambien paso los de la clase padre para usarlos aqui 
        super().__init__( cantidad_patas, tipo) #esto porque llamo los atributos de mi clase padre
        self.nombre = nombre;
        self.raza = raza;
        
    def correr(self):
        return "Estoy corriendo...";
    
class Aguila(Animal):
    
    def volar(self):
        return "Estoy volando...";
    
    
    
# Crear instancias de las clases
mi_mascota_es_un_monstruo = Aguila(2, "Ave")
tengo_un_bicho = Perro(4, "Mamífero", "Panchin", "Perro Salchicha")

# Imprimir los resultados
print(mi_mascota_es_un_monstruo.volar())
print(tengo_un_bicho.nombre)
print(tengo_un_bicho.raza)
print(tengo_un_bicho.correr())