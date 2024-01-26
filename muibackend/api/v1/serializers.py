from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Konsultasi
from apps.dashboard.models import Gallery

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id','Judul','Gambar','Deskripsi']

class KonsultasiSerializer(ModelSerializer):
    class Meta:
        model = Konsultasi
        fields = ['id', 'nama', 'email', 'nomor_telepon', 'topik', 'pesan','date']
    