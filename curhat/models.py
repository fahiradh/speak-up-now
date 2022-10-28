from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class curhatDong(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 520)
    contactable = models.CharField(max_length = 2)