class Coche:
    ruedas = 4
    def__init__(color, aceleracion):
       self.color = color
       self.aceleracion = aceleracion
       self.velocidad = 0

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad = self.velocidad + self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

