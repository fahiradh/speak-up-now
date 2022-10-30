from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class laporanResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Isinya user yang isi case namenya
    admin_name = models.CharField(max_length=60) # Username admin yang merespon
    case_name = models.CharField(max_length=30) # Judul case namenya
    status_case = models.BooleanField() # Status case apakah diterima(diproses atau tidak)
    admin_response = models.CharField(max_length=100) # Pesan khusus dari admin