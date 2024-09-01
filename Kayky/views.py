from django.shortcuts import render
from .models import Pessoa, Descricao
# Create your views here.
def index(request):
    pessoas = Pessoa.objects.all()
    contexto = {
        'pessoa': pessoas,
    }
    return render(request, 'Kayky/index.html',contexto)

def detalhamento(request, pessoa_id):
    Pessoa_selecionada = Pessoa.objects.get(id=pessoa_id)
    descricoes = Descricao.objects.filter(pessoa=Pessoa_selecionada)
    contexto = {
        'pessoa': Pessoa_selecionada,
        'descricao': descricoes,
    }
    return render(request, 'Kayky/detalhamento.html',contexto)