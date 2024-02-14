def sumar():
    a = int(input("Ingresa el primer numero a sumar por favor "));
    b = int(input("Ingresa el segundo numero a sumar por favor "));
    suma = a +b;
    return f'La suma de  {a} + {b} es {suma} ';


def multiplicar():
     a = int (input("Ingresa el primer numero a multiplicar por favor "));
     b = int(input("Ingresa el segundo numero a multiplicar por favor "));
     multiplicar = a * b;
     return f'La multiplicacion  de  {a} * {b} es {multiplicar} ';
     
def operar(opcion):
    if (opcion == '1'):
       return sumar();
    elif (opcion =='2'):
       return  multiplicar();

print("Procedemos a operar con funciones, acvtividad 1")
opcion = input("Por favor ingresa ** 1 ** para sumar || ** 2 ** para multiplicar ");

if opcion not in ['1', '2']:
    print ("Has ingresado un valor invalido, debes ingresar entre 1 o 2");
    while opcion not in ['1', '2']:
        opcion = input("Por favor ingresa ** 1 ** para sumar || ** 2 ** para multiplicar ");
else:
    print ( f' Has ingresado la opcion de {opcion}', operar(opcion));
    