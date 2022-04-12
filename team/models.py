from django.db import models
from users.models import User

# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=25, default="TeamX")
    users = models.ManyToManyField(User, related_name='team_member')
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name
