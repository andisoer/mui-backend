from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Konsultasi

class KonsultasiSerializer(ModelSerializer):
    class Meta:
        model = Konsultasi
        fields = ['id', 'nama', 'email', 'nomor_telepon', 'topik', 'pesan','date']
    