import calendar
import datetime
from django.shortcuts import render
from RecVideo.tests import RecordList, RecordInfo
from Config.models import config


def calendarInit():
    year = datetime.date.today().year
    month = datetime.date.today().month
    FirDayWeek = calendar.monthrange(year, month)[0] + 1
    allDays = calendar.monthrange(year, month)[1]
    day = 1

    month = []
    while day <= allDays:
        week = []
        i = 0
        if day == 1:
            while i < FirDayWeek:
                week.append('')
                i += 1
        while i < 7 and day <= allDays:
            week.append(day)
            day += 1
            i += 1
        if i < 7:
            while i < 7:
                week.append('')
                i += 1
        month.append(week)
    return month


def index(request):
    context = {
        'room_id': config.objects.all()[0].roomid,
        'records': config.objects.all()[0].records,
        'status': config.objects.all()[0].status,
        'month': calendarInit(),
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
        'page': "HomePage",
        'RecordList': RecordList()
    }
    return render(request, 'index.html', context)


def Record(request):
    if request.GET and request.GET['date'] and request.GET['date'] != '':
        RecList = RecordList(request.GET['date'])
    else:
        RecList = RecordList()
    context = {
        'month': calendarInit(),
        'navs': [
            {
                'text': '主页',
                'toPage': 'Home',
                'active': False
            },
            {
                'text': '录播',
                'toPage': 'Record',
                'active': True
            }
        ],
        'page': "RecordPage",
        'RecordList': RecList
    }
    return render(request, 'index.html', context)


def Info(request):
    if 'id' in request.GET:
        id = request.GET['id']
    else:
        id = 1
    context = {
        'month': calendarInit(),
        'navs': [
            {
                'text': '主页',
                'toPage': 'Home',
                'active': False
            },
            {
                'text': '录播',
                'toPage': 'Record',
                'active': False
            }
        ],
        'page': "RecordInfo",
        'info': RecordInfo(id)
    }

    return render(request, 'index.html', context)
