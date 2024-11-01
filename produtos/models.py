from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Acabamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    codigo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    acabamento = models.ForeignKey(Acabamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
