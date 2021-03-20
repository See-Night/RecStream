from django.http.response import JsonResponse
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


def addListener(request):
    URL = request.GET['URL']
    try:
        newListener = Listener(LiveURL=URL, Status=0)
        newListener.save()
        return JsonResponse({
            'status': 1,
            'msg': 'OK'
        })
    except Exception as e:
        return JsonResponse({
            'status': 0,
            'msg': e
        })


def delListener(request):
    URL = request.GET['URL']
    try:
        oldListener = Listener.objects.get(LiveURL=URL)
        oldListener.delete()
        return JsonResponse({
            'status': 1,
            'msg': 'OK'
        })
    except Exception as e:
        return JsonResponse({
            'status': 0,
            'msg': e
        })


def startListener(request):
    URL = request.GET['URL']

    try:
        if LiveURL_exist(URL) and not ListenerStatus(URL):
            p = subprocess.Popen(
                '{platform} {base_dir}/bin/Controller.py --url {url}'
                .format(
                    platform=PlatForm(),
                    base_dir=BASE_DIR.parent,
                    url=URL
                ),
                shell=True
            )

            Listener.objects.filter(
                LiveURL=URL
            ).update(Status=1, PID=p.pid)
            return JsonResponse({
                'status': 1,
                'msg': 'OK'
            })
        else:
            return JsonResponse({
                'status': 0,
                'msg': 'URL is not exist'
            })

    except Exception as e:
        return JsonResponse({
            'status': 0,
            'msg': e
        })


def stopListener(request):
    URL = request.GET['URL']
    try:
        if LiveURL_exist(URL) and ListenerStatus(URL):
            if KillListener(URL):
                Listener.objects.filter(LiveURL=URL).update(
                    Status=0
                )
                return JsonResponse({
                    'status': 1,
                    'msg': 'OK'
                })
            else:
                return JsonResponse({
                    'status': 0,
                    'msg': 'Error'
                })
    except Exception as e:
        return JsonResponse({
            'status': 0,
            'msg': e
        })
