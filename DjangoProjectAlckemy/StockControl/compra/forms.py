from django import forms
from .models import Proveedor  ##no olvidarnos importar esto porque no va andar ni para adelante ni para atras, 
from .models import Producto ## lo de arriba x2
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProveedorForm(forms.ModelForm): ##aprovechando las funciones de django con forms tenemos maas funciones
    class Meta: #define metadatos adicionales para el formulario. es una clase anidada de forms
        model = Proveedor; ##avisamos que esta clase esta vinculada a nuestro modelo de Proveedor
        fields = ['nombre', 'apellido', 'dni'] ##avisamos que datos vamos  a tneer el form, parace ser algo asi como descontruction de react en inversa
    
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Agregar Proveedor'))
    
          
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_actual': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-select'})
        }