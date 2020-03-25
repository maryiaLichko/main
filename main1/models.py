from django.contrib.auth.models import User
from django.db import models


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
    scores = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Teams(models.Model):
    name = models.CharField(max_length=200)
    done_tasks = models.ManyToManyField(Tasks)


class Profile(models.Model):
    is_captain = models.BooleanField(default=False)
    user = models.OneToOneField(User)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
