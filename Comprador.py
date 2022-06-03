
import tkinter as tk
from tkinter import Frame,Label,Button
# import conector
# from conector import conector


# import interfaz_grafica                                       #me importo el modulo interfaz_grafica
#                                                             #me importo la clase interfaz_grafica del modulo interfaz_grafica


class Comprador():
#---------------------------metodos de la clase---------------------------#
    def __init__(self):
        print("se ha pulsado el boton comprar")

    def VentanaNueva(self):
        def vuelvo():                                                        #tras estar mucho pensandolo e intentado que este metodo devolviese a la ventana original pero no he sido capaz
                                                                                #de averiguar cómo
            root2.destroy()
        print("quiero comprar")
        root2=tk.Tk()
        root2.title("COMPRADOR")


#---------------------------creacion del marco---------------------------#

        marco = Frame(root2)
        marco.pack(side="top",fill="x")
        marco.config(bg="blue",width=800,height=800)

#---------------------------creacion ventana---------------------------#

        ventana_ppal3 =Label(marco,text="BIENVENIDO COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
        ventana_ppal3.place(x=500,y=0)

#---------------------------creacion botones---------------------------#

        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)
        boton1.place(x=250,y=250)

        root2.mainloop()



# comprador1 =Comprador()
# comprador1.habla()
#        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)