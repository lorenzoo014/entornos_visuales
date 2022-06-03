
# import tkinter as tk
from msilib.schema import Font
from tkinter import Tk,GROOVE, Frame,Label,Button,Entry,Canvas,font
class Vendedor:
    def __init__(self):
        print("se ha pulsado el boton vender")

    def VentanaNueva2(self):
        def vuelvo():
            root3.destroy()
        print("quiero vender")
        root3=Tk()
        root3.title("VENDEDOR")


# #---------------------------creacion del canva---------------------------#
        canvas =Canvas(root3, height=380 ,width=400)
        canvas.pack()

# #---------------------------creacion del marco---------------------------#

        marco = Frame()
        '''marco.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)'''
        marco.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
        # marco.config(width=500,height=500,relief=GROOVE)

# #---------------------------creacion ventana---------------------------#

        ventana_ppal3 =Label(marco,text="BIENVENIDO VENDEDOR",font=40,fg="GREEN")
        ventana_ppal3.grid(row=0,column=1)

        ventana1 =Label(marco,text="nombre",fg="GREEN")
        ventana1.grid(row=1,column=0)

        ventana2 =Label(marco,text="apellido",fg="GREEN")
        ventana2.grid(row=2,column=0)

        ventana3 =Label(marco,text="NFT",fg="GREEN")
        ventana3.grid(row=3,column=0)


# #---------------------------creacion entradas---------------------------#
        entrada1 = Entry(marco)
        entrada1.grid(row =1,column=1)

        entrada2 = Entry(marco)
        entrada2.grid(row =2,column=1)

        entrada3 = Entry(marco)
        entrada3.grid(row =3,column=1)

# ---------------------------creacion boton---------------------------#

        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)
        boton1.config(row=4,column=2)

        root3.mainloop()

