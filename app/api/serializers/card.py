from rest_framework import serializers
from api import models
from api.serializers import tagging
from api.serializers import text, pictures

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        fields = "__all__"


class CardUpdateSerializer(CardSerializer):
    pass


class CardReadSerializer(CardSerializer):
    tags = tagging.TaggingReadSerializer(many=True, read_only=True)
    texts = text.TextReadSerializer(many=True, read_only=True)
    picture = pictures.PictureReadSerializer(read_only=True)
    class Meta:
        model = models.Card
        fields = ["sorting","text","texts","tags","picture","title","name","links"]
