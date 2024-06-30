from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class MetaModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sorting = models.FloatField(default=0.1)
    public = models.BooleanField(default=True)
    show_to_authenticated = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Tagging(MetaModel, models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


def upload_picture(instance, filename):
    return "pictures/{filename}".format(filename=filename)


class Picture(MetaModel, models.Model):
    picture = models.ImageField(upload_to=upload_picture)
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    tags = models.ManyToManyField(Tagging, blank=True)

    class Meta:
        ordering = ["sorting"]

    def __str__(self):
        return self.name


class Text(MetaModel, models.Model):
    text = models.TextField()
    link = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tagging, blank=True)

    class Meta:
        ordering = ["sorting"]

    def __str__(self):
        return self.text


class Card(MetaModel, models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    picture = models.ForeignKey(
        Picture, on_delete=models.CASCADE, blank=True, null=True
    )
    links = models.JSONField(blank=True, null=True, default=list)
    texts = models.ManyToManyField(Text, blank=True)
    text = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tagging, blank=True)

    class Meta:
        ordering = ["sorting"]

    def __str__(self):
        return self.name

class AssetJson(MetaModel,models.Model):
    name = models.CharField(max_length=200, unique=True)
    json = models.JSONField(blank=True, null=True, default=dict)
    tags = models.ManyToManyField(Tagging, blank=True)
    members = models.ManyToManyField(User, blank=True)
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name