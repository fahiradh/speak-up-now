from django.db import models

# Create your models here.

class curhatDong(models.Model):
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    descriprion = models.CharField(max_length = 520)
    contactable = models.CharField(max_length = 20)