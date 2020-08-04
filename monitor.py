#!/usr/bin/python3
import json
import sys
import requests
import ffmpeg
import platform
import sqlite3
import time
import streamlink
import subprocess

class Monitor:
    port = 8000
    path = '.'

    def __init__(self, room, uid, port=8000, path='.'):
        self.room = room
        self.uid = uid
        self.port = port
        self.path = path

    def DetectLiveStream(self):
        streams = len(streamlink.streams("https://live.bilibili.com/{}".format(self.room)))
        if streams == 0:
            return False
        else:
            return True

    def getTitle(self):
        res = requests.get('https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom?room_id={}'.format(self.room)).text
        self.Title = json.loads(res)['data']['room_info']['title']

    def setFileName(self):
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        rl = requests.get('http://localhost:{}/getRecordList?date={}'.format(self.port, date))
        rl = json.loads(rl.text)['recordlist']
        const = 0
        for r in rl:
            if self.Title == r['Title']:
                const += 1
        self.file_name = "{}-part{}.mp4".format(self.Title, const)
    
    def getCover(self):
        res = requests.get('https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid={}'.format(self.uid)).text
        cover = json.loads(res)['data']['cover']
        with open('./static/image/Cover/{}.jpg'.format(self.Title), 'wb') as f:
            f.write(requests.get(cover).content)
            self.cover = './static/image/Cover/{}.jpg'.format(self.Title)

    def Record(self):
        print("start recording")
        p = subprocess.Popen('streamlink -O https://live.bilibili.com/{0} best | ffmpeg -y -loglevel error -i pipe:0 -vcodec copy -acodec copy -vbsf h264_mp4toannexb  {1}/"{2}" >> log'.format(self.room, self.path, self.file_name), shell=True)

        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        id = c.execute('SELECT id FROM Config_config').fetchall()[0][0]
        c.execute('UPDATE Config_config SET streamlinkPID = \'{}\' WHERE rowid = {}'.format(p.pid, id))
        conn.commit()
        conn.close()

        p.wait()

        # Get Info
        info = ffmpeg.probe('{}/{}'.format(self.path, self.file_name))

        # Save In Database
        requests.get('http://localhost:{}/addRecord'.format(self.port), params={
            'Title': self.Title,
            'Cover': self.cover,
            'Date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
            'Time': info['format']['duration'],
            'Resolution': '{}x{}'.format(info['streams'][0]['width'], info['streams'][0]['height']),
            'FrameRate': info['streams'][0]['r_frame_rate'],
            'VideoByteRate': info['streams'][0]['bit_rate'],
            'AudioByteRate': info['streams'][1]['bit_rate']
        })
