
# import tkinter as tk
# from tkinter import E, END, Frame,Label,Button,Entry,Listbox,W


# import threading
# import time
# # import conector
# # from conector import conector


# # import interfaz_grafica                                       #me importo el modulo interfaz_grafica
# #                                                             #me importo la clase interfaz_grafica del modulo interfaz_grafica

# # esto solo va a servir para asegurarme guardar el github debido a que voy a hacer cambios sustanciales con el thread

# import psycopg2



# class Comprador():
# #---------------------------metodos de la clase---------------------------#
#         def __init__(self):
#                 # super().__init__()
#                 # self.bloqueo1 = threading.Lock()
#                 print("bienvenido comprador")


#         def run(self):
#                 #---------------metodos de la clase ventana nueva------------#
#                 def vuelvo():
#                         # # self.bloqueo1.acquire()
#                         # threading.Lock.release()
#                         # threading.Lock.acquire()

#                 def mostrar():
#                         conn = psycopg2.connect(
#                                 host ="ec2-23-23-182-238.compute-1.amazonaws.com",
#                                 database="d8jkpbdn8n5tau",
#                                 user= "sfgectibhzlelp",
#                                 password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
#                                 port="5432"
#                                 )
#                         cursor = conn.cursor()
#                         query = '''SELECT * FROM tabla_contador'''
#                         cursor.execute(query)
#                         guardar = cursor.fetchall()
#                         caja = Listbox(marco, width=20, height=5)
#                         caja.grid(row=1, columnspan=10,sticky=W+E)                   #el cloumnspan sirve para que le de espacio a los lados
#                         for elemento in guardar:
#                                 caja.insert(END, elemento)
#                         conn.commit()
#                         conn.close()


#                 # self.bloqueo1.acquire()
#                 root2 = tk.Tk()                                            #tras estar mucho pensandolo e intentado que este metodo devolviese a la ventana original pero no he sido capaz de averiguar cómo
#                 print("quiero comprar")

#                 root2.title("COMPRADOR")


# #---------------------------creacion del marco---------------------------#

#                 marco = Frame(root2)
#                 marco.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
#                 marco.config(bg="blue",width=800,height=800)

# #---------------------------creacion ventana---------------------------#

#                 ventana_ppal3 =Label(marco,text="BIENVENIDO COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
#                 ventana_ppal3.grid(row=0,column=1)

# #---------------------------creacion botones---------------------------#

#                 boton1=Button(marco,text="¿quieres volver?",command=lambda:vuelvo(),width=47)
#                 boton1.grid(row=2,column=0)

# #---------------------------creacion entradas---------------------------#
# #por ahora lo dejo vacio porque no sé si lo voy a usar

#                 mostrar()
#                 # time.sleep(3)


# #crear una tercera clase alternativa para guardar ahi los threads a ver qué pasa
#                 root2.mainloop()



# # comprador1 =Comprador()
# # comprador1.habla()
# #        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)


from msilib.schema import Font
# from venv import psycopg2
import psycopg2                                                    #aparece en la seccion "problemas" que no se puede encontrar el modulo del cual se importa pero esto se produce porque el programa no puede tener en cuenta que
#                                                                  #yo lo estoy ejecutando sobre el entorno virtual "env"(importado por mi) en el cual SÍ esta importado el módulo PSYCOPG2 por eso no hay luego fallos porque en ese entorno SÍ esta importado
#      f                                                            #yo lo estoy ejecutando sobre el entorno virtual "env"(importado por mi) en el cual SÍ esta importado el módulo PSYCOPG2 por eso no hay luego fallos porque en ese entorno SÍ esta importado

import tkinter as tk
from tkinter import E, END, Frame,Label,Button,Entry,Listbox,W,Canvas
# import conector
# from conector import conector
# import interfaz_grafica                                       #me importo el modulo interfaz_grafica
#                                                             #me importo la clase interfaz_grafica del modulo interfaz_grafica

# esto solo va a servir para asegurarme guardar el github debido a que voy a hacer cambios sustanciales con el thread


# import threading
# import time


class Comprador():
#---------------------------metodos de la clase---------------------------#
        def __init__(self):
                pass
        def VentanaNueva(self, master,callback = None, args=(),kwargs={}):
                #---------------metodos de la clase ventana nueva------------#
                # def vuelvo():
                #         root2.destroy()
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
                # root2 = tk.Tk()                                            #tras estar mucho pensandolo e intentado que este metodo devolviese a la ventana original pero no he sido capaz de averiguar cómo

                # root2.title("COMPRADOR")
#---------------------------creacion del marco---------------------------#
                # marco = Frame(root2)
                marco = tk.Frame(master)
#---------------------------creacion ventana---------------------------#
                ventana_ppal3 =Label(marco,text="BIENVENIDO COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
                ventana_ppal3.grid(row=0,column=1)
#---------------------------creacion botones---------------------------#
                boton1=Button(marco,text="¿quieres volver?",command= callback)
                boton1.grid(row=2,column=0)
#---------------------------creacion entradas---------------------------#
#por ahora lo dejo vacio porque no sé si lo voy a usar
                mostrar()
                #root.mainloop()
                return marco
#la idea de lo que he hecho es conectar el comprador a un frame que se conecta a su vez a un root indeterminado(se determina en la clase interfaz_grafica).Y, al final del metodo devolver dicho marco

#---------------borrador--------------#
# comprador1 =Comprador()
# comprador1.habla()
#        boton1=Button(marco,text="¿quieres volver?",command=lambda: vuelvo(),width=47)


#command=lambda:threading.Thread(vuelvo()).start()