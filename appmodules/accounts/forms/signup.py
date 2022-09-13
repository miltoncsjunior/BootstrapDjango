from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, PasswordInput


class SignupForm(UserCreationForm):
    username = CharField(label='Usuário')
    email = CharField(label='Email')
    first_name = CharField(label='Nome')
    last_name = CharField(label='Sobrenome')
    password1 = CharField(label='Senha', widget=PasswordInput)
    password2 = CharField(label='Confirme', widget=PasswordInput)
