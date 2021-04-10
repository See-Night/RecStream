from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Listener
from pathlib import Path
import subprocess
import platform
import os
import signal

BASE_DIR = Path(__file__).resolve().parent


def PlatForm():
    if platform.system() == "Windows":
        return "python"
    else:
        return "python3"


def LiveURL_exist(URL):
    try:
        Listener.objects.get(LiveURL=URL)
        return True
    except Exception:
        return False


def ListenerStatus(URL):
    try:
        if Listener.objects.get(LiveURL=URL).Status == 1:
            return True
        else:
            return False
    except Exception:
        return False


def KillListener(URL):
    l = Listener.objects.get(LiveURL=URL)
    PID = l.PID
    RPID = l.RPID
    try:
        if PID:
            kill(PID)
            Listener.objects.filter(LiveURL=URL).update(PID=None)
        if RPID:
            kill(RPID)
            Listener.objects.filter(LiveURL=URL).update(RPID=None)
        return True
    except Exception:
        return False


def kill(PID):
    if platform.system() == "Windows":
        os.popen("taskkill.exe /pid:{} /F /T".format(PID))
    else:
        os.kill(PID, signal.SIGKILL)


def getListener(request):
    res = []
    for listener in Listener.objects.all():
        res.append({
            'LiveURL': listener.LiveURL,
            'Name': listener.Name,
            'Status': listener.Status
        })
    return JsonResponse(res, safe=False)


@csrf_exempt
def addListener(request):
    LiveURL = request.POST['LiveURL']
    Name = request.POST['Name']
    Status = request.POST['Status']
    Platform = request.POST['Platform']
    try:
        newListener = Listener(LiveURL=LiveURL, Name=Name, Status=Status, Platform=Platform)
        newListener.save()
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
def delListener(request):
    LiveURL = request.POST['LiveURL']
    try:
        oldListener = Listener.objects.get(LiveURL=LiveURL)
        oldListener.delete()
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
def startListener(request):
    LiveURL = request.POST['LiveURL']

    try:
        if LiveURL_exist(LiveURL) and not ListenerStatus(LiveURL):
            p = subprocess.Popen(
                '{platform} {base_dir}/bin/Controller.py --url {url}'
                .format(
                    platform=PlatForm(),
                    base_dir=BASE_DIR.parent,
                    url=LiveURL
                ),
                shell=True
            )

            Listener.objects.filter(
                LiveURL=LiveURL
            ).update(Status=1, PID=p.pid)
            return JsonResponse({
                'status': True,
                'msg': 'OK'
            })
        else:
            return JsonResponse({
                'status': False,
                'msg': 'URL is not exist'
            })

    except Exception as e:
        return JsonResponse({
            'status': 0,
            'msg': e
        })


@csrf_exempt
def stopListener(request):
    LiveURL = request.POST['LiveURL']
    try:
        if LiveURL_exist(LiveURL) and ListenerStatus(LiveURL):
            if KillListener(LiveURL):
                Listener.objects.filter(LiveURL=LiveURL).update(
                    Status=0
                )
                return JsonResponse({
                    'status': True,
                    'msg': 'OK'
                })
            else:
                return JsonResponse({
                    'status': False,
                    'msg': 'Error'
                })
    except Exception as e:
        return JsonResponse({
            'status': False,
            'msg': e
        })