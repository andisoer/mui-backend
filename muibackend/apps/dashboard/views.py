from django.shortcuts import render
from rest_framework import generics
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

class FatwaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fatwa.objects.all()
    serializer_class = FatwaSerializer
