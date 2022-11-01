from django.db import models
from django.utils import timezone

# Create your models here.
class curhatAdmin(models.Model):
    date = models.DateField(default=timezone.now)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)