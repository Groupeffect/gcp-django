from rest_framework.viewsets import ModelViewSet
from api.serializers import card
from api.viewsets.mixins import MetaViewsetAdminMixin

class CardModelViewSet(MetaViewsetAdminMixin, ModelViewSet):
    serializer_class = card.CardSerializer
    filterset_fields = ['tags__name']

    
    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return card.CardReadSerializer

        return self.serializer_class
