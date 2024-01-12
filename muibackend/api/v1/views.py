from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from apps.dashboard.models import Item
# from .serializers import ItemSerializer
# @api_view(['GET'])
# def item_list(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return JsonResponse(serializer.data, safe=False)
from rest_framework.viewsets import ModelViewSet
from apps.dashboard.models import Item
from api.v1.serializers import ItemSerializer

class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer