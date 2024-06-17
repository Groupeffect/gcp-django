from rest_framework.routers import DefaultRouter
from api.views import HealthCheckViewset

router = DefaultRouter()
router.register(r'healthcheck', HealthCheckViewset, 'healthcheck')
urlpatterns = router.urls