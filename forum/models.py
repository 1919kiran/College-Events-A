import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=300)
    def __str__(self):
        return self.question_text


class Answer(models.Model):
#    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer_text=models.CharField(max_length=500)
    question_id_of_answer=models.IntegerField(default=0)
    #votes=models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text




