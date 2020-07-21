from django.db import models


# Create your models here.

class RecordVideo(models.Model):
    Title = models.CharField(max_length=50)
    Cover = models.CharField(max_length=100)
    Date = models.DateField(max_length=10)
    Time = models.CharField(max_length=20)
    Resolution = models.CharField(max_length=20)
    FrameRate = models.IntegerField()
    VideoByteRate = models.IntegerField()
    AudioByteRate = models.IntegerField()
