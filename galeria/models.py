
from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "nebulosa"),
        ("ESTRELA", "estrela"),
        ("GALAXIA", "galaxia"),
        ("PLANETA", "planeta"),
        ("BURACO NEGRO", "buraco negro")
    ]

    nome = models.CharField(max_length=100, null=False , blank=False)
    legenda = models.CharField(max_length=150, null=False , blank=False)
    categoria = models.CharField(max_length=100,choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    data_fotografia = models.DateTimeField(default = datetime.now , blank = False)
    publicada = models.BooleanField(default=False)
    


    def __str__(self) -> str:
        return self.nome