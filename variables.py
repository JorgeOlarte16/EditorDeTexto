import re

txt = "SI 3 MENOR 5 Y 4 MAYOR 3 ENTONCES a SINO FSINO FSI"
I = r'ENTERO'
X = r'[a-z][a-z0-9]+'
E = r'='
Y = r'-?[0-9]+'
W = r','


P= r'ENTERO ([a-z][a-z0-9]+(=(-?[0-9]+|[a-z][a-z0-9]+))?)(,[a-z][a-z0-9]+(=(-?[0-9]+|[a-z][a-z0-9]+))?)*'
C= r'(SI ((([a-z0-9]+ (MENOR|MAYOR|IGUAL|MAYORI|MENORI|DIFERENTE) [a-z0-9]) (((Y|O|NO) [a-z0-9]+) (MENOR|MAYOR|IGUAL|MAYORI|MENORI|DIFERENTE) [a-z0-9]+)+)|TRUE|FALSE) ENTONCES (.*) (SINO(.*)(FSINO)|(FSI)) FSI)'
#P = I(X(E(Y|X))?)(WX(E(Y|X))?)

#x = re.search(C, txt)

#print(x)


texto = "ENTERO a=-9 "

x = texto.split("\n")

print(x)

regex_Patterns = [r'ENTERO ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*',
                  r'REAL ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*',
                  r'BOOLEANO ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*'
                ]

for linea in x:
    for pattern in regex_Patterns:
        a = re.search(pattern, linea)
        if (a != None):
            break

    if(a == None):
        b = re.search(linea, texto)
        break

print(a)
"""
 regex_Patterns = [r'ENTERO ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*',
                  r'REAL ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*',
                  r'BOOLEANO ([a-z][a-z0-9]*(=(-?[0-9]+|[a-z][a-z0-9]*))?)(, [a-z][a-z0-9]*(= (-?[0-9]+|[a-z][a-z0-9]*))?)*'
                ]
        if x[0]!="INICIO":
            print("No inicia")
            return "No inicia"
        
        elif x[len(x)-1]!="FINAL":
            print("No finaliza")
            return "No finaliza"

        x.pop(0)
        x.pop(len(x)-1)

        for linea in x:
            for pattern in regex_Patterns:
                a = re.search(pattern, linea)
                if (a != None):
                    print(a)
                    break

            if(a == None):
                b = re.search(linea, texto)
                break
"""