# Projeto Django: Retornando "Hello World" a partir de uma View

Este projeto básico em Django tem como objetivo configurar um aplicativo que exibe a mensagem **"Hello World"** ao ser acessado em um navegador. Ele é uma introdução prática para quem está começando com Django e deseja entender como funciona a estrutura básica de rotas e views.

---

## Passos para Configurar o Projeto

### 1. **Criar o Projeto Django**
Execute o comando abaixo para criar um projeto chamado `hello_world_project`:
```bash
django-admin startproject hello_world_project
```
Isso criará uma estrutura básica de diretórios para o projeto.

### 2. **Criar o Aplicativo**
Dentro do diretório do projeto, crie um aplicativo chamado `hello`:
```bash
python manage.py startapp hello
```

### 3. **Registrar o Aplicativo no Projeto**
No arquivo `settings.py` dentro de `hello_world_project`, registre o aplicativo na variável `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...,
    'hello',
]
```

---

## Configuração da View

### 4. **Definir a View**
No arquivo `views.py` do aplicativo `hello`, crie uma função que retorna um **HttpResponse** com o texto "Hello World":
```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")
```

---

## Configuração de Rotas

### 5. **Criar o Arquivo `urls.py` no Aplicativo**
Crie um arquivo `urls.py` dentro do diretório `hello` e configure uma rota para a view:
```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]
```

### 6. **Incluir as Rotas do Aplicativo no Projeto**
No arquivo `urls.py` do projeto (`hello_world_project/urls.py`), inclua as rotas do aplicativo:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),  # Inclui as rotas do aplicativo hello
]
```

---

## Executar o Projeto

### 7. **Iniciar o Servidor**
Execute o comando para iniciar o servidor de desenvolvimento:
```bash
python manage.py runserver
```

### 8. **Acessar no Navegador**
Abra o navegador e acesse `http://127.0.0.1:8000/`. Você verá a mensagem **"Hello World"**.

---

## Explicação do Fluxo

1. **Rota do Projeto**: O arquivo `hello_world_project/urls.py` redireciona as requisições para o aplicativo `hello`.
2. **Rota do Aplicativo**: O arquivo `hello/urls.py` define qual view será chamada ao acessar a URL.
3. **View**: A função `hello_world` retorna uma resposta HTTP com a mensagem "Hello World".

---

## Possíveis Melhorias

- **Usar Templates**: Substituir o retorno simples de texto por um template HTML.
- **Adicionar Rotas Personalizadas**: Criar outras views e rotas para expandir a aplicação.
- **Adicionar Testes**: Implementar testes unitários para garantir que a aplicação retorna o texto correto.

Esse projeto é ideal para aprender os fundamentos de views e roteamento no Django.
