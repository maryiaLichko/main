from django.db import models
from django.db.models import ManyToManyField


class Users(models.Model):
    nickname = models.CharField(max_length=20)


class Tasks(models.Model):
    TASKS_TYPES = (
        ('specials', 'SPECIAL'),
        ('tricks', 'TRICKS'),
    )

    title = models.CharField(max_length=250)
    body = models.TextField()

    tasks_type = models.CharField(max_length=20,
                                  choices=TASKS_TYPES,
                                  default='specials')

    def __str__(self):
        return self.title


class Teams(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Users)
    done_tasks = models.ManyToManyField(Tasks)


class Score(models.Model):
    score_of_the_team: ManyToManyField = models.ManyToManyField(Teams)
