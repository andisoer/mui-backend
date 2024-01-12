# from django.urls import path
# from . import views
# urlpatterns = [ path('items/', views.item_list, name='item-list'), ]

from api.v1.routers import router

urlpatterns = [] + router.urls