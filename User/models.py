from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    """
    Representa um usuário.
    """

    REGIOES_BRASIL = [
        ('Norte', 'Norte'),
        ('Nordeste', 'Nordeste'),
        ('Centro-Oeste', 'Centro-Oeste'),
        ('Sudeste', 'Sudeste'),
        ('Sul', 'Sul'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    regiao_brasil = models.CharField(max_length=20, choices=REGIOES_BRASIL)

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para gerar uma senha segura se for um novo usuário.
        """
        if not self.pk:  # Verifica se é um novo registro
            # Gera a senha segura
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retorna uma representação em string do usuário.
        """
        return self.nome
