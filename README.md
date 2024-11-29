#### **1. Criar o Projeto e a Aplicação**

Comandos para iniciar o projeto e a aplicação:

```bash
# Crie o projeto Django
django-admin startproject myproject

# Entre na pasta do projeto
cd myproject

# Crie uma aplicação chamada "hello"
python manage.py startapp hello
```

---

#### **2. Configurar a Aplicação no Projeto**

Edite o arquivo `myproject/settings.py` e adicione `hello` ao array `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',  # Adicione aqui a aplicação "hello"
]
```

---

#### **3. Criar a View "Hello, World!"**

No arquivo `hello/views.py`, crie a view que retorna "Hello, World!":

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! Bem-vindo ao app Hello!")
```

---

#### **4. Configurar as URLs da Aplicação `hello`**

Crie um arquivo `urls.py` dentro da pasta `hello/` (caso ainda não exista) e configure-o da seguinte forma:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),  # Rota para "Hello, World!"
]
```

---

#### **5. Configurar as URLs do Projeto**

No arquivo `myproject/urls.py`, inclua o roteamento para a aplicação `hello`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Rota para o painel de administração
    path('', include('hello.urls')),         # Inclui as rotas do app "hello"
]
```

---

#### **6. Rodar o Servidor**

No terminal, execute:

```bash
python manage.py runserver
```

Agora, ao acessar [http://127.0.0.1:8000](http://127.0.0.1:8000), você verá a mensagem:

```
Hello, World! Bem-vindo ao app Hello!
```

---

### README.md (em Português)

Aqui está o arquivo `README.md` atualizado para refletir essa configuração:

```markdown
# 🌐 Aplicação Django - Hello App 🌟

Uma aplicação Django que exibe "Hello, World!" na página inicial, com o roteamento configurado em uma aplicação separada chamada **hello**.

---

## 🚀 Funcionalidades

- Exibe a mensagem "Hello, World!" na rota principal (`/`).
- Estrutura organizada com rotas na aplicação `hello`.

---

## 🛠️ Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

---

## 📥 Instalação

Siga os passos abaixo para configurar e executar o projeto:

1. **Clone este repositório**:
   ```bash
   git clone <url_do_repositorio>
   cd <pasta_do_projeto>
   ```

2. **Crie um ambiente virtual e ative-o**:
   ```bash
   python -m venv env
   source env/bin/activate       # Linux/MacOS
   env\Scripts\activate          # Windows
   ```

3. **Instale o Django**:
   ```bash
   pip install django
   ```

4. **Configure e execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

5. **Acesse a aplicação no navegador**:
   - URL: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Estrutura do Projeto

```plaintext
myproject/
│
├── hello/                 # Aplicação "Hello"
│   ├── urls.py            # Configuração de rotas da aplicação
│   ├── views.py           # View "Hello, World!"
│   ├── ...
│
├── myproject/             # Configurações do projeto Django
│   ├── settings.py        # Configurações gerais
│   ├── urls.py            # Rotas principais do projeto
│   ├── ...
│
└── manage.py              # Script de gerenciamento
```
