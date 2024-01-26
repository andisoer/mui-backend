#from .models import User
#from django.contrib.auth import authenticate, login, logout
#from django.contrib import messages

#def login_user(request):
#    return render(request, 'authenticate/login.html', {})
#def user_list(request):
#    users = User.objects.all()
#    return render(request, 'templates/user_list.html', {'users': users})
# apps/dashboard/views.py

from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate, login  # Tambahkan impor ini
# from django.shortcuts import redirect

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             # Authentikasi pengguna
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 # Login pengguna
#                 login(request, user)
#                 return JsonResponse({'success': True, 'message': 'Login berhasil'})
#             else:
#                 # Authentikasi gagal
#                 return JsonResponse({'success': False, 'message': 'Username atau password tidak valid'})
#         else:
#             # Form validasi gagal
#             errors = dict(form.errors.items())
#             return JsonResponse({'success': False, 'errors': errors})
#     elif request.method == 'GET':
#         # Render formulir login untuk permintaan GET
#         form = AuthenticationForm()
#         return render(request, '/login', {'form': form})
#     else:
#         # Tangani metode HTTP lainnya
#         return JsonResponse({'success': False, 'message': 'Metode Tidak Diizinkan'}, status=405)

# def dashboard(request):
#     # Logika tampilan dashboard di sini
#     return render(request, '/dashboard', {})




# class LoginAPIView(APIView):
#     # Your implementation for the login view

#     def post(self, request, *args, **kwargs):
#         # Assuming you have a form that contains 'username' and 'password'
#         username = request.data.get('username')
#         password = request.data.get('password')

#         # Validate credentials
#         if not username or not password:
#             return Response(data={'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

#         # Authenticate the user
#         user = authenticate(username=username, password=password)

#         if user:
#             # Generate tokens
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)

#             return Response(data={'access_token': access_token}, status=status.HTTP_200_OK)
#         else:
#             return Response(data={'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
