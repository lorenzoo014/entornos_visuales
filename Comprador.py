
import tkinter as tk
from tkinter import E, END, Frame,Label,Button,Entry,Listbox,W


import threading
import time
# import conector
# from conector import conector


# import interfaz_grafica                                       #me importo el modulo interfaz_grafica
#                                                             #me importo la clase interfaz_grafica del modulo interfaz_grafica

# esto solo va a servir para asegurarme guardar el github debido a que voy a hacer cambios sustanciales con el thread

import psycopg2



class Comprador(threading.Thread):
#---------------------------metodos de la clase---------------------------#
        def __init__(self):
                print("se ha pulsado el boton comprar")
                super().__init__()
                self.bloqueo1 = threading.Lock()


        def run(self):
                #---------------metodos de la clase ventana nueva------------#
                def vuelvo():
                        self.bloqueo1.acquire()
                def mostrar():
                        conn = psycopg2.connect(
                                host ="ec2-23-23-182-238.compute-1.amazonaws.com",
                                database="d8jkpbdn8n5tau",
                                user= "sfgectibhzlelp",
                                password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
                                port="5432"
                                )
                        cursor = conn.cursor()
                        query = '''SELECT * FROM tabla_contador'''
                        cursor.execute(query)
                        guardar = cursor.fetchall()
                        caja = Listbox(marco, width=20, height=5)
                        caja.grid(row=1, columnspan=10,sticky=W+E)                   #el cloumnspan sirve para que le de espacio a los lados
                        for elemento in guardar:
                                caja.insert(END, elemento)
                        conn.commit()
                        conn.close()


                self.bloqueo1.acquire()
                root2 = tk.Tk()                                            #tras estar mucho pensandolo e intentado que este metodo devolviese a la ventana original pero no he sido capaz de averiguar cómo
                print("quiero comprar")

                root2.title("COMPRADOR")


#---------------------------creacion del marco---------------------------#

                marco = Frame(root2)
                marco.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
                marco.config(bg="blue",width=800,height=800)

#---------------------------creacion ventana---------------------------#

                ventana_ppal3 =Label(marco,text="BIENVENIDO COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
                ventana_ppal3.grid(row=0,column=1)

#---------------------------creacion botones---------------------------#

                boton1=Button(marco,text="¿quieres volver?",command=lambda:vuelvo(),width=47)
                boton1.grid(row=2,column=0)

#---------------------------creacion entradas---------------------------#
#por ahora lo dejo vacio porque no sé si lo voy a usar

                mostrar()
                time.sleep(3)


#crear una tercera clase alternativa para guardar ahi los threads a ver qué pasa
                root2.mainloop()



# comprador1 =Comprador()
# comprador1.habla()
#        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)