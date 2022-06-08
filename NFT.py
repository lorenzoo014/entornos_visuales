import random
from sqlalchemy import null
class NFT():
    global riesgo
    riesgo = null
    def __init__(self,riesgo):
        if riesgo ==null:                  #esto se ejecuta en caso de que riesgo no tenga ningun valor,y obviamente no lo va a decidir el vendedor q solo busca su beneficio

            riesgo= random.randint(1,3)
        else:
            pass
def nivelRiesgo(self):
    return self.riesgo
