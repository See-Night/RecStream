import getopt
import sys
import time
from Recorder import Monitor
from Listener import Listener

opts, args = getopt.getopt(sys.argv[1:], "", ["url="])
url = ''

try:
    for opt, val in opts:
        if opt == "--url":
            url = val
except getopt.GetoptError as e:
    sys.exit()


def rec(url):
    l = Listener(url)
    m = Monitor(l)
    print('start')
    while True:
        if l.DetectLiveStream():
            m.Record()
        time.sleep(120)



if __name__ == "__main__":
    rec(url)
