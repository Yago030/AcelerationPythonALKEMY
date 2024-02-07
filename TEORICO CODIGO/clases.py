#aca creamos las clases
class Persona:
    #aca creamos los metodos que tendra esto
    
    def __init__(self, nombre , apellido, direccion):
        self.nombre = nombre;
        self.apellido = apellido
        self.__direccion = direccion;
    
    def caminar(self):
        return "caminando .... "
    
#aca creamos las personas
juan = Persona() 
maria = Persona()
sergio = Persona()

