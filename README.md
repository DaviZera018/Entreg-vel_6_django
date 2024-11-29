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
