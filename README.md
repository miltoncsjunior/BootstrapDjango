# BootstrapDjango

[![Python Version](https://img.shields.io/badge/python-3.8.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.1-brightgreen.svg)](https://djangoproject.com)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-5.2-brightgreen.svg)](https://getbootstrap.com)

Este é um exemplo simples de uma aplicação usando Bootstrap 5.2 e Django 4.1, com autenticação.

## Instruções para executar o projeto localmente

Clone o repositório

```bash
git clone https://github.com/miltoncsjunior/BootstrapDjango.git
```

Instale as dependências

```bash
pip3 install -r requirements.txt
```

Aplique as atualizações de banco de dados (migrations)

```bash
python3 manage.py migrate
```

Execute o servidor de desenvolvimento

```bash
python3 manage.py runserver
```

Acesse a aplicação no seu navegador através do endereço **http://localhost:8000**