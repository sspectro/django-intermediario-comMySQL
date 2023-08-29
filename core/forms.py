from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    # widget - Determina que seja um campo de texto com várias linhas
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())