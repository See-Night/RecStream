from bs4 import BeautifulSoup
from plugins.plugin import plugin
import requests
import re
import json
import time

class douyu(plugin):
    def DetectLiveStream(self):
        api = self.url
        res = BeautifulSoup(requests.get(api).text, 'html5lib')
        title = res.find(class_="Title-header").string
        info = res.find_all('script')
        reg = r'\$ROOM\.show_status\=(\w)'
        status = re.search(reg, info[3].string.replace(' ', '').replace(';', '\n')).group(1)
        if status == '1':
            self.status = True
            self.title = title
            self.filename = '{}-{}.mp4'.format(
                self.title,
                time.strftime('%Y%m%d_  %H%M%S', time.localtime(time.time()))
            )
            return True
        else:
            self.status = False
            return False