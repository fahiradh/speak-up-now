from django.db import models

# Create your models here.
class curhatAdmin(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)