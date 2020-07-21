from django.db import models

# Create your models here.


class config(models.Model):
    roomid = models.CharField(max_length=15)
    records = models.IntegerField(default=0)
    status = models.BooleanField(default=True)