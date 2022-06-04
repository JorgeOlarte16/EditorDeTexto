import re

##leer = input("fun: ")


##fun = r'(FUNCION)[ ]*((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|[ ]*)[ ]*([a-zA-Z]+[a-zA-Z0-9_]*)[(](((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER))[ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)]'
##fun = r'(FUNCION)[ ]*((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|[ ]*)[ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*)[(][ ]*(((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER))[ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)]'
##dic = r'(FUNCION)|(ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)'

def funciones(cadena):
    nombre = r'[a-zA-Z]+[a-zA-Z0-9_]*'
    fun = r'(FUNCION)[ ]*((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|[ ]*)[ ]*([a-zA-Z]+[a-zA-Z0-9_]*)[(](((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER))[ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)][ ]*[a-zA-Z]+[a-zA-Z0-9_]*[ ]*(FINF)'
    ##fun = r'(FUNCION)[ ]*((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER)|[ ]*)[ ]*([a-zA-Z]+[a-zA-Z0-9_]*)[(](((ENTERO)|(REAL)|(BOOLEANO)|(CARACTER))[ ]*([a-zA-Z]+[a-zA-Z0-9_]*[ ]*))*[ ]*[)]'
    resultado = ""
    if(re.search(fun, cadena)):
        aux = cadena.split()
        
        n = 0
        
        ##print(aux)
        flag_name = 0

        for x in aux:


            """for y in aux:
                if(re.search(dic,y)):
                    flag_w = 1"""
            if(x == "FUNCION"):
                resultado = resultado
            elif(x == "FINF"):
                resultado = resultado
            elif(x == "REAL"):
                resultado = resultado+" "+"float"
            elif(x == "BOOLEANO"):
                resultado = resultado+" "+"bool"
            elif(x == "CARACTER"):
                resultado = resultado+" "+"char"
            elif(x == "ENTERO"):
                resultado = resultado+" "+"int"
            elif(re.search(nombre, x)):

                palabra = aux[n]
                letra = palabra[-1]

                ##palabra2 = aux[n]


                if(letra != ")"):
                
                    if(aux[n+1] == "(" or aux[n+1] == ")" or flag_name == 0):
                        flag_name = 1
                        resultado = resultado + " " + x
                    else:
                        ##print("n: ",n)
                        ##print("x: "+x)
                        ##print("aux: " +aux[n+1])
                        resultado = resultado + " "+x+","
                else:
                    resultado = resultado + " " + x
            elif(x == "("):
                resultado = resultado+" "+x
            elif(x == ")"):
                resultado = resultado+" "+x
                
            n = n+1
        
        ##final = fun+" "+nombre+ "FINF"
        return resultado

    else:
        return "Syntax Error f"


##print(funciones(leer))

def mostrar_funcion(cadena):
    print(funciones(cadena))
