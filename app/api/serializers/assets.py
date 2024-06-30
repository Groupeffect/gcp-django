from rest_framework import serializers
from api import models
from api.serializers import tagging

class AssetJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssetJson
        fields = "__all__"


class AssetJsonReadSerializer(AssetJsonSerializer):
    tags = tagging.TaggingReadSerializer(many=True, read_only=True)
    class Meta:
        model = models.AssetJson
        fields = ["json","name","tags"]
