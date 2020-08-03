from django.test import TestCase
from RecVideo.models import RecordVideo
from Config.models import config


# Create your tests here.

def RecordList(date=None):
    res = []

    if date is None:
        allRec = RecordVideo.objects.all()
    else:
        allRec = RecordVideo.objects.filter(Date=date)

    for r in allRec:
        rec = {
            'id': r.id,
            'Title': r.Title,
            'Date': r.Date,
            'Cover': r.Cover,
            'Time': r.Time,
            'Resolution': r.Resolution,
            'FrameRate': r.FrameRate,
            'VideoByteRate': r.VideoByteRate,
            'AudioByteRate': r.AudioByteRate
        }
        res.append(rec)

    return res


def RecordInfo(recid):
    info = RecordVideo.objects.get(id=recid)
    res = {
        'Title': info.Title,
        'Cover': info.Cover,
        'Date': info.Date,
        'Time': info.Time,
        'Resolution': info.Resolution,
        'FrameRate': info.FrameRate,
        'VideoByteRate': info.VideoByteRate,
        'AudioByteRate': info.AudioByteRate
    }

    return res


def addRecordVideo(title, cover, date, time, resolution, framerate, videobyterate, audiobyterate):
    print(title, cover, date, time, resolution, framerate, videobyterate, audiobyterate)
    RecordVideo(
        Title=title,
        Cover=cover,
        Date=date,
        Time=str(time),
        Resolution=resolution,
        FrameRate=int(str(framerate).replace('/1', '')),
        VideoByteRate=int(videobyterate)/1024,
        AudioByteRate=int(audiobyterate)/1024
    ).save()
    config.objects.all().update(records=(config.objects.all()[0].records + 1))