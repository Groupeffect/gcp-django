from rest_framework import serializers
from api import models


class TaggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tagging
        fields = "__all__"


class TaggingUpdateSerializer(TaggingSerializer):
    pass


class TaggingReadSerializer(TaggingSerializer):
    class Meta:
        model = models.Tagging
        fields = ["sorting","name"]
