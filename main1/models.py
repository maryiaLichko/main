from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


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
    scores = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Teams(models.Model):
    profile_set = None
    name = models.CharField(max_length=200)
    done_tasks = models.ManyToManyField(Tasks)

    def sum(self):
        sum = self.done_tasks.all().aggregate(scores=Sum('scores'))
        return sum['scores']


class Profile(models.Model): 
    is_captain = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
