from rest_framework.routers import DefaultRouter
from api.views import HealthCheckViewSet

router = DefaultRouter()
router.register(r'healthcheck', HealthCheckViewSet, 'healthcheck')
urlpatterns = router.urls