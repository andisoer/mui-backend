from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import uuid
import os
from uuid import uuid4

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


#class User(AbstractUser):
#    name = models.CharField(max_length=255)
#    email = models.CharField(max_length=255, unique=True)
#    password = models.CharField(max_length=255)
#    username = None

#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = []

def file_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('static/img', filename)

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

class Gallery(models.Model):
    Judul = models.CharField(max_length=100)
    Gambar = models.ImageField(upload_to=file_image, verbose_name='Photo')
    Deskripsi = models.TextField() 
    def __str__(self):
        return self.Judul
