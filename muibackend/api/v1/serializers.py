from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Gallery

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id','Judul','Gambar','Deskripsi']
    