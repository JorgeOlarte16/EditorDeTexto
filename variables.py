# -*- coding: utf-8 -*-
"""automatasNelson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13NiUxd19DSJcvptkVI-hlR-ukpZXD2jU
"""

#MAIN DE VARIABLES
#VALIDACION DE TIPOS DE DATOS
import re

def lee_entero(vint): #VALIDAR TIPO DE DATO ENTERO
       try:
           vint = int(vint)
           return True
       except ValueError or TypeError:
           return False 

def error_entero_variables(evaluar): #FUNCION PARA EVALUAR SI UNA CADENA ES VARIABLE NUMERICA
  remplace = re.compile('ENTERO|REAL|CARACTER|BOOLEANO')
  sinesp= re.compile('\s') #COMPILAMOS LA ER ESPACIOS PARA CAMBIARLOS
  cadsinesp=sinesp.sub('',evaluar) # CAMBIAMOS LOS ESPACIOS POR NADA
  sintipo=remplace.sub('',cadsinesp) # TAMBIEN ELIMINAMOS LA PALABRA RESERVADA PARA EL TIPO DE DATOS
  descompone=sintipo.split(',') # SEPARAMOS LA CADENA RESTANTE CON LAS COMAS (,)
  quitard=re.compile('[^\d,]')
  solovar= list()
  cont=0
  for i in descompone: # RECORRE EL VECTOR DE CADENAS DIVIDIDAS
    if(i.find(r'=')): # SI EN UNA ENCUENTRA UN "="
      iwal=i.split('=') # DIVIDE LA CADENA 
      solovar.append(iwal[0]) #AGREGAMOS LA POSICION [0] QUE ES EN LA CADENA LA VARIABLE a la lista solovar
    else:
      solovar.append(i) #AGREGAMOS LA CADENA DIRECTAMENT YA QUE NO TIENE ASIGNACION

  for i in solovar: #RECORREMOS LA LISTA DE SOLO VARIABLES
    if(lee_entero(i)): #SI LA VARIABLE ES UN NUMERO
      print("Error de variables numericas")
      return True

  return False

