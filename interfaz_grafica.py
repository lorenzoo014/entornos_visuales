import tkinter as tk
from tkinter import Frame,Label,Button

import Comprador                                      #me importo el modulo comprador
from Comprador import Comprador                       #me importo la clase comprador

import Vendedor                              #me importo el modulo vendedor f
from Vendedor import Vendedor                #me importo la clase Vendedor del modulo Vendedor

import psycopg2

import threading
import time
class interfaz_grafica(threading.Thread):
    def __init__(self):
        super().__init__()
        self.bloqueo3 = threading.Lock()
    def run(self):

#---------------------------funciones---------------------------#
        def cambiapágina(a):
            if a==1:
                print("cambio")
                ñ=ñ+1
                self.bloqueo3.acquire()
                time.sleep(5)
                comprador1.bloqueo1.release()
            if a==2:
                root1.destroy()
                self.bloqueo3.acquire()
                time.sleep(5)
                vendedor1.bloqueo2.release()
                z=z+1



        root1 =tk.Tk()
        root1.title("NFT´S")
        global a,ñ,z                                           #me creo una variable global inicializada a 0 que luego será de uso en las funciones
        a=0
        ñ=0
        z=0

#---------------------------creacion del marco---------------------------#
        marco = Frame(root1)
        marco.pack(side="top",fill="x")
        marco.config(bg="blue",width=800,height=180)

        marco2 = Frame(root1)
        marco2.pack(fill="both",expand=True)
        marco2.config(bg="red")

#---------------------------Ventanas---------------------------#

        ventana_ppal =Label(marco2,text="COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
        ventana_ppal.place(x=150,y=170)

        ventana_ppal2 =Label(marco2,text="VENDEDOR",font=("Comic Sans MS",40),fg="GREEN")
        ventana_ppal2.place(x=950,y=170)

        ventana_ppal3 =Label(marco,text="BIENVENIDO",font=("Comic Sans MS",40),fg="GREEN")
        ventana_ppal3.place(x=500,y=0)

#---------------------------Botones---------------------------#

        boton1=Button(marco2,text="¿quieres comprar?",command=lambda: cambiapágina(1),width=47)
        boton1.place(x=150,y=270)

        boton2=Button(marco2,text="¿quieres vender?",command=lambda: cambiapágina(2),width=41)
        boton2.place(x=950,y=270)


#---------creacion de las tablas-------------#
        conn = psycopg2.connect(
            host ="ec2-23-23-182-238.compute-1.amazonaws.com",
            database="d8jkpbdn8n5tau",
            user= "sfgectibhzlelp",
            password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
            port="5432"
            )
# conn.database()
        cursor = conn.cursor()
# query1= "SHOW TABLES"
# cursor.execute(query1)
        query = '''CREATE TABLE IF NOT EXISTS tabla_contador (id SERIAL PRIMARY KEY, nombre TEXT,apellido TEXT,nft TEXT ,riesgo TEXT);'''
        cursor.execute(query)
        conn.commit()
        conn.close()
        print("se ha creado el registro")

        # if ñ==1:
        #     bloqueo1.acquire()
        #     root1.destroy()
        # elif z==1:                                           manera alternativa por si acaso
        #     bloqueo2.acquire()
        # else:
        #     time.sleep(2)

        root1.mainloop()

# ---------------main----------------#
objeto = interfaz_grafica()
vendedor1 =Vendedor()
comprador1 =Comprador()

objeto.start()
comprador1.start()
vendedor1.start()





