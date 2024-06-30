from rest_framework.viewsets import ModelViewSet
from api.serializers import assets
from api.viewsets.mixins import MetaViewsetAdminMixin

class AssetJsonModelViewSet(MetaViewsetAdminMixin, ModelViewSet):
    serializer_class = assets.AssetJsonSerializer
    filterset_fields = ['tags__name']

    
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return assets.AssetJsonReadSerializer

        return self.serializer_class
