class Persona :
    def __init__(self, nombre, apellido, profesion, edad):
        self.nombre = nombre;
        self.apellido =apellido;
        self.profesion = profesion;
        self.edad = edad;
    
    def caminata(self):
        return "Sale a caminar....";
    
class Bici(Persona):
    def __init__(self,nombre, apellido, profesion, edad, marca, color ):
        super().__init__(nombre, apellido, profesion, edad);
        
        self.marca = marca;
        self.color = color;
        
        
    def vueltas(self):
        return "Pasea en bici...";
    
    



JuanLopez = Persona ( "Juan","Lopez","Abogado", 25);
naveEspacial = Bici( "Juan","Lopez","Abogado", 25, "Massino", "Amarrilla")

print (f' {JuanLopez.nombre}  {JuanLopez.apellido} tiene {JuanLopez.edad} años, y es de profesion {JuanLopez.profesion}')
print (f'Por las tardes el {JuanLopez.caminata()}, y otras veces {naveEspacial.vueltas()} ')
print (f'Su bici es de color {naveEspacial.color} y su  es marca {naveEspacial.marca}')