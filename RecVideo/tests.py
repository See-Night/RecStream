from django.test import TestCase
from RecVideo.models import RecordVideo


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
            'Date': r.Date
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
    RecordVideo(
        Title=title,
        Cover=cover,
        Date=date,
        Time=time,
        Resolution=resolution,
        FrameRate=framerate,
        VideoByteRate=videobyterate,
        AudioByteRate=audiobyterate
    ).save()