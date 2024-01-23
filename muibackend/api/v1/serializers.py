from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Gallery
from rest_framework import serializers

class GallerySerializer(ModelSerializer):

    # Gambar = serializers.ImageField(required=False)

    class Meta:
        model = Gallery
        fields = ['id','Judul','Gambar','Deskripsi']
    