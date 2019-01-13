from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
