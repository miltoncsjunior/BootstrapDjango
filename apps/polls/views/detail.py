from apps.polls.models import Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import DetailView


class DetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'polls_detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
