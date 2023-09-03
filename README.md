# django-intermediario-comMySQL

>Projeto Django intermediário com banco de dados MySQL, Bootstrap4.
> 
>>Projeto desenvolvido no curso da Geek University - Udemy [Programação Web com Python e Django Framework: Essencial](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/)

## Ambiente de Desenvolvimento
Linux, Docker e MySQL

## Documentação
- [DJango](https://www.djangoproject.com/)
## Desenvolvimento:
1. <span style="color:383E42"><b>Preparando ambiente</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar repositório no github
    - Criar README básico
    - Criar e ativar ambiente virtual
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    - Instalação pip - se necessario
        ```sh
        sudo apt update
        sudo apt install python3-pip
        pip3 --version
        ```
    - Instalar o `django`, `whitenoise`(para os arquivos staticos), `gunicorn`( servidor para python), `django-bootstrap4` (integrado com django), `PyMySQL`(driver de conexão com o banco mysql) e `django-std-image`(para trabalhar com imagens)
        ```sh
        sudo apt update
        pip3 install django
        pip3 install whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage
        ```
    - Criação arquivo requirements
    Contém informaçẽos sobre todas as bibliotecas utilizadas no projeto. Para atualizar o arquivo, basta executar o comando novamente após instalar outras bibliotecas.
        ```sh
        pip freeze > requirements.txt
        ```
    </p>

    </details> 

    ---

2. <span style="color:383E42"><b>Criação de projeto django2 e app core</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criar app no mesmo diretório/pasta que está o projeto. Usa ponto espaço e ponto no final para não criar subdiretório
        >Criarei um arquivo `meusDados.py` com com as informaçoes que não quero que vá para repositório - Então incluirei o arquivo com a classe no gitignore
        ```sh
        django-admin startproject django2 .
        django-admin startapp core
        ```
    - Incluir apps em Installed apps - settings
        ```python
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'core',
        'bootstrap4',
        'stdimage',
        ]
        ```
    - Adicionando MIDDLEWARE `whitenoise`, porém deixar comentado para uso posterior
        ```python
        MIDDLEWARE = [
            # ...
            "django.middleware.security.SecurityMiddleware",
            #"whitenoise.middleware.WhiteNoiseMiddleware",
            # ...
        ]
        ```
    
    - Informar diretório de templates no settings
        ```python
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': ['templates'],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```
    - Configurar databases
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': MeusDados['MYSQLDATABASENAME'],
                'USER': MeusDados['USUARIO_MYSQL'],
                'PASSWORD': MeusDados['SENHA_MYSQL'],
                'HOST': MeusDados['HOST'],
                'PORT':'3306',
                
            }
        }
        ```
    - Definindo timezone Em `settings.py`
        ```python
        # Internationalization
        # https://docs.djangoproject.com/en/4.2/topics/i18n/

        LANGUAGE_CODE = 'pt-br'

        TIME_ZONE = 'America/Sao_Paulo'

        USE_I18N = True

        USE_TZ = True

        ```

    - Configuração para arquivos státicos e `settings.py`
        ```python
        STATIC_URL = 'static/'
        STATIC_ROOT = os.path.join(STATIC_URL, 'staticfiles')
        ```
    </p>

    </details> 

    ---

3. <span style="color:383E42"><b>Criar container com imagem MySQL</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - [Documentação dockerhub](https://hub.docker.com/_/mysql/tags)
        Baixa imagem `pull mysql`
        Cria container 
        Nomeando `--name django2` 
        Adiciono informação da porta `-p 3306:3306`
        Informo a senha `MYSQL_ROOT_PASSWORD=suasenha`
        ```bash
        docker pull mysql
        sudo docker run -p 3306:3306 --name django2 -e MYSQL_ROOT_PASSWORD=suasenha -d mysql
        ```

        Inciar container
        ```bash
        sudo docker start django2
        ```

        Verificar `id` container e `ip` do container
        ```bash
        sudo docker ps
        sudo docker container inspect idcontainer
        ```

        Acessar container no modo interativo - container em execução
        ```bash
        sudo docker exec -it idcontainer bash
        ```

        Acessar mysql terminal. Informar senha
        ```bash
        mysql -u root -p 
        ```

        Criar database
        ```sql
        create database django2;
        ```

        Exibir databases
        ```sql
        show databases
        ```

    - Testar acesso com `Workbench`
        Instale o Workench pela loja de aplicativos linux
        Se algum erro ao configurar, como:
        `....Workbench incompatible/nonstandard server....`

        Após abrir o `Workbench` pressione `ctrl + r` ou clic em `Database` e selecione Reverse Engineer
        Informe `ip, user e password` do container em execução
    

    </p>

    </details> 

    ---

4. <span style="color:383E42"><b>Criação das views, rotas, templates e instalação MySQL</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Criação das views `index, contato, produto`
        ```python
        from django.shortcuts import render

        def index(request):
            return render(request, 'index.html')

        def contato(request):
            return render(request, 'contato.html')

        def produto(request):
            return render(request, 'produto.html')
        ```

    - Criação diretórios:
        `core/templates`
        `core/static`
        `core/static/css`
        `core/static/css/js`
        `core/static/css/js/images`

    - Criação templates
        >index.html
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Index</title>
        </head>
        <body>
            <h1>Index</h1>
        </body>
        </html>
        ```
        
        >contado.html
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cotato</title>
        </head>
        <body>
            <h1>Contato</h1>
        </body>
        </html>
        ```

        >produto.html
        ```html
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Produto</title>
        </head>
        <body>
            <h1>Produto</h1>    
        </body>
        </html>
        ```

    - Criar arquivo de rotas app core `core/urls.py`
        ```python
        urlpatterns = [
        path('', index, name='index'),
        path('contato/', contato, name='contato'),
        path('produto/', produto, name='produto'),
        ]
        ```

    - Incluir `rota` no arquivo de rotas do projeto que direciona para arquivo de rotas do app core - `django2/urls.py`
        ```python
        path('', include('core.urls')),
        ```

    - Instale o `libmysqlclient-dev` se necessário
        **Obs.:** no terminal principal/local, não no projeto
        ```bash
        sudo apt-get install libmysqlclient-dev python3-dev
        ```

    - Instalar `MysSQL` no projeto
        ```bash
        pip install MySQL
        ```

    - Atualizar o `requirements.txt`
        ```bash
        pip freeze > requirements.txt
        ```

    - Executar o `migrate` para criação das tabelas django no `database`
        Não esquecer de dar os privilégios necessários ao usuário do banco de dados
        ```bash
        python manage.py migrate
        ```

    - Criar super usuário do projeto
        ```bash
        python manage.py createsuperuser
        ```
    
    - Testar aplicação, se não der nenhum erro, teste no navegador com `localhost:8000`
        ```bash
        python3 manage.py runserver
        ```

    </p>

    </details> 

    ---

5. <span style="color:383E42"><b>Formulários</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Verificar os atributos de um form django com `python shell`
        >Observe que o sinal `>>>` é mostrado ao executar o primeiro comando, significa que está no python shell, não é parte do comando
        ```bash
        python manage.py shell
        >>> from django import forms
        >>> dir(forms)
        >>> help(forms.CharFields)
        ```

    - Criar arquivo `core/forms.py` - Arquivo que contém todos os formulários da aplicação - Criar o form `ContatoForm` 
        ```python
        from django import forms

        class ContatoForm(forms.Form):
            nome = forms.CharField(label='Nome', max_length=100)
            email = forms.EmailField(label='Email', max_length=100)
            assunto = forms.CharField(label='Assunto', max_length=120)
            # widget - Determina que seja um campo de texto com várias linhas
            mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
        ```

    - Incluir `ContatoForm` na view `contato`
        ```python
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
                    nome = form.cleaned_data['nome']
                    email = form.cleaned_data['email']
                    assunto = form.cleaned_data['assunto']
                    mensagem = form.cleaned_data['mensagem']

                    print('Mensagem enviada')
                    print(f'Nome: {nome}')
                    print(f'Email: {email}')
                    print(f'Assunto: {assunto}')
                    print(f'mensagem: {mensagem}')

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
        ```

    - Incluir `ContatoForm` ao template `contato.html`
        >Incluir bootstrap4 ao template `{% load bootstrap4 %}`
        `autocomplete`como `off` é para desativar opção autocomplete do formulário, evitando exibir dados informados anteriormente pelos usuários.
        `{% csrf_token %}` - Segurança - É criado um token a cada solicitação que usado para validar o formulário. É possível verificar esse token ao inspecionar página no navegador.
        `{% bootstrap_form form %}` - Indica ao bootstrap para aplicar css no `form` que recebeu como parâmetro da view `contato`
        
        ```html
        {% load bootstrap4 %}
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Contato</title>
            {% bootstrap_css %}
        </head>
        <body>
            <div class="container">
                <h1>Contato</h1>
                {% bootstrap_messages %}

                <form action="{% url 'contato' %}" method="post" class="form" autocomplete="off">
                    {% csrf_token %}
                    {% bootstrap_form form %}
                    {% buttons %}
                        <button type="submit" class="btn btn-primary">Enviar Mensagem</button>
                    {% endbuttons %}
                </form>
            </div>
        {% bootstrap_javascript jquery='full' %}
        </body>
        </html>
        ```

    - Testar
        ```bash
        python manage.py runserver
        ```

    </p>

    </details>

    ---

6. <span style="color:383E42"><b>Enviando e-mails com Django</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - Configuração email em `django2/settings.py`
        >Usado `EMAIL_BACKEND` para teste - Parte comentada é para uso com provedor de email
        ```python
        #...
        STATIC_ROOT = os.path.join(STATIC_URL, 'staticfiles')

        # Configuração de Email do seu servidor de email
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

        """
        EMAIL_HOST = `localhost`
        EMAIL_HOST_USER = `seuemail@seudomínio.com.br`
        EMAIL_PORT = 587
        EMAIL_USER_TSL = True
        EMAIL_HOST_PASSWORD = `sua senha`
        """
        #...
        ```

    - Incluir método para enviar email em `core/forms.py - ContatoForm`
        ```python
        #...
        def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
        #...
        ```

    - View `contato` configurada para usar o método `send_mail`
        ```python
        #...
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
        #...
        ```


    </p>

    </details>

    ---

7. <span style="color:383E42"><b>Definindo e configurando `models` e `ModelForms`</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    >Info: 
    >slugify - usado para criar url válida com texto passado
    >[signals](https://docs.djangoproject.com/en/4.2/topics/signals/) - Usado para detectar evento/ação que ocorra em outro lugar/objeto, neste caso `Produto` - [Tutorial](https://www.youtube.com/watch?v=CZ7vUBLpoZc)

    - Definindo modelo Produto em `core/models.py` - após definir o modelo, executar o `makemigrations e depois migrate`
        ```python
        from django.db import models
        from stdimage.models import StdImageField


        #SIGNALS
        from django.db.models import signals
        from django.template.defaultfilters import slugify


        class Base(models.Model):
            criado = models.DateField(`Data de Criação`, auto_now_add=True)
            modificado = models.DateField(`Data de Atualização`, auto_now=True)
            ativo = models.BooleanField(`Ativo?`, default=True)

            class Meta:
                abstract = True


        class Produto(Base):
            nome = models.CharField(`Nome`, max_length=100)
            preco = models.DecimalField(`Preço`, max_digits=8, decimal_places=2)
            estoque = models.IntegerField(`Estoque`)
            imagem = StdImageField(`Imagem`, upload_to=`produtos`, variations={`thumb`:(124,124)})
            slug = models.SlugField(`Slug`, max_length=100, blank=True, editable=False)

            def __str__(self):
                return self.nome


        def produto_pre_save(signal, instance, sender, **kwargs):
            instance.slug = slugify(instance.nome)


        signals.pre_save.connect(produto_pre_save, sender=Produto)

        ```
        Terminal
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

    - Configurar  exibição de `Produto` em painel admin `core/admin.py `
        ```python
        from django.contrib import admin

        from .models import Produto


        @admin.register(Produto)
        class ProdutoAdmim(admin.ModelAdmin):
            list_display = (`nome`, `preco`, `estoque`, `slug`, `criado`, `modificado`, `ativo`)
        ```

    - Testar aplicação, se não der nenhum erro, teste no navegador com `localhost:8000/admin`
        Cadastrar produto, inserir imagem para produto - Verificar slug

    - Criar `modelForm` de produto
        ```python
        class ProdutoModelForm(forms.ModelForm):

        class Meta:
            model = Produto
            fields = ['nome', 'preco', 'estoque', 'imagem']
        ```
    
    - Configurando view Produto - Inclusão de controle de acesso usando `Seção` do usuário
        > Em caso de usuário anônimo (não estando logado), será redirecionado para página `index.html`
        ```python
        def produto(request):
        if str(request.user) != 'AnonymousUser':
            if str(request.method) == 'POST':
                form = ProdutoModelForm(request.POST, request.FILES)
                if form.is_valid():
                    # Permite acessar as informações antes de serem salvas no banco de dados
                    # prod = form.save(commit=False)
                    form.save()

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
        else:
            return redirect('index')
        ```

    - Configurando template produto - botstrap4
        >Configuração para envio de arquivos no form `enctype="multipart/form-data"`
        ```html
        {% load bootstrap4 %}
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Produto</title>
            {% bootstrap_css %}
        </head>
        <body>
            <div class="container">
                <h1>Produto</h1>
                {% bootstrap_messages %}

                <form action="{% url 'produto' %}" method="post" class="form" autocomplete="off" enctype="multipart/form-data">
                    {% csrf_token %}

                    {% bootstrap_form form %}
                    {% buttons %}
                        <button type="submit" class="btn btn-primary">Cadastrar</button>
                    {% endbuttons %}
                </form>
            </div>
        {% bootstrap_javascript jquery='full' %}
        </body>
        </html>
        ```

    - Configurando diretório de midias/imagens em `settings` - Diretório e arquivos usados em modo debug
        >Obervação: Foi removido o diretório `produtos` que estava sendo usado anteriormente.
        ```python
        #..
        STATIC_ROOT = os.path.join(BASE_DIR, `staticfiles`)
        MEDIA_URL = `media/`
        MEDIA_ROOT = os.path.join(BASE_DIR, `media`)
        #...
        ```

    - Configurando arquivo urls do projeto2
        >Usado para permitir fazer acesso aos arquivos de mídias nos templates. O método `static(...)` retorna url para os arquivos. Usado no modo debug
        ```python
        from django.contrib import admin
        from django.urls import path, include

        from django.conf.urls.static import static
        from django.conf import settings

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('core.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        ```
    - Cofigurando a view `index` em `core/views.py`
        > Configurado envio de lista de produtos no contexto para página index
        ```python
        def index(request):
        context = {
            'produtos': Produto.objects.all()
        }
        return render(request, 'index.html', context)
        ```
    
    - Inclusão arquivo `core/static/css/styles.css` 
        >Configurar cor do link do produto
        ```css
        a{
            color: #fff;
        }
        ```

    - Configurando template `core/templates/index.html`
        ```html
        {% load bootstrap4 %}
        {% load static %}
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <title>Index</title>
            {% bootstrap_css %}
            <link href="{% static 'css/styles.css' %}" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                {% if produtos %}
                <h1>Produtos</h1>

                <table class="table table-dark">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Produto</th>
                            <th scope="col">Preço</th>
                            <th scope="col">Estoque</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for produto in produtos %}
                            <tr>
                                <td scope="row">{{ produto.id }}</td>
                                <td scope="row"><a href="#modal{{produto.id}}" data-toggle="modal">{{ produto.nome }}</a></td>
                                <td scope="row">{{ produto.preco }}</td>
                                <td scope="row">{{ produto.estoque }}</td>
                            </tr>
                            <div class="modal fade bd-example-modal-lg show" id="modal{{produto.id}}" role="dialog">
                                <div class="modal-dialog">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="modal-produto-label">Detalhes do produto</h5>
                                            <button type="button" class="close" data-dismiss="modal">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body" id="dynamic-content">
                                            <img src="{{ produto.imagem.url }}" class="img-fluid" alt="{{ produto.nome }}"/>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        {% endfor %}
                    </tbody>
                </table>
                {% else %}
                    <h2>Ainda não existem produtos cadastrados. :(</h2>
                {% endif %}
            </div>
        {% bootstrap_javascript jquery='full' %}
        </body>
        </html>
        ```
    </p>

    </details>

    ---


## Deploy no Google App Engine:
1. <span style="color:383E42"><b>Instalar a CLI gcloud [Link](https://cloud.google.com/sdk/docs/install?hl=pt-br)</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    >Em Desenvolvimento.....

    </p>

    </details>

    ---

## Meta
><span style="color:383E42"><b>Cristiano Mendonça Gueivara</b> </span>
>
>>[<img src="readmeImages/githubIcon.png">](https://github.com/sspectro "Meu perfil no github")
>
>><a href="https://linkedin.com/in/cristiano-m-gueivara/"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a> 
>
>>[<img src="https://sspectro.github.io/images/cristiano.jpg" height="25" width="25"> - Minha Página Github](https://sspectro.github.io/#home "Minha Página no github")<br>



><span style="color:383E42"><b>Licença:</b> </span> Distribuído sobre a licença `Software Livre`. Veja Licença **[MIT](https://opensource.org/license/mit/)**.