#/usr/bin/python3

import re
from plugins.bilibili import bilibili
from plugins.huya import huya
from plugins.douyu import douyu
from plugins.qq import qq

class Listener:
    def __init__(self, url):
        self.url = url
        self.RecognitionPlatform()

    def RecognitionPlatform(self):
        regular = r'http[s]?:\/\/([a-zA-Z0-9]+\.)?([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)'
        self.platform = re.match(regular, self.url).groups(2)

        if self.platform == 'bilibili':
            self.stream = bilibili(self.url)
        if self.platform == 'huya':
            self.stream = huya(self.url)
        if self.platform == 'douyu':
            self.stream = douyu(self.url)
        if self.platform == 'qq':
            self.stream = qq(self.url)
    
    def DetectLiveStream(self):
        if self.stream.DetectLiveStream():
            return True
        else:
            return False
