import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from .managers import PublicGraphManager

User = get_user_model()


class Graph(models.Model):
    """ A class to represent bjj digraphs """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="graphs")
    public = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, default="")

    objects = models.Manager() # default manager
    public_objects = PublicGraphManager() # manager for public graphs
