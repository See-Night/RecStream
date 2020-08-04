from django.shortcuts import render
from RecVideo.tests import RecordList
from Config.models import config
from django.http import JsonResponse
import platform
import subprocess
import signal
import os


def index(request):
    if request.GET and request.GET['date'] and request.GET['date'] != '':
        RecList = RecordList(request.GET['date'])
    else:
        RecList = RecordList()
    context = {
        'room_id': config.objects.all()[0].roomid,
        'savepath': config.objects.all()[0].savepath,
        'records': config.objects.all()[0].records,
        'status': config.objects.all()[0].status,
        'navs': [
            {
                'text': '主页',
                'toPage': 'Home',
                'active': True
            },
            {
                'text': '录播',
                'toPage': 'Record',
                'active': False
            }
        ],
        'UID': config.objects.all()[0].UID,
        'record_status': config.objects.all()[0].record_status,
        'RecordList': RecList
    }
    return render(request, 'index.html', context)


def MonitorControl(request):
    code = int(request.GET['code'])
    if platform.system() == "Windows":
        py = "python"
        s = signal.SIGTERM
    else:
        py = "python3"
        s = signal.SIGKILL
    try:
        if code == 1:
            p = subprocess.Popen("{} start.py".format(py), shell=True)
            config.objects.all().update(
                record_status=1,
                monitorPID=str(p.pid)
            )
        elif code == 0:
            p = int(config.objects.all()[0].monitorPID)
            if platform.system() == "Windows":
                os.popen('taskkill.exe /pid:{}'.format(p))
            else:
                os.kill(p, s)
            config.objects.all().update(
                record_status=0,
                monitorPID='0'
            )
        elif code == -1:
            p = config.objects.all()[0].monitorPID
            if platform.system() == "Windows":
                os.popen('taskkill.exe /pid:' + p)
            else:
                os.kill(p, s)
            p = subprocess.Popen("{} start.py".format(py), shell=True)
            config.objects.all().update(
                record_status=1,
                monitorPID=str(p.pid)
            )
    except Exception as e:
        print(e)
    res = {
        'code': 1,
        'msg': 'OK'
    }
    return JsonResponse(res)