def automatas_Variables(texto):
  lineaV=0
  for i in texto:
    
    if (re.match(r'^ENTERO\s[a-zA-Z0-9]+\s*(\s*=-?([a-zA-Z0-9]+|[0-9]+))?\s?(\s*,\s*[a-zA-Z0-9]+\s*(\s*=-?([a-zA-Z0-9]+|[0-9]+))?\s?)*$',i,flags=re.MULTILINE)):
      #print("DECLARACION ENTERO") #VARIABLE ENTERO
      if(error_entero_variables(i)):
        return ["Error en la linea {}".format(lineaV+1),lineaV]
      else:
        remplace = re.compile('ENTERO')
        texto[lineaV]=remplace.sub('int',i)+';'
        
        lineaV=lineaV+1
    elif(re.match(r'^REAL\s*[A-Za-z0-9_]+\s*(\s*=\s*-?([A-Za-z0-9_]+|[0-9]+(\.[0-9]+)?))?\s*(\s*,\s*[a-zA-Z0-9]+\s*(=\s*-?([A-Za-z0-9_]+|[0-9](\.[0-9]+)?))?)*\s*$',i,flags=re.MULTILINE)):
      #print ('DECLARACION REAL') #VARIABLE REAL
      if(error_entero_variables(i)):
        return ["Error en la linea {}".format(lineaV+1),lineaV]
         
      else:
        remplace = re.compile('REAL')
        texto[lineaV]=remplace.sub('float',i)+';'
        
        lineaV=lineaV+1
    elif(re.match(r'^CARACTER\s[a-zA-Z0-9]+\s*(=\s*((".+")))?\s*(\s*,\s*[a-zA-Z0-9]+\s*(=\s*((".+")))?\s*)?\s*$',i,flags=re.MULTILINE)):
      #print ('DECLARACION CARACTER') #VARIABLE CARACTER
      if(error_entero_variables(i)):
        return ["Error en la linea {}".format(lineaV+1),lineaV]
      else:
        remplace=re.compile('CARACTER') #COMPILAMOS LA ER CARACTER PARA CAMBIARLA
        sinesp= re.compile('\s') #COMPILAMOS LA ER ESPACIOS PARA CAMBIARLOS
        cadsinesp=sinesp.sub('',i) # CAMBIAMOS LOS ESPACIOS POR NADA
        sinchar=remplace.sub('',cadsinesp) # TAMBIEN ELIMINAMOS LA PALABRA CARACTER
        variables=sinchar.split(',') # SEPARAMOS LA CADENA RESTANTE CON LAS COMAS (,)
        cadenaenc='char ' # AGREGAMOS A LA CADENA EN C char PARA EMPEZAR CON LA DECLARACION DE VARIABLE
        cont =0 # CONTADOR PARA EL NUMERO DE ITEMS DE LA LISTA CREADA CUANDO SE SEPARO LA CADENA POR LAS COMAS
        cont2= 0 # CONTADOR PARA LLEVAR LA CUENTA EN EL FOR 
        for i in variables: #FOR PARA CONTAR NUMERO DE ITEMS DE LA CADENA DIVIDIDA
          cont=cont+1
        for i in variables: #FOR PARA LLENAR LA CADENA EN C
          cont2=cont2+1
          if(cont2<cont):
            cadenaenc=cadenaenc+'*{va},'.format(va=i) # CONCATENA LA CADENA EN C CON * Y LA VARIABLE CON SU ASIGNACION Y UNA COMA PARA LA SIGUIENTE VARIABLE
          else:
            cadenaenc=cadenaenc+'*{va};'.format(va=i) # PARA ESTO ERAN LOS CONTADORES, UNA VEZ LLEGADO AL FINAL DE LAS VARIABLES SE LE AGREGA UN (;) EN VEZ DE LA COMA (,)
        texto[lineaV]=cadenaenc #CADENA EN C RESULTANTE DE TODO EL DESASTRE DE ARRIBA
        
        lineaV=lineaV+1
    elif(re.match(r'^BOOLEANO\s[a-zA-Z0-9]+\s*((=\s*(VERDADERO|FALSO))|\s*)\s*(\s*,\s*[a-zA-Z0-9]+\s*((=\s*(VERDADERO|FALSO))|\s*)\s*)*\s*$',i,flags=re.MULTILINE)):
      #print ('DECLARACION BOOLEANO') #VARIABLE BOOLEANO
      if(error_entero_variables(i)):
        return ["Error en la linea {}".format(lineaV+1),lineaV]
      else:
        remplace = re.compile('BOOLEANO') # COMPILAMOS LA ER BOOLEANO PARA REEMPLAZARLA
        verdad=re.compile('VERDADERO') # COMPILAMOS LA ER VERDADERO PARA  REEMPLAZARLA
        mentira= re.compile('FALSO') # COMPILAMOS LA ER FALSO PARA REEMPLAZARLA
        cadenaenc=remplace.sub('bool',i)  # SE REEMPLAZA "BOOL" EN LOS "BOOLEANOS" USANDO COMO CADENA BASE LA CADENA ORIGINAL
        cadenaenc=verdad.sub('true',cadenaenc) # SE REEMPLAZA "TRUE" EN LOS "VERDADERO" USANDO COMO CADENA BASE LA CADENA EN C
        cadenaenc=mentira.sub('false',cadenaenc)+';' # SE REEMPLAZA "FALSE" EN LOS "FALSO" USANDO COMO CADENA BASE LA CADENA EN C Y CONCATENAMOS EL (;)
        texto[lineaV]=cadenaenc # CADENA EN C RESULTANTE DE TODO ESTE DESMADRE
        
        lineaV=lineaV+1
