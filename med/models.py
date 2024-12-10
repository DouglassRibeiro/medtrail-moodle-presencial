from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # Ideal para hash da senha
    telefone = models.CharField(max_length=15, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(
        max_length=20,
        choices=[
            ("feminino", "Feminino"),
            ("masculino", "Masculino"),
            ("outro", "Outro"),
            ("nao_informar", "Prefiro não informar")
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome