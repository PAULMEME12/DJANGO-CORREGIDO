from django.db import models

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)  # Campo de texto para el nombre
    email = models.EmailField()                # Campo de correo electrónico

    def __str__(self):
        return self.nombre                     # Muestra el nombre al imprimir el objeto