from apps.accounts.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View


class SignupView(View):

    def get(self, request):
        data = {'form': SignupForm()}
        return render(request, 'accounts_signup.html', data)

    def post(self, request):
        form = SignupForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if username and password1 and password2 and password1 == password2:

                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password1
                )

                if user:
                    return HttpResponseRedirect(reverse('accounts:login'))

        data = {
            'form': form,
            'error': form.errors.as_text
        }
        return render(request, 'accounts_signup.html', data)


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


class LogoutView(LoginRequiredMixin, LogoutView):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))
