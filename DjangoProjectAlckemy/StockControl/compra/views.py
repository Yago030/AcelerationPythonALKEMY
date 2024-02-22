from django.shortcuts import render,redirect

from .models import Producto, Proveedor;
from .forms import ProductoForm, ProveedorForm;


def inicio(request): ##esto para que nos reediriga al inicio 
    return redirect('listar_productos')

##funcion para ver los productos que ya cargamos 
def listar_productos(request): ## representa la solicitud HTTP recibida por el servidor.
    productos = Producto.objects.all() #para recuperar todos los objetos de tipo Producto de la base de datos. 
    return render(request, 'listar_productos.html', {'productos': productos});



##funcion para agregar productos
def agregar_productos(request): ## representa la solicitud HTTP recibida
    if request.method == 'POST': 
        form = ProductoForm(request.POST)
        if form.is_valid(): # si esta correcto lo guardo 
            form.save()
            return redirect('listar_productos');
    
    else:
        form = ProductoForm();
    return render(request, 'agregar_producto.html', {'form': form});


def agregar_proveedor(request): 
     if request.method == 'POST':
          form = ProveedorForm(request.POST)
          if form.is_valid():
               form.save()  
               return redirect('listar_productos')
     else:
         form = ProveedorForm();
     return render(request, 'agregar_proveedor.html', {'form': form});