from django.shortcuts import render
from django.contrib import messages #adicionar msgs no contexto da página

from .forms import ContatoForm, ProdutoModelForm

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        #print(f'Post: {request.POST}')
        if form.is_valid():
            form.send_mail()

            '''nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')'''

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }


    return render(request, 'produto.html', context)
