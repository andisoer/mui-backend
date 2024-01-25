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
