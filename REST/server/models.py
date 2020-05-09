from django.db import models
import sys
from itertools import cycle
# Create your models here.

class User(models.Model):
    rut = models.CharField(max_length=25)
    nombres = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)
    comprut = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.rut = self.rut.upper()
        self.nombres = self.nombres.title()
        self.ap_paterno = self.ap_paterno.title()
        self.ap_materno = self.ap_materno.title()
        self.genero = self.genero.upper()

        rut1 = self.rut
        self.rut = self.rut.replace(".", "")
        self.rut = self.rut.replace("-", "")
        rut1 = rut1.replace(".", "")
        rut1 = rut1.replace("-", "")

        aux=rut1[:-1]
        dv=rut1[-1:]

        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s)%11
        if str(res) == dv:
            self.comprut = True
        elif dv == "K" and res==10:
            self.comprut = True
        else:
            self.comprut = False
        if self.comprut == False:
            self.comprut = "caca"


        self.rut = self.rut[::-1]
        ct=0
        for indice in range(len(self.rut)):
            if ct==0:
                aux1=self.rut[indice]
            if ct==3:
                aux2="-"+self.rut[indice-2]+self.rut[indice-1]+self.rut[indice]+"."
            if ct==6:
                aux3=self.rut[indice-2]+self.rut[indice-1]+self.rut[indice]+"."
            if ct==7:
                aux4=self.rut[indice]
            if ct>7:
                aux4=aux4+self.rut[indice]
            ct=ct+1

        self.rut = aux1+aux2+aux3+aux4
        self.rut = self.rut[::-1]



        return super(User, self).save(*args, **kwargs)
