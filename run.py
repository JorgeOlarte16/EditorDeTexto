from funcion import *
from llamado import *
from asignar import *
from operacion import *

def run(copia):
    cont=0
    traduccion = []
    for x in copia:
        
        if(funciones(x) != "Syntax Error f"):
            traduccion.append(funciones(x))
            cont = cont + 1
        elif(asig(x) != "Syntax Error a"):
            traduccion.append(asig(x))
            cont = cont + 1
        elif(llamado(x) != "Syntax Error l"):
            traduccion.append(llamado(x))
            cont = cont + 1
            ##if(linea_error_l(x) == x):
            ##    print("El error está en la linea: " +x.index)
        elif(operacion(x) != "Syntax Error o"):
            traduccion.append(operacion(x))
            cont = cont + 1
        else:
            ##print("SYNTAX ERROR")
            traduccion.append(x)
            cont = cont + 1
    
    
    return(traduccion)


#run("text.txt")

