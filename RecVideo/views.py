from django.shortcuts import render
from RecVideo.tests import addRecordVideo
from django.http import JsonResponse

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