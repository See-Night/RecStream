#!/usr/bin/python3

from django.conf.urls import url
import ffmpeg
import getopt
import sys
import requests
import time
import os

opts, args = getopt.getopt(sys.argv[1:], "i:f:t:u:o:", [])
input_video = ""
video_format = ""
title = ""
liveurl = ""
filename = ""

try:
    for opt, val in opts:
        if opt == "-i":
            input_video = val
        if opt == "-f":
            video_format = val
        if opt == "-t":
            title = val
        if opt == "-u":
            liveurl = val
        if opt == "-o":
            filename = val
except getopt.GetoptError as e:
    sys.exit()

def recode(input_video, video_format, title, liveurl, filename):
    stream = ffmpeg.input(input_video)
    
    params = {
        "mp4": {
            "vcodec": "libx264",
            "acodec": "aac",
        },
        "flv": {
            "vcodec": "libx264",
            "acodec": "aac",
        },
        "mov": {
        }
    }
    (
        ffmpeg
        .concat(
            stream.video, stream.audio,
            v=1, a=1
        )
        .output('{}.{}'.format(input_video[:-4], video_format), **params["{}".format(video_format)])
        .run()
    )

    info = ffmpeg.probe(
        '{}'
        .format(
            input_video
        )
    )

    video = {}
    audio = {}
    for i in info['streams']:
        if i['codec_type'] == 'video':
            video = i
        if i['codec_type'] == 'audio':
            audio = i

    hour, remainder = divmod(float(info['format']['duration']), 3600)
    minute, second = divmod(remainder, 60)

    requests.post('http://localhost:8000/VideoInfo/add',{
        'FileName': filename,
        'Title': title,
        'Time': "%02d:%02d:%02d" % (hour, minute, second),
        'Date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        'LiveURL': liveurl,
        'Resolution': '{}x{}'.format(video['width'], video['height']),
        'FrameRate': "%.2fMbps" % (int(info['format']['bit_rate'])/1048576),
        'AudioByteRate': "%.2fKbps" % (int(audio['bit_rate'])/1024)
    })


if __name__ == "__main__":
    recode(input_video, video_format, title, liveurl, filename)
