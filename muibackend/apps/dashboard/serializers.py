# serializers.py
from rest_framework import serializers
from .models import Fatwa

class FatwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatwa
        fields = ('id', 'title', 'no_fatwa', 'thumbnail', 'lampiran_fatwa', 'keterangan', 'date')
