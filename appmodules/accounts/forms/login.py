from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField, PasswordInput


class LoginForm(AuthenticationForm):
    username = CharField(label='Usuário')
    password = CharField(label='Senha', widget=PasswordInput)
