from django.db import models
from curhat.models import curhatDong

# Create your models here.
class curhatAdmin(models.Model):
    curhat_user = models.ForeignKey(curhatDong, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)