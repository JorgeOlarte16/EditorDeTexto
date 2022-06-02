from cgitb import enable
from faulthandler import disable
from tkinter import *
from collections import deque
from tkinter.filedialog import askopenfile, asksaveasfile
import re
 

class Window:
    def __init__(self, master):
        self.master = master
        self.master.option_add("*Font", "Verdana 12")
        
 
        self.Main = Frame(self.master)
 
        self.stack = deque(maxlen = 10)  #Creacion y configuracion de la ventana del editor
        self.stackcursor = 0
 
        self.L1 = Label(self.Main, text = "EDITOR DE TEXTO")
        self.L1.pack(padx = 5, pady = 5)
 
        self.T1 = Text(self.Main, width = 90, height = 25)
        self.T2 = Text(self.Main, width = 90, height = 10, state='disable')
        #---------
 
        
        self.T1.tag_configure("red", foreground = "red", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("orange", foreground = "orange", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("blue", foreground = "blue", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("purple", foreground = "purple", font = ("Verdana", "12", "bold"))  #Configuracion de las etiquetas que permiten
        self.T1.tag_configure("green", foreground = "green", font = ("Verdana", "12", "bold"))    #resaltar las palabras reservadas
        self.T1.tag_configure("gold", foreground = "gold", font = ("Verdana", "12", "bold"))
        self.T1.tag_configure("brown", foreground = "brown", font = ("Verdana", "12", "bold"))
        
 
        self.tags = ["orange", "blue", "purple", "green", "red", "gold", "brown"]
 
        self.wordlist = [ ["RETORNA", "FINSI", "SI", "SINO","ENTONCES", "SEGUN", "CASO", "ROMPER", "HAS", "MIENTRAS", "PARA", "FMIENTRAS", "FHAZ", "FPARA", "IMPRIMIR", "LEER"],
                          ["ENTERO", "CARACTER", "REAL", "BOOLEANO"],
                          ["INICIO", "FINAL"],                          #Conjuntos de las palabras reservadas
                          ["VERDADERO", "FALSO"],
                          ["Y", "O", "NO", "MAYOR", "MENOR", "IGUAL", "MAYORI", "MENORI", "DIFERENTE",]]
 
        self.T1.bind("<Return>", lambda event: self.indent(event.widget))
         
        self.T1.pack(side=TOP,padx = 5, pady = 5)
        self.T2.pack(side=BOTTOM,padx = 5, pady = 5)
 
        #---------
 
        self.menu = Menu(self.Main)
        self.menu.add_command(label = "Abrir", command = self.print_stack)
        self.menu.add_command(label = "Deshacer", command = self.undo)          
        self.menu.add_command(label = "Rehacer", command = self.redo)
 
        self.master.config(menu = self.menu)
 
        self.B1 = Button(self.Main, text = "Guardar", width = 8, command = self.save)
        self.B1.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B2 = Button(self.Main, text = "Limpiar", width = 8, command = self.clear)
        self.B2.pack(padx = 5, pady = 5, side = LEFT)
                                                                                        #Creacion de los botones que realizan algunas
        self.B3 = Button(self.Main, text = "Deshacer", width = 8, command = self.undo)  #de las funciones del editor
        self.B3.pack(padx = 5, pady = 5, side = LEFT)
 
        self.B4 = Button(self.Main, text = "Rehacer", width = 8, command = self.redo)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)

        self.B4 = Button(self.Main, text = "Verificar", width = 8, command = self.verificar)
        self.B4.pack(padx = 5, pady = 5, side = LEFT)
 
        self.Main.pack(padx = 5, pady = 5)
 
    def verificar(self):      
        self.T2.configure(state='normal')                
        texto1 = self.T1.get("1.0", "end")   
        x = texto1.split("\n")
        x.pop(len(x)-1)
        self.T2.delete("1.0","end")
        print(x)

        inicio = x[0].replace(" ", "")

        while (x[len(x)-1] == ""):
            x.pop(len(x)-1)

        final = x[len(x)-1].replace(" ", "")

        if inicio !="INICIO":                               #Funcion que se encargara de verificar que el texto ingresado
            print("No inicia")                              #este correcto mediante los automatas diseñados y programados
                                                            #por los otros grupos                                   
            self.T2.insert(INSERT, "\nNo inicia")             
            self.T2.configure(state='disable') 
            return "No inicia"      

        elif final !="FINAL":
            print("No finaliza")
            self.T2.insert(INSERT, "\nNo finaliza")
            self.T2.configure(state='disable')              
            return "No finaliza"

        x.pop(0)
        x.pop(len(x)-1)
        
        
    
    def tagHighlight(self):
        start = "1.0"                   #Funcion que se encarga de identificar las palabras
        end = "end"                     #reservadas y resaltarlas segun las etiquetas previamente
                                        #definidas
        for mylist in self.wordlist:
            num = int(self.wordlist.index(mylist))
 
            for word in mylist:
                self.T1.mark_set("matchStart", start)
                self.T1.mark_set("matchEnd", start)
                self.T1.mark_set("SearchLimit", end)
 
                mycount = IntVar()
                 
                while True:
                    index= self.T1.search(word,"matchEnd","SearchLimit", count=mycount, regexp = False)
 
                    if index == "": break
                    if mycount.get() == 0: break
 
                    self.T1.mark_set("matchStart", index)
                    self.T1.mark_set("matchEnd", "%s+%sc" % (index, mycount.get()))
 
                    preIndex = "%s-%sc" % (index, 1)
                    postIndex = "%s+%sc" % (index, mycount.get())
                     
                    if self.check(index, preIndex, postIndex):
                        self.T1.tag_add(self.tags[num], "matchStart", "matchEnd")
                         
 
    def check(self, index, pre, post):
        letters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        letters2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                   "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        if self.T1.get(pre) == self.T1.get(index):
            pre = index
        else:
            if self.T1.get(pre) in letters1:
                return 0
            elif self.T1.get(pre) in letters2:    #Funcion que se encarga de validar las letras
                return 0                          #en una cadena para evitar resaltar palabras 
        if self.T1.get(post) in letters1:         #que contienen palabras reservadas
            return 0
        elif self.T1.get(post) in letters2:
            return 0
        return 1
 
 
    def scan(self):
        start = "1.0"
        end = "end"
        mycount = IntVar()
                                            #Funcion para resaltar comentarios y cadenas
        regex_patterns = [r'".*"', r'#.*']  #mediante expresiones regulares
 
        for pattern in regex_patterns:
            self.T1.mark_set("start", start)
            self.T1.mark_set("end", end)
 
            num = int(regex_patterns.index(pattern))
 
            while True:
                index = self.T1.search(pattern, "start", "end", count=mycount, regexp = True)
 
                if index == "": break
 
                if (num == 1):
                    self.T1.tag_add(self.tags[5], index, index + " lineend")
                elif (num == 0):
                    self.T1.tag_add(self.tags[6], index, "%s+%sc" % (index, mycount.get()))
 
                self.T1.mark_set("start", "%s+%sc" % (index, mycount.get()))
 
 
    def indent(self, widget):       
 
        index1 = widget.index("insert")      #Funcion que permite separar bloques de codigo
        index2 = "%s-%sc" % (index1, 1)      #mediante indentado
        prevIndex = widget.get(index2, index1)
 
        prevIndentLine = widget.index(index1 + "linestart")
        print("prevIndentLine ",prevIndentLine)
        prevIndent = self.getIndex(prevIndentLine)
        print("prevIndent ", prevIndent)
 
 
        if prevIndex == ":":
            widget.insert("insert", "\n" + "     ")
            widget.mark_set("insert", "insert + 1 line + 5char")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "     ")
                widget.mark_set("insert", "insert + 5 chars")
                prevIndentLine += "+5c"
            return "break"
         
        elif prevIndent != prevIndentLine:
            widget.insert("insert", "\n")
            widget.mark_set("insert", "insert + 1 line")
 
            while widget.compare(prevIndent, ">", prevIndentLine):
                widget.insert("insert", "     ")
                widget.mark_set("insert", "insert + 5 chars")
                prevIndentLine += "+5c"
            return "break"
 
 
    def getIndex(self, index):
        while True:
            if self.T1.get(index) == " ":       #Funcion directamente relacionada a la anterior
                index = "%s+%sc" % (index, 1)   #que permite obtener la ubicacion del ultimo indentado
            else:                               
                return self.T1.index(index)
            
                    
    def update(self):
        self.stackify()
        self.tagHighlight()     #Funcion que contiene las 3 funciones que
        self.scan()             #permiten la actualizacion del texto segun se 
                                #ingresa
    def save(self):
                                #Funcion que se encarga de guardar el texto en txt.
        files = [('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
        f = open(file.name, "a")                
        f.write(self.T1.get("1.0", "end"))   
 
    def clear(self):            #Funcion para borrar todo el texto
        self.T1.delete("1.0", "end")
 
    def stackify(self):                                     #Funcion que guarda los ultimos cambios 
        self.stack.append(self.T1.get("1.0", "end - 1c"))   #aplicados al texto 
        if self.stackcursor < 9: self.stackcursor += 1
 
    def undo(self):
        if self.stackcursor != 0:       #Funcion la cual mediante los cambios almacenados
            self.clear()                #por la funcion anterior deshace lo ultimo que se agrego
            if self.stackcursor > 0: self.stackcursor -= 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def redo(self):                                 
        if len(self.stack) > self.stackcursor + 1:  #Funcion la cual mediante los cambios almacenados
            self.clear()                            #por la funcion anterior rehace lo ultimo que se elimino
            if self.stackcursor < 9: self.stackcursor += 1
            self.T1.insert("0.0", self.stack[self.stackcursor])
 
    def print_stack(self):  #Funcion de prueba para mostrar el funcionamiento
        filename = askopenfile(mode='r', filetypes=[('Texto', '*.txt')])

        if filename == None:
            return 0

        self.T1.delete("0.0", END)
        f = open(filename.name, "r")
        text = f.read()
        self.T1.insert("0.0", text)
        self.update()

root = Tk()
window = Window(root)
root.bind("<Key>", lambda event: window.update())
root.mainloop()