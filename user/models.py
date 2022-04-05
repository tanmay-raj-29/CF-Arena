from django.db import models

# Create your models here.
class Profile(models.Model):
    handle = models.CharField(max_length=50, default="Mike")
    rating = models.IntegerField(default=1400)
    virtual_rating = models.IntegerField(default=1400)

    def __str__(self):
        return self.handle