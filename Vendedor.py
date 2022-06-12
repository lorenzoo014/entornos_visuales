
import threading
import time

from msilib.schema import Font
from tkinter import Tk, Frame,Label,Button,Entry,Canvas,font,W,E
# from venv import psycopg2
import psycopg2

                                                #aparece en la seccion "problemas" que no se puede encontrar el modulo del cual se importa pero esto se produce porque el programa no puede tener en cuenta que
#      f                                                            #yo lo estoy ejecutando sobre el entorno virtual "env"(importado por mi) en el cual SÍ esta importado el módulo PSYCOPG2 por eso no hay luego fallos porque en ese entorno SÍ esta importado
class Vendedor(threading.Thread):
        def __init__(self):
                print("se ha pulsado el boton vender")
                super().__init__()
                self.bloqueo2 = threading.Lock()
                # print(contador)
        def run(self):
        #---------------------------creacion de funciones---------------------------#
                def vuelvo():
                        self.bloqueo2.acquire()                                                # debido a  que es una funcion da igual utilizar objetos no creados(root) porque
                        # en el flujo de ejecucion ya estará creado

                def guarda_dato(nombre,apellido,nft):                                       #para que los vendedores coloquen sus anuncios
                        self.contador += 1                                               #variable contador para ver cuantas veces se han publicado anuncios
                        print(self.contador)
                        conn = psycopg2.connect(
                                host ="ec2-23-23-182-238.compute-1.amazonaws.com",
                                database="d8jkpbdn8n5tau",
                                user= "sfgectibhzlelp",
                                password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
                                port="5432"
                                )
                        cursor = conn.cursor()
                        query = '''INSERT INTO tabla_contador(nombre,apellido,nft) VALUES (%s,%s,%s)'''
                        cursor.execute(query,(nombre,apellido,nft))
                        conn.commit()
                        conn.close()
                        #-------pequeña comprobacion de que la signatura y los parametros se enlazan correctamente----------#
                        print(nombre)
                        print(apellido)
                        print(nft)
        ##---------------------------fin de funciones---------------------------#
                self.bloqueo2.acquire()
                root3=Tk()
                print("quiero vender")
                root3.title("VENDEDOR")



# #---------------------------creacion del canva---------------------------#
                canvas =Canvas(root3, height=380 ,width=400)
                canvas.pack()

# #---------------------------creacion del marco---------------------------#

                marco = Frame()
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

                boton1=Button(marco,text="¿quieres salir?",command=lambda:vuelvo())
                boton1.grid(row=5,column=1,sticky=W+E)

                boton2=Button(marco,text="poner en el mercado",command=lambda:guarda_dato(
                        entrada1.get(),
                        entrada2.get(),
                        entrada3.get())
                        )
                boton2.grid(row=4,column=1,sticky=W+E)
                #tiempo a dormir

                time.sleep(3)

                root3.mainloop()
