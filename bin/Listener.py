#/usr/bin/python3

import re
from plugins.bilibili import bilibili

class Listener:
    def __init__(self, url):
        self.url = url
        self.RecognitionPlatform()

    def RecognitionPlatform(self):
        regular = r'http[s]?:\/\/([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)\.?([a-zA-Z0-9]+)?'
        groups = re.match(regular, self.url).groups()
        self.platform = groups[-2]

        if self.platform == 'bilibili':
            self.stream = bilibili(self.url)
    
    def DetectLiveStream(self):
        if self.stream.DetectLiveStream():
            return True
        else:
            return False
