import os
import platform
import getopt
import sys
import sqlite3
import multiprocessing


def start_django(py, p):
    os.system('{} manage.py runserver 0.0.0.0:{} --insecure'.format(py, p))


def start_monitor(py, r, p, pa, u):
    os.system('{} monitor.py -r {} -p {} -o {} -u {}'.format(py, r, p, pa, u))


if __name__ == '__main__':
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

    if platform.system() == 'Windows':
        python = 'python'
    else:
        python = 'python3'

    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    records = cur.execute('select count(*) as num from RecVideo_recordvideo').fetchall()[0][0]

    if cur.execute('select count(*) as num from Config_config').fetchall()[0][0] == 0:
        cur.execute(
            'insert into Config_config (roomid, records, status) values (\'{}\', {}, {})'.format(room, records, 'True'))
        conn.commit()
    else:
        id = cur.execute('select * from Config_config').fetchall()[0][0]
        cur.execute('update Config_config set roomid = \'{}\' where id = {}'.format(room, id))
        conn.commit()
    conn.close()

    django = multiprocessing.Process(target=start_django, args=(python, port))
    monitor = multiprocessing.Process(target=start_monitor, args=(python, room, port, path, uid))

    try:
        django.start()
        monitor.start()
        django.join()
        monitor.join()
    except Exception:
        django.close()
        monitor.close()
        print("END")