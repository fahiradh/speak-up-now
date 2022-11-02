from django.db import models
from django.contrib.auth.models import AbstractUser

class Pengguna(AbstractUser):
    is_konsulir = models.BooleanField(default=False)