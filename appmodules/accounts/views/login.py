from appmodules.accounts.forms.login import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class LoginView(LoginView):
    def get(self, request):
        data = {'form': LoginForm()}
        return render(request, 'accounts_login.html', data)

    def post(self, request):
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request=request, user=user)
                    return HttpResponseRedirect(reverse('polls:index'))

        data = {
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, 'accounts_login.html', data)
