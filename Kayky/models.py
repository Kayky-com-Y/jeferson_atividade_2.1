from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.IntegerField()
    data_nacimento = models.DateField()
    image = models.ImageField(upload_to='cursos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Descricao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=500)
    interesses = models.TextField(max_length=500)
    parentesco = models.CharField(max_length=100)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.parentesco