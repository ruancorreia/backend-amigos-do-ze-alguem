from django.db import models

class Pessoa(models.Model):
  nome = models.CharField(max_length=100)
  apelido = models.CharField(max_length=50)
  endereco = models.CharField(max_length=100)

  def __str__(self):
    return self.nome