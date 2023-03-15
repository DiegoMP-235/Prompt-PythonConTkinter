from tkinter import Toplevel,Label,Entry,Button

class Prompt:
    
    def __init__(self,NodoPadre,TituloVentana,LabelTitulo,TextButton):
        self.__NodoPadre = NodoPadre
        self.__ventana = self.__creaVentana(TituloVentana)
        self.__LabelTitle = self.__creaLabel(LabelTitulo)
        self.__CajaTexto = self.__creaCajaTexto()
        self.__BotonGuardar = self.__creaBoton(TextButton)
        self.__value = ""
        
        
    def __creaVentana(self,TituloVentana):
        ventana = Toplevel(self.__NodoPadre)
        ventana.title(TituloVentana)
        ventana.geometry("240x100")  
        ventana.resizable(False,False)
        return ventana
    
    def __creaLabel(self,LabelTitulo):
        etiqueta = Label(self.__ventana,text=LabelTitulo)
        etiqueta.pack()
    
    def __creaCajaTexto(self):
        cajaTexto = Entry(self.__ventana)
        cajaTexto.pack()
        return cajaTexto
    
    def __creaBoton(self,textoBtn):
        Boton = Button(self.__ventana,text=textoBtn,command=self.guardaTexto)
        Boton.pack(pady=5)
        
    def guardaTexto(self):
        self.__value = self.__CajaTexto.get()
        self.cierraPrompt()    
    
    def cierraPrompt(self):
        self.__ventana.destroy()
        
    def getValue(self):
        return self.__value    
    
    def getVentana(self):
        return self.__ventana