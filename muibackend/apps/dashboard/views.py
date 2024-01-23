from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Fatwa
from .serializers import FatwaSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class FatwaListCreateView(generics.ListCreateAPIView):
    queryset = Fatwa.objects.all()
    serializer_class = FatwaSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        # Set the user who uploaded the file
        uploaded_by = self.request.user if self.request.user.is_authenticated else None

        # Automatically set the uploaded_by field
        serializer.save(uploaded_by=uploaded_by)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Check if a new thumbnail is provided
            if 'thumbnail' not in request.data:
                serializer.validated_data['thumbnail'] = instance.thumbnail

            # Check if a new lampiran_fatwa is provided
            if 'lampiran_fatwa' not in request.data:
                serializer.validated_data['lampiran_fatwa'] = instance.lampiran_fatwa

            self.perform_update(serializer)
            return Response(serializer.data)

        return Response(serializer.errors)

class FatwaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatwa
        fields = ['id', 'title', 'keterangan', 'no_fatwa', 'date', 'thumbnail', 'lampiran_fatwa']

    def create(self, validated_data):
        # Create an instance without requiring thumbnail and lampiran_fatwa
        return Fatwa.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update only if thumbnail or lampiran_fatwa are provided
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.no_fatwa = validated_data.get('no_fatwa', instance.no_fatwa)
        instance.keterangan = validated_data.get('keterangan', instance.keterangan)
        
        thumbnail_file = validated_data.get('thumbnail')
        if thumbnail_file:
            instance.thumbnail = thumbnail_file

        lampiran_file = validated_data.get('lampiran_fatwa')
        if lampiran_file:
            instance.lampiran_fatwa = lampiran_file

        instance.save()
        return instance

class FatwaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fatwa.objects.all()
    serializer_class = FatwaSerializer
