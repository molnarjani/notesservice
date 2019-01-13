from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel


class Note(TimeStampedModel, TitleSlugDescriptionModel):
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
