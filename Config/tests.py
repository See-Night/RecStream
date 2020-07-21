from django.test import TestCase
from Config.models import config

# Create your tests here.


def updateConfig(room, records, status):
    if len(config.objects.all()) == 0:
        config(room, records, status).save()
    else:
        config.objects.all().update(roomid=room, records=records, status=status)