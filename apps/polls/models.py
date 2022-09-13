import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('texto da questão', max_length=200)
    pub_date = models.DateTimeField('data publicação')
    
    def __str__(self):
        return self.question_text
    
    @admin.display(boolean=True, ordering='pub_date', description='Publicado recentemente?')
    def was_published_recently(self):
        now = timezone.now()
        yesterday = now - datetime.timedelta(days=1)
        return  yesterday <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('texto da escolha', max_length=200)
    votes = models.IntegerField('votos', default=0)

    def __str__(self):
        return self.choice_text
