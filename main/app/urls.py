
from rest_framework import routers
from .views import UserViewSet, ClientViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls

