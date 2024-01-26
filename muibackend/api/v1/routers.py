from rest_framework.routers import DefaultRouter
from api.v1.views import KonsultasiViewset  

router: DefaultRouter = DefaultRouter()

router.register(r'konsultasi', KonsultasiViewset)