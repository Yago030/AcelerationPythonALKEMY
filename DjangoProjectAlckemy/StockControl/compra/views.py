from django.shortcuts import render,redirect
from .models import Producto, Proveedor;
from .forms import ProductoForm, ProveedorForm;
from django.views.decorators.csrf import csrf_protect ## esto para que no nos hagan  ataques csrf :c  abajo deje un mini resumen de que son ataques csrf

@csrf_protect
def pagina_inicio(request):
    productos = Producto.objects.all()
    return render(request, 'pagina_inicio.html', {'productos': productos})

##funcion para ver los productos que ya cargamos
@csrf_protect 
def listar_productos(request): ## representa la solicitud HTTP recibida por el servidor.
    productos = Producto.objects.all() #para recuperar todos los objetos de tipo Producto de la base de datos. 
    return render(request, 'listar_productos.html', {'productos': productos});


@csrf_protect 
def listar_proveedores(request): ## representa la solicitud HTTP recibida por el servidor.
    proveedores = Proveedor.objects.all() #para recuperar todos los objetos de tipo Proveedor de la base de datos. 
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores});


##funcion para agregar productos
@csrf_protect
def agregar_productos(request): ## representa la solicitud HTTP recibida
    if request.method == 'POST': 
        form = ProductoForm(request.POST)
        if form.is_valid(): # si esta correcto lo guardo 
            form.save()
            return redirect('listar_productos');
        else:
            ##este lo usamos para avisar que algo no esta bien en el formulario, para avisar de ello al usuario
            return render(request,'agregar_producto.html', {'form': form, 'error_message': '¡El formulario no es válido! Por favor, revise los datos ingresados.'})
    else:
        form = ProductoForm();
    return render(request, 'agregar_producto.html', {'form': form});

@csrf_protect
def agregar_proveedor(request): 
     if request.method == 'POST':
          form = ProveedorForm(request.POST)
          if form.is_valid():
               form.save()  
               return redirect('listar_proveedores') ##aca podemos ponerlo en listar:productos en caso que necesitemos cambiar la vista donde lo mandamos
     else:
         form = ProveedorForm();
     return render(request, 'agregar_proveedor.html', {'form': form});
 
 
 ##CSRF es un ataque que explota la confianza entre un navegador y un sitio web al aprovechar las sesiones activas del usuario en múltiples sitios. Las protecciones contra CSRF son importantes para garantizar la seguridad de las aplicaciones web.