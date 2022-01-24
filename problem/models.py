from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(default='tag', unique=True, max_length=50, blank=False)

    def __name__(self):
        return str(self.name)


class Problem(models.Model):
    contest_id = models.IntegerField(default=0, blank=False)
    index = models.CharField(max_length=10, default=0, blank=False)
    name = models.CharField(max_length=100, default='Mike', blank=False)
    rating = models.IntegerField(default=1400)
    tags = models.ManyToManyField(Tag)
    solve_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.contest_id) + str(self.index)