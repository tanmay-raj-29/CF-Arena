from django.db import models
from team.models import Team
from problem.models import Problem

# Create your models here.


class Match(models.Model):
    problems = models.ManyToManyField(Problem)
    team1 = models.OneToOneField(
        Team, null=True, on_delete=models.SET_NULL, related_name='first_team')
    team2 = models.OneToOneField(
        Team, null=True, on_delete=models.SET_NULL, related_name='second_team')
    duration = models.IntegerField(default=15)  # match duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team1.name + " | " + self.team2.name
