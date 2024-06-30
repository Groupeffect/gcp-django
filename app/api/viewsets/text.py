from rest_framework.viewsets import ModelViewSet
from api.serializers import text
from api.viewsets.mixins import MetaViewsetAdminMixin

class TextModelViewSet(MetaViewsetAdminMixin, ModelViewSet):
    serializer_class = text.TextSerializer
    filterset_fields = ['text','tags__name']

    
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return text.TextReadSerializer

        return self.serializer_class
