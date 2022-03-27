from django.db import models

# Create your models here.
class Contest(models.Model):
    contest_id = models.IntegerField(blank=False, primary_key=True, db_index=True)
    contest_duration = models.IntegerField(blank=True, default=120)
    name = models.CharField(max_length=250, default='Codeforces Round #0')
    
    def __str__(self):
        return self.name