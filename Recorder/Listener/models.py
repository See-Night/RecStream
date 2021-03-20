from django.db import models

# Create your models here.
class Listener(models.Model):
    LiveURL = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    Platform = models.CharField(max_length=255)
    Status = models.IntegerField()
    PID = models.CharField(max_length=255, null=True)
    RPID = models.CharField(max_length=255, null=True)
