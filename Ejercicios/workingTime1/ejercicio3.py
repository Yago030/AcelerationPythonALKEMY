def promedio (a, b , c):
        nota = (a + (b+c))/3;
        if (nota >= 6) :
            return "El alumno esta aprobado";
        else:
            return "Reprobado";
    


print ("Resultado FINAL: "+ promedio(3,6,7));