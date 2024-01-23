from django.db import models
import os
from uuid import uuid4

def file_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid4()), ext)
    return os.path.join('static/img', filename)

# Create your models here.
class Gallery(models.Model):
    Judul = models.CharField(max_length=100)
    Gambar = models.ImageField(upload_to=file_image, verbose_name='Photo', null=True, blank=True)
    Deskripsi = models.TextField() 
    def __str__(self):
        return self.Judul
