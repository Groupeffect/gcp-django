from rest_framework.viewsets import ModelViewSet
from api.serializers import tagging
from api.viewsets.mixins import MetaViewsetAdminMixin

class TaggingModelViewSet(MetaViewsetAdminMixin,ModelViewSet):
    serializer_class = tagging.TaggingSerializer
    filterset_fields = ['name']
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return tagging.TaggingReadSerializer

        return self.serializer_class