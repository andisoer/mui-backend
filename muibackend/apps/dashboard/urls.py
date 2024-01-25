from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import FatwaListCreateView, FatwaDetailView

urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('dashboard/', include('apps.dashboard.urls')),
    path('fatwa/', FatwaListCreateView.as_view(), name='fatwa-list-create'),
    path('fatwa/<int:pk>/', FatwaDetailView.as_view(), name='fatwa-detail'),
] + static(settings.FILE_URL, document_root=settings.FILE_ROOT)
