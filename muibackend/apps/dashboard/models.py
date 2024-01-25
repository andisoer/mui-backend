from django.db import models
from django.contrib.auth.models import User
import uuid

class Konsultasi(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=15)
    topik = models.CharField(max_length=50)
    pesan = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

def upload_to_func(instance, filename):
    extension = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4().hex}.{extension}"
    return f"files/{new_filename}" 

class Fatwa(models.Model):
    title = models.CharField(max_length=255)
    no_fatwa = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to=upload_to_func, null=True, blank=True)
    lampiran_fatwa = models.FileField(upload_to=upload_to_func, null=True, blank=True)
    keterangan = models.TextField()
    date = models.DateField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
