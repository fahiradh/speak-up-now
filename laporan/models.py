from django.db import models
# Create your models here.

class laporan(models.Model):
    name = models.CharField(max_length = 60)
    phone_num = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    case_name = models.CharField(max_length = 30)
    victim_name = models.CharField(max_length = 60)
    victim_description = models.CharField(max_length = 2000)
    crime_place = models.CharField(max_length = 100)
    chronology = models.TextField(max_length = 5000)