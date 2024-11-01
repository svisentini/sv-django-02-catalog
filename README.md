# sv-django-01-todo-list
Todo list with Django


DJANGO
Framework para Desenvolvimento Python


Video Youtube
	https://www.youtube.com/watch?v=MsUL3Pgofl4&t=28s
	
Configuração do Ambiente
https://github.com/treinaweb/treinaweb-youtube-introducao-ao-django/blob/main/.github/SETUP.md

Instalar uma extensão no VSCode para facilitar a visualização dos dados no SQLite
	SQLite Viewer

PIP >> Gerenciador de pacotes do python
Ambientes Virtuais >> Para nao ocorrer problemas de conflito de versoes das dependencias entre um projeto e outro >> Quando instaladas de forma global.
Cada projeto tera suas proprias dependencias.
	
--------------------------------------------------------
Passos para rodar a aplicação:
--------------------------------------------------------
- git config --global credential.helper store  >> Configura para GIT armazenar as credenciais
- Git clone
- sudo apt install python3-venv			>> Pacote para criar Ambientes Virtuais
- VSCode
  
	Extensões (Ctrl + P)

		ext install ms-python.python
  
		ext install batisteo.vscode-django
  
		SQLite Viewer

		Django  >> do Baptiste Darthenay

		MySQL >> do Weijan Chen
  
- python3 -m venv .venv 				>> Criar Ambiente Virtual
- source .venv/bin/activate 			>> Entrar no Ambiente Virtual
- pip install django
- pip install python-decouple
- pip install dj-database-url
- pip install black                     >> Biblioteca de formatação do código
- pip install crispy-bootstrap5			>> Biblioteca para formatação do "form" usando bootstrap5
Verificar se os arquivos .env e db.sqlite3 existem
- python manage.py makemigrations		>> Criar os arquivos de migração
- python manage.py migrate				>> Rodar as migrações
- python manage.py runserver			>> Rodar a aplicação

--------------------------------------------------------


1) Criar ambiente virtual e ativar
Linux:
		python3 -m venv .venv         >> Cria um Ambiente Virtual
		source .venv/bin/activate     >> Entra no Ambiente Virtual

2) Instalar o Django (dentro do ambiente virtual >> criado e ATIVADO no passo 1)
	pip install django

Para saber que esta dentro do ambiente virtual, verificar no inicio da linha de comando (.venv)

	
3) Criar um projeto (Projeto é um conjunto de app >> app seria cada funcionalidade)
	django-admin startproject setup .
Será criada uma pasta com alguns arquivos de configuração, por isso, por convensão essa pasta é chamada de setup, mas não é obrigatório.
	
4) Rodar aplicacao
	python manage.py runserver

5) Criar um APP (deve estar com o Ambiente Virtual ativo)
	python manage.py startapp todos

6) Precisa relacionar a APP com o projeto
“settings.py” tem os INSTALLED_APPS
Adicionar o APP recém criado
‘todos.apps.TodosConfig’

7) Criar arquivos de migrações a partir das classes de models.py
	python manage.py makemigrations

8) Rodar as migrações
	python manage.py migrate

    No arquivo “db.sqlite3”, é possível ver as tabelas criadas






Em “settings.py” tem algumas configurações para alterar:
- LANGUAGE_CODE para ‘pt-br’
- TIME_ZONE para 'America/Sao_Paulo'


Django trabalha com a arquitetura MTV

Model = É a camada relacionada com o Banco de Dados. Classes python que representam as entidades que a aplicação trabalha.

Template = Camada de visualização dos dados. Onde o usuário interage com a aplicação. São os arquivos HTML.

View = É a camada que faz o relacionamento entre as duas outras camadas.


Cada função declarara em views.py tem que ter um parametro “request”

No arquivo urls.py definimos a url e qual função será executada.

No models.py cada classe representa uma tabela no banco de dados.
Para isso, a classe precisa extender “models.Model”
Cada coluna do banco, será representado por um atributo nessa classe.


45:00 do video

Isolar as configurações para não ficarem "expostas"
    Instalar uma biblioteca para isso
        pip install python-decouple
    Criar um arquivo ".env" na raiz do projeto
        SECRET_KEY=django-insecure-gy$h5(78bb-cufrww@^o9b%b&d9r0!#4mr(kx27*wcrg!crod-
        DEBUG=True
        ALLOWED_HOSTS=*
    settings.py >> from decouple import config
    config("SECRET_KEY")
    Para a String de conexão, sera necessario outra biblioteca
        pip install dj-database-url
    from dj_database_url import parse as db_url

52:00 do video

--------------------------
11/09/2024
Ferramentas para padronização do código
    pip install black
    black .   >> Roda o formatador dos dados

--------------------------
12/09/2024
56:12 >> Criação das Páginas do Sistema
Criar um arquivo todo_lis.html e alterar o tipo dele para Django HTML

--------------------------
18/09/2024
1:09:00 >> Utilizando bootstrap
https://getbootstrap.com/
Sempre que alterar o Modelo ou criar um novo, precisa criar uma nova migração
	python manage.py makemigrations
Aplicar a migração
	python manage.py migrate
Se precisar apagar o arquivo db.sqlite3, apagar a conexao e criar outra para nao dar problemas.


--------------------------
18/09/2024
1:26:00 >> Uma nova maneira de criar as Views
Esatvamos utilizando as "FBV" >> Functions Based Views (Views baseadas em funções)

Vamos Utilizar as "Class Based Views" (CBV) >> Views baseadas em Classes >> Metodo mais novo e mais recomendado

CBV
	Django ja fornece uma serie de classes que podem ser utilizadas
	Fazer o import da da classe ListView 
	****  A classe vai utilizar o template que tem o nome do modelo utilizado + "_list" >> Nesse caso, todo_list.html

1:30:00
Cadastro de Tarefas
	View >> from django.views.generic import ListView, CreateView
	Para create view, a template utilizada sera o nome do modelo + "_form" >> Nesse caso, todo_form.html


-----------------------------
1:35:00

{% csrf_token %}

reverse_lazy >> Permite utilizar o nome das rotas

django-crispy-forms >> Permite renderizar o form utilizando booststrap
pip install crispy-bootstrap5
precisa adicionar bicliotecas no INSTALLED_APPS do sttings.py
verbose_name >> Nome para aperecer na tela >> Definido nos campos do Model.

1:50:10

Reaproveitamento de Código:
Herança de Templates
Criação de pontos onde podem ser inseridos blocos de códigos.
{% extends "base.html" %} >> Indica qual template base ira utilizar.

1:54:19

Pagina de Edição de Tarefas
from django.views.generic import UpdateView

2:01:24

Pagina de Exclusao de Tarefa
Importar a Generic View >> DeleteView
Um POST para a mesma rota é que confirma a exclusao

2:08:40

Ação de concluir uma tarefa
É uma tarefa especifica do projeto, entao nao tera uma view generica do Django que faça isso !
Importar a Generic View >> View (que é apenas uma view sem nenhuma funcionalidade)

2:15:23

Alguns ajustes na aplicação
Ordenação da listagem
Desabilitar botoes quando tarefa estiver concluida
Regras de negocio devem estar no modelo e nao na view





