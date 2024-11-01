from django.shortcuts import render
from .models import Produto, Categoria, Acabamento

def listar_produtos(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    acabamentos = Acabamento.objects.all()
    
    # Filtros
    descricao = request.GET.get('descricao')
    categoria = request.GET.get('categoria')
    acabamento = request.GET.get('acabamento')
    
    if descricao:
        produtos = produtos.filter(descricao__icontains=descricao)
    if categoria:
        produtos = produtos.filter(categoria__id=categoria)
    if acabamento:
        produtos = produtos.filter(acabamento__id=acabamento)

    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos, 'categorias': categorias, 'acabamentos': acabamentos})
