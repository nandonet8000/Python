from django.db import models

class Patrocinio(models.Model):
    descricao = models.CharField(max_length=100, null=False , blank=False)
    tempoInicio = models.DateField(null= False)
    tempoFim = models.DateField(auto_now=False, auto_now_add=False,null = False)
    valor = models.DecimalField(max_digits=19, decimal_places=10,null =False)

    def __str__(self) -> str:
        return f"Fotografia  Nome: {self.descricao}"
