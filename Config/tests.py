from django.test import TestCase
from Config.models import config
from django.http import JsonResponse


# Create your tests here.


def updateConfig(request):
    room = request.GET['roomid']
    UID = request.GET['UID']
    records = request.GET['records']
    status = request.GET['status']
    record_status = request.GET['record_status']
    savepath = request.GET['savepath']
    if len(config.objects.all()) == 0:
        config(
            roomid=room,
            UID=UID,
            records=records,
            status=status,
            record_status=record_status,
            savepath=savepath,
        ).save()
    else:
        config.objects.all().update(
            roomid=room,
            UID=UID,
            records=records,
            status=status,
            record_status=record_status,
            savepath=savepath,
        )

    return JsonResponse({'code': 1})
