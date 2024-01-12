from rest_framework.routers import DefaultRouter
from api.v1.views import ItemViewset  

router: DefaultRouter = DefaultRouter()

router.register(r'item', ItemViewset)