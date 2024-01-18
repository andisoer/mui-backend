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
    
    print("TEST")

    def perform_create(self, serializer):
        print("DEBUG", self.request.user)

        # Set the user who uploaded the file
        serializer.save(uploaded_by=self.request.user)

class FatwaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fatwa.objects.all()
    serializer_class = FatwaSerializer
