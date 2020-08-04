import os
import platform
import getopt
import sys
import sqlite3
import multiprocessing
import signal
from monitor import Monitor

def rec():
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    room = cur.execute('select roomid from Config_config').fetchall()[0][0]
    uid = cur.execute('select UID from Config_config').fetchall()[0][0]
    path = cur.execute('select savepath from Config_config').fetchall()[0][0]
    port = cur.execute('select prot from Config_config').fetchall()[0][0]
    print('start linsten room {}'.format(room))
    m = Monitor(
        room=room,
        uid=uid,
        path=path,
        port=port
    )
    while True:
        try:
            if not m.DetectLiveStream():
                continue
            m.getTitle()
            m.setFileName()
            m.getCover()
            m.Record()
        except Exception as e:
            print("ERROR: {}".format(e))
            continue
        except KeyboardInterrupt as k:
            continue
    print('stop')


if __name__ == '__main__':
    rec()