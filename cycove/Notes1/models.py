from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    detail = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
