# -*- coding: utf-8 -*-
"""CONDICIONALES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tnSsAM0ztDHzf1d_Yc6rjULcOiywarNB

#DEFINICION DE PALABRAS RESERVADOS Y EQUIVALENCIA EN C PARA SU COMPILACION
"""

import re

RESERVED_WORDS_SI = ['SI','ENTONCES','PROGRAMA','SINO','FSINO','FSI']
RESERVED_WORDS_SEGUN = ['SEGUN','HACER','CASO','PROGRAMA','DEOTROMODO','FSEGUN']
X = re.compile(r'[a-zA-Z]+|((-|)([0]|[1-9][0-9]*)(\.[0-9]+)*)')
all_var_name = re.compile(r'^[a-zA-Z][\w-]*')

Y = ['&&','||']
COMP = ['>','<','>=','<=','!=', '==', '!']

TRADUCIR = {
    'SI': 'if(',
    'ENTONCES': '){\n',
    'FSI': '\n}',
    'SINO': '\n}\nelse{\n',
    'FSINO': '\n}',
    'SEGUN': '\nswitch(',
    'HACER': '){',
    'CASO': '\n\tcase ',
    'DEOTROMODO:': '\n\tdefault: ',
    'FSEGUN': 'break;\n}'
}

def CondicionUnitaria(cadena):
    estado = 1
    iterador = 0
    for i in range(0, len(cadena)):
      # Se asigna una nueva transicion de la cadena por cada paso del for
      transicion = cadena[i]

      if estado == 1:
        if transicion == 'NO':
          estado = 2
        
        elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in RESERVED_WORDS_SEGUN and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
          estado = 3

        else:
          estado = 4

      elif estado == 2:
        if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in RESERVED_WORDS_SEGUN and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
          estado = 3

        else:
          estado = 4
      elif estado == 3:
            if transicion == 'HACER':
              iterador = i
              break
            else:
                estado = 4
      
      elif estado == 4:
        break
      else:
        return False

    if estado == 3:
        return {'aceptacion':'Entra', 'iterador':iterador}
    else:
        return {'aceptacion':'No'}

"""# Funcion Condicion

Valida las condiciones dentro de la ESTRUCTURA SI 
"""

