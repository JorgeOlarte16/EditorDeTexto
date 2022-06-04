import re

##leer = input("fun: ")
def asig(cadena):
    
    exp = r'([a-zA-Z]+[a-zA-Z0-9_]*)[=]([a-zA-Z]+[a-zA-Z0-9_]*)[(][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*[)]'
    ##exp = r'([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)[=][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)[(][ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)*[)]'


   

    aux = cadena.split()
    n=0
    resultado= ""
    ##print(aux)
    if(re.search(exp,cadena)):
        for x in aux:
            if(re.search(r'[a-zA-Z]+[a-zA-Z0-9_]*',x)):
                palabra = aux[n]
                letra = palabra[-1]

                if(letra != ")"):
                    if(aux[n+1] == "(" or aux[n+1] == ")" or aux[n+1] == "="):
                        resultado = resultado + " " + x
                        
                    else:
                        resultado = resultado + " "+x+","
                else:
                    resultado = resultado + " " + x

            elif(x == "="):
                resultado = resultado + x
            elif(x == "("):
                resultado = resultado + x
            elif(x == ")"):
                resultado = resultado + x


            n = n+1
        return resultado + ";"
    else:
        return "Syntax Error a"




def mostrar_asignar(cadena):
    print(asig(cadena))
        

