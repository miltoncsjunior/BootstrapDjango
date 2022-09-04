from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse


class LogoutView(LoginRequiredMixin, LogoutView):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))
