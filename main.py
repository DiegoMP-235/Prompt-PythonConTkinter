from tkinter import *
from Prompt import *

def muestraPrompt():
    myPrompt = Prompt(ventana,"Mi prompt","Ingresa tu valor","Guardar")
    myPrompt.esperarVentana()
    Valor_ingresado = myPrompt.getValue()
    print("El valor ingresado:"+Valor_ingresado)
ventana = Tk()
ventana.title("Mi ventana principal")
ventana.geometry("350x350")

myButton = Button(ventana,text="Abrir Prompt",command=muestraPrompt)
myButton.pack()

ventana.mainloop()