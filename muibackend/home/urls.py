from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateHomeAPIView.as_view(), name='get_post_homes'),
    path('<int:pk>/', views.RetrieveUpdateDestroyHomeAPIView.as_view(),
         name='get_delete_update_home'),
]
