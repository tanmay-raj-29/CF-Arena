from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Contest)
admin.site.register(models.Participation)