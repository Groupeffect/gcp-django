from rest_framework import serializers
from api import models
from api.serializers import tagging


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Text
        fields = "__all__"


class TextUpdateSerializer(TextSerializer):
    pass


class TextReadSerializer(TextSerializer):
    tags = tagging.TaggingReadSerializer(many=True, read_only=True)

    class Meta:
        model = models.Text
        fields = ["sorting","text","tags"]
