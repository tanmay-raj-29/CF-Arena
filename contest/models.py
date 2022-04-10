from django.db import models
from users.models import Profile

# Create your models here.


class Contest(models.Model):
    contest_id = models.IntegerField(
        blank=False, primary_key=True, db_index=True)
    contest_duration = models.IntegerField(blank=True, default=120)
    name = models.CharField(max_length=250, default='Codeforces Round #0')

    def __str__(self):
        return self.name


class Participation(models.Model):
    contest_id = models.IntegerField(
        blank=False, primary_key=True, db_index=True)
    rank = models.IntegerField(blank=False)
    rating_delta = models.IntegerField(blank=False)
    virtually = models.BooleanField(blank=False, default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.handle + ' | ' + str(self.contest_id)
