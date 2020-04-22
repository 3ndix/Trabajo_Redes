from django.db import models

# Create your models here.

class User(models.Model):
    rut = models.BigIntegerField()
    dig_ver = models.CharField(max_length=5)
    nombres = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    genero = models.CharField(max_length=15)
    