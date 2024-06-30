from django.contrib import admin
from api import models
from backend.settings import SERVICE_BRANDING
# Register your models here.

admin.site.site_title = SERVICE_BRANDING
admin.site.site_header = SERVICE_BRANDING
admin.site.register(models.Tagging)
admin.site.register(models.Picture)
admin.site.register(models.Text)
admin.site.register(models.Card)
admin.site.register(models.AssetJson)