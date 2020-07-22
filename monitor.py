#!/usr/bin/python3
import json
import os
import time
import sys
import getopt
import requests
import ffmpeg
import platform


def Record(room, path, file_name, title, cover, port):
    os.system('streamlink -O https://live.bilibili.com/{0} best | ffmpeg -y -loglevel error -i pipe:0 -vcodec copy -acodec copy -vbsf h264_mp4toannexb  {1}/"{2}" &'.format(room, path, file_name))
    print("Recorded")
    
    # Get Info
    info = ffmpeg.probe('{}/{}'.format(path, file_name))

    # Save In Database
    print("Upload Database")
    requests.get('http://localhost:{}/addRecord'.format(port), params={
        'Title': title,
        'Cover': cover,
        'Date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
        'Time': info['format']['duration'],
        'Resolution': '{}x{}'.format(info['streams'][0]['width'], info['streams'][0]['height']),
        'FrameRate': info['streams'][0]['r_frame_rate'],
        'VideoByteRate': info['streams'][0]['bit_rate'],
        'AudioByteRate': info['streams'][1]['bit_rate']
    })
    print("Upload Successful")

if __name__ == "__main__":
    opts, args = getopt.getopt(sys.argv[1:], "r:o:p:u:", ["room=", "outpath=", "port=", "uid="])

    try:
        for opt, val in opts:
            if opt in ("-r", "--room"):
                room = val
            if opt in ("-o", "--outpath"):
                path = val
            if opt in ("-p", "--port"):
                port = val
            if opt in ("-u", "--uid"):
                uid = val
    except getopt.GetoptError as e:
        sys.exit()

    print("正在监听{}".format(room))

    while True:
        try:
            streams = len(streamlink.streams("https://live.bilibili.com/{}".format(room)))
            if streams != 0:
                # Get Title
                title = json.loads(requests.get('https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={}'.format(room)).text)['data']['room_info']['title']

                # Set File Name
                file_name = '{}.mp4'.format(title)
                
                # Get Cover
                cover = json.loads(requests.get('https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={}'.format(uid)).text)['data']['cover']
                with open('./static/image/Cover/{}.jpg'.format(title), 'wb') as f:
                    f.write(requests.get(cover).content)
                    cover = './static/image/Cover/{}.jpg'.format(title)
                
                # Record
                try:
                    Record(room, path, file_name, title, cover, port)
                except Exception:
                    print("ERROR")
                    continue

        except Exception as e:
            print("ERROR: {}".format(e))
            break