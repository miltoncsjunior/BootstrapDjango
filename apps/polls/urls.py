from apps.polls.views.detail import DetailView
from apps.polls.views.index import IndexView
from apps.polls.views.results import ResultsView
from django.urls import path

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', ResultsView.vote, name='vote'),
]
