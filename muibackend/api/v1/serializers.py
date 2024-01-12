from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name','description']
    