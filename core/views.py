from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        print(f'Post: {request.POST}')
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
        else:
            messages.error(request, 'Erro ao enviar e-mail')
            form = ContatoForm()
    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')