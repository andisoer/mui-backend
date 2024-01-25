from django.shortcuts import render
#from .models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages

#def login_user(request):
#    return render(request, 'authenticate/login.html', {})
#def user_list(request):
#    users = User.objects.all()
#    return render(request, 'templates/user_list.html', {'users': users})
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics, serializers
from .models import Fatwa
from .serializers import FatwaSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

class LoginAPIView(APIView):
    # Your implementation for the login view

    def post(self, request, *args, **kwargs):
        # Assuming you have a form that contains 'username' and 'password'
        username = request.data.get('username')
        password = request.data.get('password')

        # Validate credentials
        if not username or not password:
            return Response(data={'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(data={'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.

class FatwaListCreateView(generics.ListCreateAPIView):
    queryset = Fatwa.objects.all()
    serializer_class = FatwaSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        if self.request.method == 'GET':
            # Allow public access for the list view
            return [AllowAny()]
        else:
            # Require authentication for other methods (e.g., POST for create)
            return [IsAuthenticated()]

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
