from django import forms
from .models import Proveedor  ##no olvidarnos importar esto porque no va andar ni para adelante ni para atras, 
from .models import Producto ## lo de arriba x2

class ProveedorForm(forms.ModelForm): ##aprovechando las funciones de django con forms tenemos maas funciones
    class Meta: #define metadatos adicionales para el formulario. es una clase anidada de forms
        model = Proveedor; ##avisamos que esta clase esta vinculada a nuestro modelo de Proveedor
        fields = ['nombre', 'apellido', 'dni'] ##avisamos que datos vamos  a tneer el form, parace ser algo asi como descontruction de react en inversa
        
class ProductoForm(forms.ModelForm):
    class  Meta:
        model = Producto;
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']
        
        