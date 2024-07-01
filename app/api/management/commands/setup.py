# This file is used to setup the app by creating the superuser and loading the pictures into the database
import os
import json
from django.conf import settings
from pathlib import Path
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from backend.settings import ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD
from api.serializers import pictures, tagging, text, card, assets
from shutil import rmtree

# import call command
from django.core.management import call_command

fixtures = json.loads(open(Path(settings.BASE_DIR / "api/fixtures/default.json")).read())
tags = fixtures["tags"]
default_text = fixtures["text"]
default_pictures = fixtures["pictures"]
default_cards = fixtures["cards"]
defaule_json_assets = fixtures["assetsJson"]

from django.core.files.images import ImageFile


class Command(BaseCommand):
    help = "Setup the app"

    def iter_files(self, folder_path):
        media_path = Path(settings.MEDIA_ROOT / folder_path)
        for file in os.listdir(media_path):
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                yield file

    def load_tags(self):
        """Load tags into the database"""
        model = tagging.TaggingSerializer.Meta.model
        for tag in tags:
            if not model.objects.filter(name=tag["name"]).exists():
                tag = tagging.TaggingSerializer(data=tag)
                tag.is_valid(raise_exception=True)
                tag.save()
                self.stdout.write(
                    self.style.SUCCESS(f"Tag {tag.instance.name} saved to the database")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Tag {tag['name']} already in the database")
                )
    def load_text(self):
        """Load text into the database"""
        model = text.TextSerializer.Meta.model
        for t in default_text:
            if not model.objects.filter(text=t["text"]).exists():
                tx = text.TextSerializer(data=t)
                tx.is_valid(raise_exception=True)
                tag = tagging.TaggingSerializer.Meta.model.objects.get(name=t['tag'])
                tx.save()
                tx.instance.tags.add(tag)
                self.stdout.write(
                    self.style.SUCCESS(f"text {tx.instance.id} saved to the database")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"text {t} already in the database")
                )

    def load_cards(self):
        """Load cards into the database"""
        model = card.CardSerializer.Meta.model
        for c in default_cards:
            _tags = c.pop("tags")
            _picture = c.pop("picture")
            cd = card.CardSerializer(data=c)
            if not model.objects.filter(name=c["name"]).exists():
                cd.is_valid(raise_exception=True)
                cd.save()
                tags = tagging.TaggingSerializer.Meta.model.objects.filter(name__in=_tags)
                cd.instance.tags.set(tags)
                self.stdout.write(
                    self.style.SUCCESS(f"card {cd.instance.id} saved to the database")
                )
                for picture in pictures.PictureSerializer.Meta.model.objects.filter(
                        name=_picture
                    ):
                    cd.instance.picture=picture
                    self.stdout.write(
                        self.style.SUCCESS(f"card {cd.instance.id} tagged with {picture.name}")
                    )
                    cd.instance.save()

            else:
                self.stdout.write(
                    self.style.WARNING(f"card {c} already in the database")
                )

    def load_json_assets(self):
        """Load assets into the database"""
        model = assets.AssetJsonSerializer.Meta.model
        for c in defaule_json_assets:
            _tags = c.pop("tags")
            if not model.objects.filter(name=c["name"]).exists():
                cd = assets.AssetJsonSerializer(data=c)
                cd.is_valid(raise_exception=True)
                cd.save()
                tags = tagging.TaggingSerializer.Meta.model.objects.filter(name__in=_tags)
                cd.instance.tags.set(tags)
                self.stdout.write(
                    self.style.SUCCESS(f"assets {cd.instance.id} saved to the database")
                )

            else:
                self.stdout.write(
                    self.style.WARNING(f"assets {c} already in the database")
                )

    def load_pictures(self, folder_path="pictures"):
        """Load pictures into the database from the specified folder path"""
        media_path = Path(settings.MEDIA_ROOT / folder_path)
        tags = tagging.TaggingSerializer.Meta.model.objects.filter(name="mosaik")
        for file in self.iter_files(folder_path):
            if not pictures.PictureSerializer.Meta.model.objects.filter(
                name=file
            ).exists():
                picture = pictures.PictureSerializer(
                    data={
                        # "picture": os.path.join(folder_path,str(file)),
                        "picture": ImageFile(open(media_path / file, "rb")),
                        "name": file,
                        "tags": tags.values_list("pk", flat=True),
                        "description": "auto",
                    }
                )
                picture.is_valid(raise_exception=True)
                picture.save()
                instance = picture.instance
                self.stdout.write(
                    self.style.WARNING(
                        f"Picture {file} ID: {instance.id} saved to the database and temporary file at {instance.picture.file.name}"
                    )
                )
                # remove duplicate picture from folder
                os.remove(instance.picture.file.name)
                # update the picture instance with the correct path
                picture.update(
                    instance=instance,
                    validated_data={"picture": os.path.join(folder_path, str(file))},
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Picture {file} ID: {picture.instance.id} saved to the database"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Picture {file} already in the database")
                )
        # os remove folder recursively
        app_path = os.path.join(media_path, "app")
        self.stdout.write(
            self.style.WARNING(f"removing temporaray media path: {app_path}")
        )
        if os.path.exists(app_path):
            rmtree(app_path)
            self.stdout.write(self.style.SUCCESS(f"Folder {app_path} removed"))

        # set picture tags
        for picture in default_pictures:
            pic = pictures.PictureSerializer.Meta.model.objects.get(name=picture["name"])
            pic.tags.clear()
            for tag in picture["tags"]:
                tag = tagging.TaggingSerializer.Meta.model.objects.get(name=tag)
                pic.tags.add(tag)
                self.stdout.write(
                    self.style.SUCCESS(f"Picture {pic.name} tagged with {tag.name}")
                )

    def handle(self, *args, **kwargs):
        # create the superuser
        if not User.objects.filter(username=ADMIN_USERNAME).exists():
            User.objects.create_superuser(ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD)
            self.stdout.write(self.style.SUCCESS("Created superuser"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))

        call_command("makemigrations")
        call_command("migrate")
        call_command("collectstatic", interactive=False)
        self.load_tags()
        self.load_text()
        self.load_pictures("pictures")
        self.load_cards()
        self.load_json_assets()
        self.stdout.write(self.style.SUCCESS("Setup completed successfully"))
