from django.db import models

# Create your models here.


class Home(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    link_video = models.TextField()

    class Meta:
        ordering = ['-id']
