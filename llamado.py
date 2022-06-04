import re

##leer = input("fun: ")
##def linea_error_l(cadena):
  ##  if(llamado(cadena) == "Syntax Error l"):
   ##     return cadena

def llamado(cadena):
    exp = r'([a-zA-Z]+[a-zA-Z0-9_]*)[(]([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*[ ]*[)]'


    ##exp = r'([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)[(][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*[ ]*[)]'


    aux = cadena.split()
    
    resultado= ""
    ##print(aux)

    
    noerror = 0
    if(re.search(exp,cadena)):
        noerror = 1
    else:
        noerror = 2
        


    n=0
    
    if(noerror == 1):
        for x in aux:
            if(re.search(r'[a-zA-Z]+[a-zA-Z0-9_]*',x)):


                palabra = aux[n]
                letra = palabra[-1]

                if(letra != ")"):
                    if(aux[n+1] == "(" or aux[n+1] == ")"):
                        resultado = resultado + " " + x
                    else:
                        resultado = resultado + " "+x+","
                else:
                    resultado = resultado + " " + x



            elif(x == "("):
                 resultado = resultado + x
            elif(x == ")"):
                resultado = resultado + x
                    


            n = n+1
        return resultado + ";"
    else:
        return "Syntax Error l"


def mostrar_llamado(cadena):
    print(llamado(cadena))


