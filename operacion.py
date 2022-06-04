import re

##leer = input("fun: ")

def operacion(cadena):
    operacion = r'(([a-zA-Z]+[a-zA-Z0-9_]*[ ]*[=])|((RETORNA)[ ]*))([ ]*(([a-zA-Z]+[a-zA-Z0-9_]*)|([0-9]+)))(([ ]*[-+*/%])([ ]*(([a-zA-Z]+[a-zA-Z0-9_]*)|([0-9]+))))+' 
    ## no tenemos parentesis porque requieren "automatas" de pila (se necesitaría memoria)
    resul = ""
    if(re.search(operacion, cadena)):
        c = cadena.split()
        ##print(c)
        for x in c:
            if(x == "RETORNA"):
                resul = resul + " "+"RETURN"
            else:
                resul = resul + " "+x
                
        resul = resul +";" 

        ##print(resul) 
        return resul
    else:
        return "Syntax Error o"

def mostrar_operacion(cadena):
    print(operacion(cadena))
