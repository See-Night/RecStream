#!/usr/bin/python3

import requests
import sqlite3
import ffmpeg
import subprocess
import time
from pathlib import Path
from Listener import Listener

BASE_DIR = Path(__file__).resolve().parent


def updateRPID(PID, URL):
    conn = sqlite3.connect('{}/database.sqlite'.format(BASE_DIR.parent.parent))

    SQL = "UPDATE Listener_listener SET RPID = '{PID}' WHERE LiveURL = '{URL}'".format(
        PID=PID,
        URL=URL
    )

    conn.execute(SQL)
    conn.commit()
    conn.close()


def getConfig():
    conn = sqlite3.connect('{}/database.sqlite'.format(BASE_DIR.parent.parent))

    SQL = "SELECT * FROM Config_config WHERE key = 'savePath'"

    cursor = list(conn.execute(SQL))

    return cursor[0][1]


class Monitor:
    port = 8000

    def __init__(self, listener: Listener):
        self.listener = listener
        self.path = getConfig()

    # Start recording and save when recording stops
    def Record(self):
        try:
            print("start recording")
            p = subprocess.Popen(
                'streamlink -o {path}/"{file_name}" {url} best'
                .format(
                    url=self.listener.url,
                    path=self.path,
                    file_name=self.listener.stream.filename
                ),
                shell=True
            )

            updateRPID(p.pid, self.listener.url)

            p.wait()

            updateRPID(None, self.listener.url)

            global BASE_DIR

            # Get Info
            info = ffmpeg.probe(
                '{}/{}'
                .format(
                    self.path,
                    self.listener.stream.filename
                )
            )

            # Save In Database
            requests.post('http://localhost:{}/VideoInfo/add'.format(self.port), data={
                'FileName': self.listener.stream.filename,
                'Title': self.listener.stream.title,
                'Time': info['format']['duration'],
                'Date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                'LiveURL': self.listener.url,
                'Resolution': '{}x{}'.format(info['streams'][1]['width'], info['streams'][1]['height']),
                'FrameRate': info['streams'][1]['r_frame_rate'],
                'VideoByteRate': info['streams'][1]['bit_rate'],
                'AudioByteRate': info['streams'][0]['bit_rate']
            })
        except KeyboardInterrupt:
            updateRPID(None, self.listener.url)
        except Exception:
            updateRPID(None, self.listener.url)
