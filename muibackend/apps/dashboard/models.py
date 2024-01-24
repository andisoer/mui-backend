from django.db import models

class Konsultasi(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=15)
    topik = models.CharField(max_length=50)
    pesan = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    