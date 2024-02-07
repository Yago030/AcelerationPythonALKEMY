miLista = ["Perro", "Gato", 25, 2.6, "Viento"];


#imprimiendo el ultimo elemento de la lista
ultimoElemento = miLista[-1];
print("El utlimo elemento es : " + str(ultimoElemento));


#modificando el tercer elemento de la lista
miLista[2]= "Vaca";
print("La lista quedaria", miLista);

#agrgando dos elementos
miLista.append("Caballos");
miLista.append("Puma");
print("La lista con los elementos agregados qudaria", miLista);

##eliminado algun elemento
miLista.pop(3);
print("La lista con un elemento quitado  qudaria", miLista);
