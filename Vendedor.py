import tkinter as tk
from tkinter import Frame,Label,Button
class Vendedor:
    def __init__(self):
        print("se ha pulsado el boton vender")

    def VentanaNueva2(self):
        def vuelvo():
            root3.destroy()
        print("quiero vender")
        root3=tk.Tk()
        root3.title("VENDEDOR")

#---------------------------creacion del marco---------------------------#

        marco = Frame(root3)
        marco.pack(side="top",fill="x")
        marco.config(bg="blue",width=800,height=800)

#---------------------------creacion ventana---------------------------#

        ventana_ppal3 =Label(marco,text="BIENVENIDO VENDEDOR",font=("Comic Sans MS",40),fg="GREEN")
        ventana_ppal3.place(x=500,y=0)

#---------------------------creacion boton---------------------------#

        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)
        boton1.place(x=250,y=250)

        root3.mainloop()

