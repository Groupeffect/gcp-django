from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import GenericViewSet


class RouterViewWrapper(GenericViewSet):
    """is needed for DefaultRouter to work like APIView"""
    serializer_class = None

    def get_queryset(self):
        return []

    def get_serializer_class(self):
        return None


class HealthCheckViewset(RouterViewWrapper):

    def list(self, request, *args, **kwargs):
        data={"service":"backend","status":"ok"}
        return Response(data, status=status.HTTP_200_OK)