#===========================================================#VECTORES#=======================================================================
    elif(re.match(r'^ENTERO\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*((=\s*({\s*[0-9]+(,[0-9]+)*})\s*)|\s*)\s*$',i,flags=re.MULTILINE)):
      #print("DECLARACION VECTOR ENTERO") #VECTOR ENTERO
      remplace = re.compile('ENTERO')
      texto[lineaV]=remplace.sub('int',i)+';'
      
      lineaV=lineaV+1
    elif(re.match(r'^REAL\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*((=\s*({\s*([a-zA-Z0-9]+|[0-9](\.[0-9]+)?)(,([a-zA-Z0-9]+|[0-9](\.[0-9]+)?))*})\s*)|\s*)\s*$',i,flags=re.MULTILINE)):
      #print('DECLARACION VECTOR REAL') #VECTOR REAL
      remplace = re.compile('REAL')
      texto[lineaV]=remplace.sub('float',i)+';'
      
      lineaV=lineaV+1
    elif(re.match(r'^CARACTER\s*[a-zA-Z0-9_]+\s*\[\s*([a-zA-Z0-9_])\s*\]\s*((=\s*({\s*"."\s*(,\s*"\s*.\s*"\s*)*\s*}))|\s*)$',i,flags=re.MULTILINE)):
      #print('DECLARACION VECTOR CARACTER') #VECTOR CARACTER
      remplace = re.compile('CARACTER')
      texto[lineaV]=remplace.sub('char',i)+';'
      
      lineaV=lineaV+1
    elif(re.match(r'^BOOLEANO\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*((=\s*({\s*(VERDADERO|FALSO)(\s*,\s*((VERDADERO)|(FALSO))\s*)*})))\s*$',i,flags=re.MULTILINE)):
      #print('DECLARACION VECTOR BOOLEANO') #VECTOR BOOLEANO
      remplace = re.compile('BOOLEANO')
      texto[lineaV]=remplace.sub('bool',i)+';'
      
      lineaV=lineaV+1
    #==================================================================#--- MATRICES ---#==================================================================
    elif(re.match(r'^ENTERO\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*\[[a-zA-Z0-9]\]((=\s*({\s*[0-9]+(,[0-9]+)*})\s*({\s*[0-9]+(,[0-9]+)*}))|\s*)\s*$',i,flags=re.MULTILINE)):
      #print('DECLARACION MATRIZ ENTERO') #MATRIZ ENTERO
      remplace = re.compile('ENTERO') 
      texto[lineaV]=remplace.sub('int',i)+';'
      
      lineaV=lineaV+1

    elif(re.match(r'^REAL\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*\[[a-zA-Z0-9]\]\s*((=\s*({\s*([a-zA-Z0-9]+|[0-9](\.[0-9]+)?)(,([a-zA-Z0-9]+|[0-9](\.[0-9]+)?))*})\s*({\s*([a-zA-Z0-9]+|[0-9](\.[0-9]+)?)(,([a-zA-Z0-9]+|[0-9](\.[0-9]+)?))*})\s*)|\s*)\s*$',i,flags=re.MULTILINE)):
      #print('DECLARACION MATRIZ REAL') #MATRIZ REAL
      remplace = re.compile('REAL') 
      texto[lineaV]=remplace.sub('float',i)+';'
      
      lineaV=lineaV+1

    elif(re.match(r'^CARACTER\s*[a-zA-Z0-9_]+\s*\[\s*([a-zA-Z0-9_])\s*\]\s*\[\s*([a-zA-Z0-9_])\s*\]\s*((=\s*({\s*"."\s*(,\s*"\s*.\s*"\s*)*\s*}))\s({\s*"."\s*(,\s*"\s*.\s*"\s*)*\s*})|\s*)$',i,flags=re.MULTILINE)):
      #print('DECLARACION MATRIZ CARACTER') #MATRIZ CARACTER
      remplace = re.compile('CARACTER') 
      texto[lineaV]=remplace.sub('chat',i)+';'
      
      lineaV=lineaV+1

    elif(re.match(r'^BOOLEANO\s[a-zA-Z0-9]+\s*\[[a-zA-Z0-9]\]\s*\[[a-zA-Z0-9]\]\s*((=\s*({\s*(VERDADERO|FALSO)(\s*,\s*((VERDADERO)|(FALSO))\s*))*}\s*({\s*(VERDADERO|FALSO)(\s*,\s*((VERDADERO)|(FALSO))\s*)*})))\s*$',i,flags=re.MULTILINE)):
      #print('DECLARACION MATRIZ BOOLEANO') #MATRIZ BOOLEANA
      remplace = re.compile('BOOLEANO') 
      texto[lineaV]=remplace.sub('bool',i)+';'
    
      lineaV=lineaV+1

#=================================================================# LINEAS SALTABLES (DECLARACION DE FUNCION) #==================================================================

    elif(re.match(r'^(ENTERO|REAL|CARACTER|BOOLEANO)\s*\w+\s*\(\s*\w*(\s*,\w+)*\s*\)\s*',i,flags=re.MULTILINE)):
      print('FUNCION') #ME SALTO ESTA LINEA PORQUE SON FUNCIONES
      
      lineaV=lineaV+1
#=================================================================# ERROR EN DECLARACION #==================================================================
    elif(re.match(r'^(ENTERO|REAL|CARACTER|BOOLEANO)',i)):
      """print('DECLARACION CON ERROR') #ERROR"""
      
      return ["Error en la linea {}".format(lineaV+2),lineaV+2]
#=================================================================# LINEAS X SALTABLES #==================================================================
    else:
      #print("Linea X que me salto")
      #print(lineaV)
      lineaV=lineaV+1
#=================================================================# RETORNA # ============================================================================
  return texto

#Pruebas
text=list()
