# ¡
# import tkinter as tk
# from tkinter import Frame,Label,Button

# import Comprador                                      #me importo el modulo comprador
# from Comprador import Comprador                       #me importo la clase comprador

# import Vendedor                              #me importo el modulo vendedor f
# from Vendedor import Vendedor                #me importo la clase Vendedor del modulo Vendedor

# import psycopg2

# import threading
# import time
# class interfaz_grafica():
#                                         #me creo una variable global inicializada a 0 que luego será de uso en las funciones
#     def __init__(self):
#         # super().__init__()
#         self.ñ = 0
#         self.z = 0
#         # self.bloqueo3 = threading.Lock()
#     # def run(self):

# #---------------------------funciones---------------------------#
#     def cambiapágina(a):
#         if a==1:
#                 # print("cambio")
#                 # ñ=ñ+1
#                 # # self.bloqueo3.acquire()
#                 # time.sleep(2)
#                 # comprador1.start()
#                 # threading.Lock.acquire()
#                 # time.sleep(2)
#                 # print("se ha pulsado el boton comprar")
#                 # comprador1.start()
#                 # threading.Lock.acquire()
#                 # time.sleep(2)
#             Comprador1 = Comprador()

#                 # comprador1.bloqueo1.release()
#         if a==2:
#                 # root1.destroy()
#                 # # self.bloqueo3.acquire()
#                 # vendedor1.start()
#                 # time.sleep(2)
#                 # threading.Lock.acquire()
#                 # # vendedor1.bloqueo2.release()
#                 # print("se ha pulsado el boton vender")
#                 #             # aplico esto para que el programa tenga claro que me refiero a la variable global z ya que sino se piensa q "z" es una variable LOCAL cuando no lo es
#                 # vendedor1.start()
#                 # # threading.Lock.acquire()  la BUENA
#             time.sleep(2)
#     root1 =tk.Tk()
#     root1.title("NFT´S")

# #---------------------------creacion del marco---------------------------#
#     marco = Frame(root1)
#     marco.pack(side="top",fill="x")
#     marco.config(bg="blue",width=800,height=180)

#     main_frame = Frame(root1)
#     main_frame.pack(fill="both",expand=True)
#     main_frame.config(bg="red")

# #---------------------------Ventanas---------------------------#

#     ventana_ppal =Label(main_frame,text="COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
#     ventana_ppal.place(x=150,y=170)

#     ventana_ppal2 =Label(main_frame,text="VENDEDOR",font=("Comic Sans MS",40),fg="GREEN")
#     ventana_ppal2.place(x=950,y=170)

#     ventana_ppal3 =Label(marco,text="BIENVENIDO",font=("Comic Sans MS",40),fg="GREEN")
#     ventana_ppal3.place(x=500,y=0)

# #---------------------------Botones---------------------------#

#     boton1=Button(main_frame,text="¿quieres comprar?",command=lambda:cambiapágina(1),width=47)
#     boton1.place(x=150,y=270)

#     boton2=Button(main_frame,text="¿quieres vender?",command=lambda: cambiapágina(2),width=41)
#     boton2.place(x=950,y=270)


# #---------creacion de las tablas-------------#
#     conn = psycopg2.connect(
#         host ="ec2-23-23-182-238.compute-1.amazonaws.com",
#         database="d8jkpbdn8n5tau",
#         user= "sfgectibhzlelp",
#         password="e30184e8472a143402057f1b68c02afac1e0ffd8b3c504783772a6362b67fe3c",
#         port="5432"
#         )
# # conn.database()
#     cursor = conn.cursor()
# # query1= "SHOW TABLES"
# # cursor.execute(query1)
#     query = '''CREATE TABLE IF NOT EXISTS tabla_contador (id SERIAL PRIMARY KEY, nombre TEXT,apellido TEXT,nft TEXT ,riesgo TEXT);'''
#     cursor.execute(query)
#     conn.commit()
#     conn.close()
#     print("se ha creado el registro")

#         # if ñ==1:
#         #     bloqueo1.acquire()
#         #     root1.destroy()
#         # elif z==1:                                           manera alternativa por si acaso
#         #     bloqueo2.acquire()
#         # else:
#         #     time.sleep(2)


#     root1.mainloop()

# # ---------------main----------------#
# # objeto = interfaz_grafica()
# # objeto.start()
# # comprador1.start()
# # vendedor1.start()


import tkinter as tk
from tkinter import Frame,Label,Button

import Comprador                                      #me importo el modulo comprador
from Comprador import Comprador                       #me importo la clase comprador

import Vendedor                              #me importo el modulo vendedor f
from Vendedor import Vendedor                #me importo la clase Vendedor del modulo Vendedor

import threading
import time

import psycopg2

root1 =tk.Tk()
root1.title("NFT´S")
root1.minsize(height=2000,width=2000)
root1.maxsize(height=2000,width=2000)
global a                                           #me creo una variable global inicializada a 0 que luego será de uso en las funciones
a=0
#---------------------------funciones---------------------------#
def mostrar_comprador():
    vendedor.pack_forget()
    main_frame.pack_forget()
    comprador.pack(fill="both", expand=True)
    # comprador.place(relx=0.1, rely=0.1, relwidth=0.8,relheight=0.8)
    # comprador.config(bg="blue",width=800,height=800)


def mostrar_vendedor():
    comprador.pack_forget()
    main_frame.pack_forget()
    vendedor.pack(fill="both",expand=True)
    print("quiero comprar")
    print("bienvenido comrpador")

#     # root1.destroy()
# anaNueva2()    vendedor1 =Vendedor()
#     vendedor1.Vent

def primeraPág():
    comprador.pack_forget()
    vendedor.pack_forget()
    main_frame.pack(fill="both",expand=True)

#---------------------------configuracion del marco---------------------------#
main_frame = Frame(root1)
main_frame.config(bg="red")
#---------------------------Ventanas---------------------------#
ventana_ppal =Label(main_frame,text="COMPRADOR",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal.place(x=150,y=170)
ventana_ppal2 =Label(main_frame,text="VENDEDOR",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal2.place(x=950,y=170)
ventana_ppal3 =Label(main_frame,text="BIENVENIDO",font=("Comic Sans MS",40),fg="GREEN")
ventana_ppal3.place(x=500,y=0)
#---------------------------Botones---------------------------#
boton1=Button(main_frame,text="¿quieres comprar?",command=lambda:mostrar_comprador(),width=47)
boton1.place(x=150,y=270)
boton2=Button(main_frame,text="¿quieres vender?",command=lambda:mostrar_vendedor(),width=41)
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

#----------main(2)-----------#

comprador = Comprador().VentanaNueva(root1, primeraPág)     #sirve para enganchar el frame devuelto por VentanaNueva al root |||IMPORTANTE--> poner en la signatura del metodo el metodo que empaqueta el primer frame porque es ahí donde se dirige el callback
vendedor = Vendedor().VentanaNueva2(root1, primeraPág)       #lo mismo pero con el vendedor
primeraPág()

root1.mainloop()



#----------------borrador----------------#
# main_frame.pack(fill="both",expand=True)
# threading.Thread(target=cambiapágina(1)).start()



