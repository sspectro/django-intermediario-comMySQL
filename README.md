# django-intermediario-comMySQL

>Projeto Django intermediário com banco de dados MySQL, Bootstrap5
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
    - Instalar o `django`, `whitenoise`(para os arquivos staticos), `gunicorn`( servidor para python), `django-bootstrap-v5` (integrado com django), `PyMySQL`(driver de conexão com o banco mysql) e `django-std-image`(para trabalhar com imagens)
        ```sh
        sudo apt update
        pip3 install django
        pip3 install whitenoise gunicorn django-bootstrap5 PyMySQL django-stdimage
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
        'bootstrap5',
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
        >Incluir bootstrap5 no template `{% load bootstrap5 %}`
        `autocomplete`como `off` é para desativar opção autocomplete do formulário, evitando exibir dados informados anteriormente pelos usuários.
        `{% csrf_token %}` - Segurança - É criado um token a cada solicitação que usado para validar o formulário. É possível verificar esse token ao inspecionar página no navegador.
        `{% bootstrap_form form %}` - Indica ao bootstrap para aplicar css no `form` que recebeu como parâmetro da view `contato`
        
        ```html
        {% load bootstrap5 %}

        <!DOCTYPE html>
        <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Cotato</title>

                {# Load CSS and JavaScript #}
                {% bootstrap_css %}
                {% bootstrap_javascript %}
        </head>
        <body>
            <div class="container">
                <h1>Contato</h1>
                {% bootstrap_messages %}
                {# Display a form #}
                <form action="{% url 'contato' %}" method="post" class="form" autocomplete="off">
                    {% csrf_token %}
                    {% bootstrap_form form %}
                    {% buttons %}
                    <button type="submit" class="btn btn-primary">
                        Enviar Mensagem
                    </button>
                    {% endbuttons %}
                </form>
            </div>
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


## Deploy no Google App Engine:
1. <span style="color:383E42"><b>Instalar a CLI gcloud [Link](https://cloud.google.com/sdk/docs/install?hl=pt-br)</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>



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



><span style="color:383E42"><b>Licença:</b> </span> Distribuído sobre a licença `Software Livre`. Veja Licença **[MIT](https://opensource.org/license/mit/)**. para mais informações.