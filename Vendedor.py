
from msilib.schema import Font
from tkinter import Tk, Frame,Label,Button,Entry,Canvas,font,W,E
from venv import psycopg2                                                     #esta opcion me vale para resolver el problema pero deberia bastar con la sentencia "import psycopg2"-->evidentemente despues de haber instalado el psycopg2 en el entorno (venv)

class Vendedor:
        def __init__(self):
                print("se ha pulsado el boton vender")

        def VentanaNueva2(self):
        #---------------------------creacion de funciones---------------------------#
                def vuelvo():
                        root3.destroy()                                                    # debido a  que es una funcion da igual utilizar objetos no creados(root) porque
                        # en el flujo de ejecucion ya estará creado

                def guarda_dato(nombre,apellido,nft):                                       #para que los vendedores coloquen sus anuncios
                        conn= psycopg2.connect(
                                host ="ec2-54-211-255-161.compute-1.amazonaws.com",
                                database="dfese1r3fhpnbb",
                                user= "ketdxgwirslzzx",
                                password="5db9c6dec51f126c19693415abaaf635a36b326f20ea14ca0dcd4a27b6fa1d4f",
                                port="5432"
        )
                        cursor = conn.cursor()
                        query = '''INSERT INTO users(nombre,apellido,nft) VALUES (&s,&s,&s)'''
                        cursor.execute(query,(nombre,apellido,nft))
                        conn.commit()
                        conn.close()
        ##---------------------------fin de funciones---------------------------#
                root3=Tk()
                print("quiero vender")
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

                boton1=Button(marco,text="¿quieres salir?",command=lambda:vuelvo())
                boton1.grid(row=5,column=1,sticky=W+E)

                boton2=Button(marco,text="poner en el mercado")
                ''' ,command=lambda:guarda_dato(entrada1.get(),entrada2.get(),entrada3.get()))'''#esto se supone que iria arriba
                boton2.grid(row=4,column=1,sticky=W+E)

                root3.mainloop()