def Condicion(cadena):
  estado = 1
  iterador = 0
  
  for i in range(0, len(cadena)):
    transicion = cadena[i]

    if estado == 1:
          
      if transicion == 'NO':
        estado = 3
      elif transicion == 'VERDADERO' or transicion == 'FALSO':
        estado = 4
      elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP:
        estado = 2
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP:
        estado = 2
          
      else:
          estado = 10

    elif estado == 2:
      if transicion in COMP:
            estado = 3
      elif transicion in Y:
            estado = 6
      elif transicion == 'ENTONCES':
            iterador = i
            break
      else:
            estado = 10

    elif estado == 3:
      if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != 'NO':
        estado = 5
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != 'NO':
        estado = 5
          
      else:
        estado = 10

    elif estado == 4:
      if transicion == 'ENTONCES':
        iterador = i
        break
      else:
        estado = 10
        
    elif estado == 5:
      if transicion in Y:
        estado = 6
      elif transicion == 'ENTONCES':
        iterador = i
        break
      else:
        estado = 10

    elif estado == 6:
      if transicion == 'NO':
        estado = 8
      elif re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
        estado = 7 
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO':
        estado = 7 
      else:
        estado = 10

    elif estado == 7:
      if transicion in Y:
        estado = 6
      elif transicion in COMP:
        estado = 8
      elif transicion == 'ENTONCES':
        iterador = i
        break
      else:
        estado = 10

    elif estado == 8:
      if re.match(all_var_name,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != 'NO':
        estado = 9
      elif re.match(X,transicion) and transicion not in RESERVED_WORDS_SI and transicion not in Y and transicion not in COMP and transicion != 'VERDADERO' and transicion != 'FALSO' and transicion != 'NO':
        estado = 9
      else:
        estado = 10

    elif estado == 9:
      if transicion in Y:
        estado = 6
      elif transicion == 'ENTONCES':
        iterador = i
        break
      else:
        estado = 10

        #ESTADO DE ERROR

    elif estado == 10:
      break
        
    else:
      break
  
  if estado == 2 or estado == 4 or estado == 5 or estado == 7 or estado == 9:
    return {'aceptacion':'Entra', 'iterador':iterador}
  else:
    return {'aceptacion':'No'}

def validarCierre(cierre,inicio,indexLinea,lineas,excepcion=''):
        aux = 1;
        for i in range(indexLinea + 1, len(lineas)):
            linea = lineas[i].strip('\t\n').split(' ')
            if excepcion:
                if excepcion in linea:
                    aux -= 1
            if inicio in linea: aux += 1
            if cierre in linea: aux -= 1
            if aux == 0: return True
        return False

"""#Funcion Validar

Esta recibe un array con las lineas de un archivo de texto, y va validando una por una si contiene un condicional (ya sea SI o SEGUN), valida que su estructura esta bien escrita y lo transforma a lenguaje C

Finalmente retorna una array con las lineas que fueron validadas y transformadas con las que no, mantieniendo su orden
"""

def validarCondicionales(lineas):
    
    #Valida si hay una estructura SI abierta 
    entro_si = False

    # Guarda la cantidad de estructuras SI que se encuentran abiertas
    conteo_si = 0

    # Guarda si hay una estructura SI con SINO abierta
    entro_sino = False

    # Guarda la cantidad de estructuras SI con SINO que se encuentran abiertas
    conteo_sino = 0

    # Guarda si hay una estructura SEGUN abierta
    entro_segun = False

    # Guarda la cantidad de estructuras SEGUN que se encuentran abiertas
    conteo_segun = 0
    RESULT = [True, []]
    # print(lineas)
    for line in lineas:
        
        sentence = line.strip('\t\n').split(' ')
        # print(sentence)
        if 'SI' in sentence:
            
            result = Condicion(sentence[1:])
            entro_si = True
            conteo_si +=1
            if(result['aceptacion'] == 'Entra'):
                pos = line.find('ENTONCES')
                if len(line) >= pos + 5:
                    for idx in range(pos+8, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                # if line.find(' ') != len(line)-1:
                #     RESULT[0] = False
                #     RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])

                if not validarCierre('FSI', 'SI', lineas.index(line), lineas, 'SINO'):
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro la palabra de cierre "FSI": ',lineas.index(line)+1])

                if RESULT[0]:
                
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)   
            else:
                if 'ENTONCES' not in sentence:
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: No se encontro la palabra "ENTONCES" en la linea: ',lineas.index(line)+1])
                else:
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: Condicion mal escrita en la linea: ',lineas.index(line)+1])
                    


        
        elif 'SINO' == sentence[0]:
            if entro_si:

                if len(line) >= 5:
                    for idx in range(5, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                entro_si = False
                entro_sino = True
                conteo_sino += 1

                if not validarCierre('FSINO', 'SINO', lineas.index(line), lineas):
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro la palabra de cierre "FSINO": ',lineas.index(line)+1])

                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    
                    RESULT[1].append(traduccion)

            elif entro_sino:
                RESULT[0] = False
                RESULT[1].append(['ERROR: palabra SINO repetida en la linea: ',lineas.index(line)+1])
    
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SI en la linea: ',lineas.index(line)+1])
                
            
            
            
            
            
        
        elif 'FSINO' == sentence[0]:
            if entro_sino:
                
                if len(line) >= 6:
                    for idx in range(6, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_sino > 0:
                    conteo_sino -= 1

                if conteo_sino == 0:
                   entro_sino = False
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SINO en la linea: ',lineas.index(line)+1])
                
            

        elif 'FSI' == sentence[0]:
            if entro_si:
                
                if len(line) >= 4:
                    for idx in range(4, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_si > 0:
                    conteo_si -= 1

                if conteo_si == 0:
                   entro_si = False

                
            elif entro_sino:
                entro_sino = False
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra FSINO en la linea: ',lineas.index(line)+1])
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SI en la linea: ',lineas.index(line)+1])
                
                   

        elif 'SEGUN' == sentence[0]:
            entro_segun = True
            conteo_segun += 1

            result = CondicionUnitaria(sentence[1:])
            
            if(result['aceptacion'] == 'Entra'):
                pos = line.find('HACER')
                if len(line) >= pos + 5:
                    for idx in range(pos+5, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                            break

                if not validarCierre('FSEGUN', 'SEGUN', lineas.index(line), lineas):
                    RESULT[0] = False
                    RESULT[1].append(['Error: No se encontro palabra de cierre "FSEGUN": ',lineas.index(line)+1])


                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)
            else:
                if 'HACER' not in sentence:
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: No se encontro la palabra "HACER" en la linea: ',lineas.index(line)+1])
                else:
                    if 'HACER' in sentence[1]:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: Condicion a evaluar no escrita: ',lineas.index(line)+1])
                    else:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: Condicion a evaluar mal escrita: ',lineas.index(line)+1])  
                
            

        elif entro_segun and 'CASO' == sentence[0]:
            if entro_segun:


                if len(sentence) == 1:
                    RESULT[0] = False
                    RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])

                elif len(sentence) == 2:

                    if ':' in sentence[1]:
                        if '::' not in sentence[1]:
                            pos = line.find(':')
                            if len(line) >= pos + 1:
                                for idx in range(pos+1, len(line)):
                                    if line[idx] != ' ':
                                        RESULT[0] = False
                                        RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                                        break
                            if RESULT[0]:
                                traduccion = ''
                                for palabra in sentence:
                                    if palabra in TRADUCIR.keys():
                                        traduccion += (TRADUCIR[palabra]+' ')
                                    else:
                                        traduccion += (palabra+' ')

                                RESULT[1].append(traduccion)

                            
                                
                        else:
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: palabra ":" repetida en la linea: ', lineas.index(line)+1])
                    else:
                        RESULT[0] = False
                        RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])
                elif len(sentence) == 3:
                    if ':' not in sentence[1]:
                        if sentence[2] == ':':
                            pos = line.find(':')
                            if len(line) >= pos + 1:
                                for idx in range(pos+1, len(line)):
                                    if line[idx] != ' ':
                                        RESULT[0] = False
                                        RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                                        break
                            if RESULT[0]:
                                traduccion = ''
                                for palabra in sentence:
                                    if palabra in TRADUCIR.keys():
                                        traduccion += (TRADUCIR[palabra]+' ')
                                    else:
                                        traduccion += (palabra+' ')

                                RESULT[1].append(traduccion)
                        
                        

                        else:
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: No se encontro la palabra ":" en la linea: ',lineas.index(line)+1])
                    else:
                        if sentence[2] == ':' or  '::' in sentence[1]:
                            RESULT[0] = False
                            RESULT[1].append(['ERROR: palabra ":" repetida en la linea: ',lineas.index(line)+1])
               
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea: ',lineas.index(line)+1])
            

        elif entro_segun and 'DEOTROMODO:' == sentence[0]:

            if entro_segun:
                pos = line.find(':')
                if len(line) >= pos + 1:
                    for idx in range(pos+1, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                
                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += ('break;\n'+TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')

                    RESULT[1].append(traduccion)
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea: ',lineas.index(line)+1])
                
            

        elif entro_segun and 'FSEGUN' == sentence[0]:

            if entro_segun:
                if len(line) >= 7:
                    for idx in range(7, len(line)):
                        if line[idx] != ' ':
                            RESULT[0] = False
                            RESULT[1].append(['Error: Se debe terminar con salto de linea en la linea: ',lineas.index(line)+1])
                
                if RESULT[0]:
                    traduccion = ''
                    for palabra in sentence:
                        if palabra in TRADUCIR.keys():
                            traduccion += (TRADUCIR[palabra]+' ')
                        else:
                            traduccion += (palabra+' ')
                    RESULT[1].append(traduccion)

                if conteo_segun > 0:
                    conteo_segun -= 1

                if conteo_segun == 0:
                    entro_segun = False
                
            else:
                RESULT[0] = False
                RESULT[1].append(['ERROR: No se encontro la palabra SEGUN en la linea:  ',lineas.index(line)+1])
            
        else:
            if RESULT[0]:
                traduccion = ''
                for palabra in sentence:
                        traduccion += (palabra+' ')

                RESULT[1].append(traduccion)
        
    cambios = 0
    if ' ' in RESULT[1]:
        RESULT[1].remove(' ')

    i = 0
    copiaResultado = RESULT[1].copy()
    while i < len(RESULT[1]):
        if not RESULT[0]:

            if not isinstance(RESULT[1][i], list):
                copiaResultado.remove(RESULT[1][i])
        else:
            if 'case' in RESULT[1][i]:
                cambios += 1

                if cambios > 1:
                    RESULT[1][i] = 'break;\n'+RESULT[1][i]
        i += 1
        
    RESULT[1] = copiaResultado

        



    # print(RESULT)
    return RESULT

"""estructura = open('/content/estructura.txt', 'r')
lineas = estructura.read().split('\n')

r = open('resultado.txt','w')
resultado = validarCondicionales(lineas)
if(resultado[0]):
        r.writelines(resultado[1])
        r.close()
        print('COMPILADO EXITOSAMENTE')
else:
        print(resultado[1])"""