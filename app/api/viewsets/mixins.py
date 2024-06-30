from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Q


class MetaViewsetAdminMixin:
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.serializer_class.Meta.model.objects.filter(
                Q(public=True) | Q(show_to_authenticated=True)
            )
        if self.request.user.is_superuser:
            return self.serializer_class.Meta.model.objects.all()
        return self.serializer_class.Meta.model.objects.filter(public=True)

    def set_auth_config(self):
        if self.request.user.is_superuser:
            self.permission_classes = [IsAdminUser]
            self.http_method_names = [
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "options",
            ]
        else:
            self.http_method_names = ["get", "options"]
            self.permission_classes = [IsAuthenticatedOrReadOnly]

    def dispatch(self, request, *args, **kwargs):
        self.set_auth_config()
        return super().dispatch(request, *args, **kwargs)
