# apps/dashboard/urls.py
from django.urls import path
from .views import login_view, dashboard  # Ensure correct import
from .views import LoginAPIView
from django.conf import settings
from django.conf.urls.static import static

from .views import FatwaListCreateView, FatwaDetailView

urlpatterns = [
    # path('login/', login_view, name='login'), 
    # path('dashboard/', dashboard, name='dashboard'),
    # Other URL patterns for your app



#     path('dashboard/', include('apps.dashboard.urls')),
     #path('users/', include('django.contrib.auth.urls')),
     #path('login_user', views.login_user, name="login")
#admin.sites.site_header = "Halaman Admin"
#admin.sites.site_header = "Browser Title"
#admin.sites.site_index = "Selamat Datang Di Area Admin..."
    path('fatwa/', FatwaListCreateView.as_view(), name='fatwa-list-create'),
    path('fatwa/<int:pk>/', FatwaDetailView.as_view(), name='fatwa-detail'),
] + static(settings.FILE_URL, document_root=settings.FILE_ROOT)
