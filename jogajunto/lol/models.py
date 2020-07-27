from django.db import models


class Fila(models.Model):
    # O django faz o ID, sozinho, durante as "migrations"
    name_view = models.TextField()
    tier = models.TextField()
    rank = models.TextField()
    modal = models.TextField()

