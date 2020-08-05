from django.db import models


# Create your models here.


class config(models.Model):
    roomid = models.CharField(max_length=15)
    UID = models.CharField(max_length=15)
    records = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    record_status = models.IntegerField(default=0)
    savepath = models.CharField(max_length=100, default='.')
    port = models.CharField(max_length=8, default='8000')
    monitorPID = models.CharField(max_length=10, default='0')
    streamlinkPID = models.CharField(max_length=10, default='0')
    command = models.IntegerField(default=0)
