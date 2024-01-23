from rest_framework.routers import DefaultRouter
from api.v1.views import GalleryViewset  

router: DefaultRouter = DefaultRouter()

router.register(r'gallery', GalleryViewset)