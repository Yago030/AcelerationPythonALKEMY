class Bicicleta:
    
        def __init__(self, rodado, marca, color, accesorioss=False, usada=False):
            self.rodado = rodado;
            self.marca = marca;
            self.color = color;
            self.accesorioss = accesorioss;
            self.usada = usada;
            
        def accesorios(self):
             if self.accesorios:
                     return f'La bicicleta de marca {self.marca} lleva accesorios.'
             else:
                      return f'La bicicleta de marca {self.marca} No lleva accesorios.'



        def tipo_de_bici(self):
            if self.rodado >= 26:
                return f'La bicicleta es ideal para largos tramos';
            else:
                return f'La bicicleta es No is ideal para largos viajes';
            
        
        def posible_cambio(self):
            if self.usada == True:
                return f'La bicicleta NO tiene cambio'
            else:
                return f' La bici Si tiene cambio'
            


mi_super_bic = Bicicleta(29, "Venzo", "Red", False, False);

print (mi_super_bic.accesorios());
print (mi_super_bic.posible_cambio());
print (mi_super_bic.tipo_de_bici())