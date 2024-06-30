from rest_framework.routers import DefaultRouter, SimpleRouter
from api.views import HealthCheckViewSet
from api.viewsets import pictures, tagging, text, card, assets
from djoser.urls.jwt import views as jwt_views
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response



class DRFGenericViewSetWrapper(GenericViewSet):
    def get_queryset(self):
        return None

    def list(self, request):
        return Response()


class DRFJWTokenObtainPairView(jwt_views.TokenObtainPairView, DRFGenericViewSetWrapper):
    pass


class DRFJWTokenRefreshView(jwt_views.TokenRefreshView, DRFGenericViewSetWrapper):
    pass


class DRFJWTokenVerifyView(jwt_views.TokenVerifyView, DRFGenericViewSetWrapper):
    pass


router = DefaultRouter()
router.register(r"healthcheck", HealthCheckViewSet, "healthcheck")
router.register(r"pictures", pictures.PictureModelViewSet, "pictures")
router.register(r"tagging", tagging.TaggingModelViewSet, "tagging")
router.register(r"text", text.TextModelViewSet, "text")
router.register(r"card", card.CardModelViewSet, "card")
router.register(r"assets/json", assets.AssetJsonModelViewSet, "assets_json")
router.register(r"auth/jwt/create", DRFJWTokenObtainPairView, "jwt_create")
router.register(r"auth/jwt/refresh", DRFJWTokenRefreshView, "jwt_refresh")
router.register(r"auth/jwt/verify", DRFJWTokenVerifyView, "jwt_verify")

urlpatterns = router.urls
