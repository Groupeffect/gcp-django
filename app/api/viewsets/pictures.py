from rest_framework.viewsets import ModelViewSet
from api.serializers import pictures
from api.viewsets.mixins import MetaViewsetAdminMixin

class PictureModelViewSet(MetaViewsetAdminMixin, ModelViewSet):
    serializer_class = pictures.PictureSerializer
    filterset_fields = ["name", "tags__name"]

    def get_serializer_class(self):
        if self.action == "update":
            return pictures.PictureUpdateSerializer
        elif self.action == "retrieve" or self.action == "list":
            return pictures.PictureReadSerializer

        return self.serializer_class
