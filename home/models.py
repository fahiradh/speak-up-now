from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pengguna(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)