from email.policy import default
from django.db import models
import datetime

# Create your models here.
class curhatAdmin(models.Model):
    date = models.DateField(default = datetime.date.today)
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)