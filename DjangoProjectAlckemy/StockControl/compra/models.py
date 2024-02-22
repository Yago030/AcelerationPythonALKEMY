from django.db import models


class Proveedor(models.Model): ## debemos usar models.model ya que nos aplia el uso de funciones 
    nombre = models.CharField(max_length=100);
    apellido = models.CharField(max_length=100);
    dni = models.IntegerField();
    
    def __str__(self): ## con el metdoo __str__ hacemos que nos devuelva un objeto en string, o cadena de texto como sea
        return f'{self.nombre} {self.apellido} ';
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100);
    precio = models.DecimalField(max_digits=10, decimal_places=2);
    stock_actual = models.IntegerField();
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE); ## aca hacemos referencia a una clave forranea, que cuando borremos el proveedor del otro modelo tambien se borre de aqui
    
    def __str__(self): ## de nuevo pasamos aca el producto en nombre, en cadena de texto
        return f'{self.nombre} ';