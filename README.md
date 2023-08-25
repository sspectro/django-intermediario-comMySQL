# django-intermediario-comMySQL

>Projeto Django intermediário com banco de dados MySQL, Bootstrap5
> 
>>Projeto desenvolvido no curso da Geek University - Udemy [Programação Web com Python e Django Framework: Essencial](https://www.udemy.com/course/programacao-web-com-django-framework-do-basico-ao-avancado/)

## Ambiente de Desenvolvimento
Linux, MySQL

## Documentação
- [DJango](https://www.djangoproject.com/)
## Desenvolvimento:
1. <span style="color:383E42"><b>Preparando ambiente</b></span>
    <!-- <details><summary><span style="color:Chocolate">Detalhes</span></summary> -->
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
    - Instalar o `django`, `whitenoise`(para os arquivos staticos), `gunicorn`( servidor para python), `bootstrap5` (integrado com django), `PyMySQL`(driver de conexão com o banco mysql) e `django-std-image`(para trabalhar com imagens)
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
        'std-image',
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
                'NAME': MYSQLDATABASENAME,
                'USER': USUARIO_MYSQL,
                'PASSWORD': SENHA_MYSQL,
                'HOST': HOST,
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
    
    </p>

    </details> 

    ---

3. <span style="color:383E42"><b>Criar container com imagem mysql</b></span>
    <details><summary><span style="color:Chocolate">Detalhes</span></summary>
    <p>

    - [Documentação dockerhub](https://hub.docker.com/_/mysql/tags)
        Adiciono informação da porta `3306:3306`
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