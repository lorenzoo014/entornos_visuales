import random
class NFT():
    def __init__(self, nivel=0,riesgo="bajo"):
        self.nivel = nivel
        self.riesgo =riesgo

    def NivelRiesgo(self):
        nivel = random.randint(1,3)
        if nivel == 3:
            self.riesgo ="alto"
        if nivel == 2:
            self.riesgo ="medio"
        if nivel == 1:
            self.riesgo ="bajo"

