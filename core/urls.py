from django.contrib import admin
#from django.shortcuts import redirect
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    # for more redirect's usage options: https://docs.djangoproject.com/en/4.1/topics/http/shortcuts/
    #path('', lambda request: redirect('polls/', permanent=False)),
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('appmodules.accounts.urls')),
    path('polls/', include('appmodules.polls.urls')),
]
