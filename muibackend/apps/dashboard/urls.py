from django.urls import path
from .views import LoginAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import FatwaListCreateView, FatwaDetailView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', include('django.contrib.auth.urls')),
    path('fatwa/', FatwaListCreateView.as_view(), name='fatwa-list-create'),
    path('fatwa/<int:pk>/', FatwaDetailView.as_view(), name='fatwa-detail'),
] + static(settings.FILE_URL, document_root=settings.FILE_ROOT)
