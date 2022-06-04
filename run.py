from funcion import *
from llamado import *
from asignar import *
from operacion import *

def run(lineas):
    cont=0
    for x in lineas:
        
        if(funciones(x) != "Syntax Error f"):
            mostrar_funcion(x)
            cont = cont + 1
        elif(asig(x) != "Syntax Error a"):
            mostrar_asignar(x)
            cont = cont + 1
        elif(llamado(x) != "Syntax Error l"):
            mostrar_llamado(x)
            cont = cont + 1
            ##if(linea_error_l(x) == x):
            ##    print("El error está en la linea: " +x.index)
        elif(operacion(x) != "Syntax Error o"):
            mostrar_operacion(x)
            cont = cont + 1
        else:
            ##print("SYNTAX ERROR")
            print("El error está en la linea #",cont+1)
            cont = cont + 1



