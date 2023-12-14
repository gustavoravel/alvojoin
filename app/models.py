from django.db import models


class Alvo(models.Model):
    identificador = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_expiracao = models.DateField()

    def __str__(self):
        return self.nome
