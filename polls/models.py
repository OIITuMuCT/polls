import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self) -> str:
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text

class Survey(models.Model):
    """Модель для создания опросов на сайте"""
    survey_text = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    polls_list = Question.objects.all()
    
    def showSurvey(self, question_id):
        polls = Question.objects.get(pk=question_id)
        return self.pk