from appmodules.accounts.views.index import IndexView
from appmodules.accounts.views.login import LoginView
from appmodules.accounts.views.logout import LogoutView
from appmodules.accounts.views.signup import SignupView
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
