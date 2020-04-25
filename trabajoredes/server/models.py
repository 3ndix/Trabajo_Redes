from django.db import models

# Create your models here.

class User(models.Model):
    rut = models.CharField(max_length=25)
    nombres = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        self.nombres = self.nombres.title()
        self.ap_paterno = self.ap_paterno.title()
        self.ap_materno = self.ap_materno.title()
        self.genero = self.genero.title()
        return super(User, self).save(*args, **kwargs)
