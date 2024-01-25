from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters
from .models import Home
from .serializers import HomeSerializer


class ListCreateHomeAPIView(ListCreateAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return super().get_permissions()


class RetrieveUpdateDestroyHomeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()
    permission_classes = [IsAuthenticated]
