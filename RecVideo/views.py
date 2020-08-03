from django.shortcuts import render
from RecVideo.tests import addRecordVideo, RecordList
from django.http import JsonResponse
import time


# Create your views here.


def addRecord(request):
    params = request.GET
    addRecordVideo(
        title=params['Title'],
        cover=params['Cover'],
        date=params['Date'],
        time=params['Time'],
        resolution=params['Resolution'],
        framerate=params['FrameRate'],
        videobyterate=params['VideoByteRate'],
        audiobyterate=params['AudioByteRate']
    )

    res = {
        'status': '1',
        'msg': 'OK'
    }

    return JsonResponse(res)


def getRecordList(request):
    if request.GET['date'] == "":
        date = None
    else:
        date = request.GET['date']

    res = {
        'recordlist': RecordList(date)
    }
    return JsonResponse(res)
