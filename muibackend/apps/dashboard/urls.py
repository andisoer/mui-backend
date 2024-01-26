# apps/dashboard/urls.py
from django.urls import path
from .views import login_view, dashboard  # Ensure correct import

urlpatterns = [
    # path('login/', login_view, name='login'), 
    # path('dashboard/', dashboard, name='dashboard'),
    # Other URL patterns for your app
]



#     path('dashboard/', include('apps.dashboard.urls')),
     #path('users/', include('django.contrib.auth.urls')),
     #path('login_user', views.login_user, name="login")
#admin.sites.site_header = "Halaman Admin"
#admin.sites.site_header = "Browser Title"
#admin.sites.site_index = "Selamat Datang Di Area Admin..."
