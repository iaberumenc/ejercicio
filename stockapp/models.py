from django.db import models

# Create your models here.
class stock(models.Model):
    id = models.CharField(max_length=10,null=False,primary_key=True)
    nombre = models.CharField(max_length=80)
    cantidad = models.IntegerField(max_length=4,null=False)
    precio = models.FloatField(max_length=10,null=False)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre
