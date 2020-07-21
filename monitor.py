#!/usr/bin/python3
import json
import os
import time
import sys
import getopt
import requests
import ffmpeg
import platform

opts, args = getopt.getopt(sys.argv[1:], "r:o:p:", ["room=", "outpath=", "port="])

record = 'off'

# 参数检测
try:
    for opt, val in opts:
        if opt in ("-r", "--room"):
            room = val
        if opt in ("-o", "--outpath"):
            path = val
        if opt in ("-p", "--port"):
            port = val
except getopt.GetoptError as e:
    sys.exit()

print("正在监听{}".format(room))

# 循环监听
try:
    while True:
        try:
            t = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
            stream_url = "streamlink --stream-url {}".format("https://live.bilibili.com/{}".format(room))
            if os.popen(stream_url).read().strip().split(':')[0] != 'error' and record == 'off':
                record = 'on'

                # get Title
                title = json.loads(requests.get('https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={}'.format(room)).text)['data']['room_info']['title']

                file_name = '{}.mp4'.format(title)
                print("Start recording {} in {}".format(file_name, t))

                # start recording
                os.system('streamlink -O https://live.bilibili.com/' + room + ' best | ffmpeg -loglevel error -i pipe:0 -vcodec copy -acodec copy -vbsf h264_mp4toannexb {}/\'{}\''.format(path, file_name))

                # get info
                info = ffmpeg.probe('{}/{}'.format(path, file_name))

                # download cover
                cover = json.loads(requests.get('https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={}'.format(room)).text)['data']['cover']
                with open('./static/image/Cover/{}.jpg'.format(title), 'wb') as f:
                    f.write(requests.get(cover).content)
                    cover = './static/image/Cover/{}.jpg'.format(title)

                # save in database
                requests.get('http://localhost:{}/addRecord'.format(port), params={
                    'Title': title,
                    'Cover': cover,
                    'Date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
                    'Resolution': '{}x{}'.format(info['streams'][0]['width'], info['streams'][0]['height']),
                    'FrameRate': info['streams'][0]['r_frame_rate'],
                    'VideoByteRate': info['streams'][0]['bit_rate'],
                    'AudioByteRate': info['streams'][1]['bit_rate']
                })

            elif os.popen('ps -ef | grep "streamlink -O" | grep -v "grep" | awk \'{print $2}\'').read().strip() == "" and record == 'on':
                record = 'off'
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("[" + time.strftime('%Y-%m-%d %H:%M:%S') + "]{}发生错误,错误信息:{}\n".format(time.localtime(time.time()), e))
            print('streamlink -O https://live.bilibili.com/' + room + ' best | ffmpeg -loglevel error -i pipe:0 -vcodec copy -acodec copy -vbsf h264_mp4toannexb {}/'.format(path) + file_name)
except KeyboardInterrupt:
    print("Monitor")