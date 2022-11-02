from django.db import models
from django.contrib.auth.models import User
from home.models import Pengguna

# Create your models here.

class curhatDong(models.Model):
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE, null = True)
    date = models.DateField()
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 520)
    contactable = models.CharField(max_length = 2)