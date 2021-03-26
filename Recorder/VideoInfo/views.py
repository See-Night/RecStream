import os
from platform import platform
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoInfo
from Config.models import Config
from pathlib import Path

import subprocess
import platform


BASE_DIR = Path(__file__).resolve().parent


def PlatForm():
    if platform.system() == "Windows":
        return "python"
    else:
        return "python3"


@csrf_exempt
def addVideoInfo(request):
    try:
        newVideo = VideoInfo(
            FileName=request.POST['FileName'],
            Title=request.POST['Title'],
            Time=request.POST['Time'],
            Date=request.POST['Date'],
            LiveURL=request.POST['LiveURL'],
            Resolution=request.POST['Resolution'],
            FrameRate=request.POST['FrameRate'],
            AudioByteRate=request.POST['AudioByteRate']
        )
        newVideo.save()
        return JsonResponse({
            'status': True,
            'msg': 'OK'
        })
    except Exception as e:
        return JsonResponse({
            'status': False,
            'msg': e
        })


@csrf_exempt
def delVideoInfo(request):
    try:
        FileName = request.POST['FileName']
        oldVideo = VideoInfo.objects.get(FileName=FileName)
        oldVideo.delete()

        path = Config.objects.get(key="savePath").value
        os.remove('{path}/{filename}'.format(
            path=path,
            filename=FileName
        ))
        return JsonResponse({
            'status': True,
            'msg': 'OK'
        })
    except Exception as e:
        return JsonResponse({
            'status': False,
            'msg': e
        })


def getVideoInfo(request):
    res = []
    for video in VideoInfo.objects.all():
        res.append({
            'FileName': video.FileName,
            'Title': video.Title,
            'Time': video.Time,
            'Date': video.Date,
            'LiveURL': video.LiveURL,
            'Resolution': video.Resolution,
            'FrameRate': video.FrameRate,
            'AudioByteRate': video.AudioByteRate
        })
    return JsonResponse(res, safe=False)


@csrf_exempt
def recodeVideo(request):
    path = Config.objects.get(key='savePath').value
    subprocess.Popen(
        '{platform} {base_dir}/bin/recodeVideo.py -i {path}/{FileName} -f {format} -t {title} -u {url} -o {output}'
        .format(
            platform=PlatForm(),
            base_dir=BASE_DIR.parent,
            path=path,
            FileName=request.POST['FileName'],
            format=request.POST['format'],
			title=request.POST['title'],
			url=request.POST['LiveURL'],
         	output='{}.{}'.format(
         	    request.POST['FileName'][:-4], request.POST['format']
			)
        ),
        shell=True
    )
    return JsonResponse({
        'status': True,
        'msg': 'OK'
    })
