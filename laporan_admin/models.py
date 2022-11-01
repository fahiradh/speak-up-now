from email.policy import default
from django.db import models
from laporan.models import laporan

# Create your models here.
class laporanResponse(models.Model):
    laporan_user = models.ForeignKey(laporan, on_delete=models.CASCADE, null=True) # Laporan user
    admin_name = models.CharField(max_length=60) # Username admin yang merespon
    case_name = models.CharField(max_length=30) # Judul case namenya
    status_case = models.BooleanField(null=True) # Status case apakah diterima(diproses atau tidak)
    admin_response = models.CharField(max_length=100) # Pesan khusus dari admin