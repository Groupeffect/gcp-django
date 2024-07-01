import os
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from api.serializers import assets
from api.viewsets.mixins import MetaViewsetAdminMixin
from backend.settings import ALLOWED_HOSTS,CORS_ALLOWED_ORIGINS,CSRF_TRUSTED_ORIGINS, DATABASES, REST_FRAMEWORK, MEDIA_ROOT, STATIC_ROOT

class AssetJsonModelViewSet(MetaViewsetAdminMixin, ModelViewSet):
    serializer_class = assets.AssetJsonSerializer
    filterset_fields = ["tags__name"]

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return assets.AssetJsonReadSerializer

        return self.serializer_class


class AdminAssetJsonView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):

        data = os.environ.copy()
        for i in [
            "SUPABASE_URL",
            "SUPABASE_TOKEN",
            "ADMIN_PASSWORD",
            "SUPABASE_JWT",
            "SUPABASE_SERVICE_ROLE_KEY",
            "GPG_KEY",
            "SECRET_KEY",
            "SUPABASE_DB_PASSWORD",
            "PYTHON_GET_PIP_SHA256"
        ]:
            if i in data:
                data.pop(i)

        return Response(data={
            "osenv":data,
            "CORS_ALLOWED_ORIGINS":CORS_ALLOWED_ORIGINS,
            "CSRF_TRUSTED_ORIGINS":CSRF_TRUSTED_ORIGINS,
            "ALLOWED_HOSTS":ALLOWED_HOSTS,
            "DATABASES":DATABASES["default"]["ENGINE"],
            "REST_FRAMEWORK":REST_FRAMEWORK,
            "MEDIA_ROOT":str(MEDIA_ROOT),
            "STATIC_ROOT":str(STATIC_ROOT)
        })
