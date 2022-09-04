from django.forms import CharField, Form, PasswordInput


class SignupForm(Form):
    username = CharField(label='Usuário')
    password1 = CharField(label='Senha', widget=PasswordInput)
    password2 = CharField(label='Confirme', widget=PasswordInput)
