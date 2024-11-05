from django.shortcuts import render


def calculaCustos(request):
    custo = None
    tabela = []
    
    if request.method == "POST":
        # Pega o valor digitado pelo usuário
        custo = float(request.POST.get('custo', 0))

        # Gera a tabela com os cálculos
        for i in range(31):
            percentual = 2 + (i * 0.1)  # Percentual de 2 a 5 com incremento de 0.1
            venda = custo * percentual
            comissao = venda * 0.30  # Comissão de 30%
            lucro = venda - custo - comissao
            tabela.append({
                'percentual': round(percentual, 1),
                'custo': round(custo, 2),
                'venda': round(venda, 2),
                'comissao': round(comissao, 2),
                'lucro': round(lucro, 2),
            })
    
    return render(request, 'calculadora/calculaCustos.html', {'custo': custo, 'tabela': tabela})

