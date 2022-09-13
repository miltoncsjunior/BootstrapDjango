from appmodules.accounts.forms.signup import SignupForm
from django.contrib.auth.models import User
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
