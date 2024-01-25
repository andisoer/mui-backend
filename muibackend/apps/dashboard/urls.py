from django.urls import path
from .views import LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    # Other URL patterns for your app
]

#     path('dashboard/', include('apps.dashboard.urls')),
     #path('users/', include('django.contrib.auth.urls')),
     #path('login_user', views.login_user, name="login")
#admin.sites.site_header = "Halaman Admin"
#admin.sites.site_header = "Browser Title"
#admin.sites.site_index = "Selamat Datang Di Area Admin..."
