from rest_framework import serializers
from api import models
from api.serializers import tagging


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Picture
        fields = "__all__"


class PictureUpdateSerializer(PictureSerializer):
    picture = serializers.ImageField(required=False)
    path = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr != "tags":
                setattr(instance, attr, value)
        instance.tags.set(validated_data.get("tags"))
        if "picture" in validated_data:
            instance.picture = validated_data.get("picture")
        # else set the picture value to the path value
        elif "path" in validated_data and "picture" not in validated_data:
            instance.picture = validated_data.get("path")

        instance.save()
        return instance


class PictureReadSerializer(PictureSerializer):
    tags = tagging.TaggingReadSerializer(many=True, read_only=True)

    class Meta:
        model = models.Picture
        fields = ["id", "name", "picture", "description", "tags", "sorting"]
