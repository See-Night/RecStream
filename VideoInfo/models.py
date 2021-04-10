from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class VideoInfo(models.Model):
    FileName = CharField(max_length=255, primary_key=True)
    Title = CharField(max_length=255)
    Time = CharField(max_length=255)
    Date = CharField(max_length=255)
    LiveURL = CharField(max_length=255)
    Resolution = CharField(max_length=255)
    FrameRate = CharField(max_length=255)
    AudioByteRate = CharField(max_length=255)