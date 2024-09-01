from django.contrib import admin
from .models import Pessoa, Descricao

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Descricao)
class DescricaoAdmin(admin.ModelAdmin):
    list_display = ['parentesco']