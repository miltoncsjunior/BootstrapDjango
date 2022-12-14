from apps.polls.models import Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'polls_index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
