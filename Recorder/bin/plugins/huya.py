from bs4 import BeautifulSoup
from plugins.plugin import plugin
import requests
import re
import json
import time

class huya(plugin):
    def DetectLiveStream(self):
        api = self.url
        res = BeautifulSoup(requests.get(api).text, 'html5lib')
        info = res.find(attrs={'data-fixed': 'true'}).string.replace(' ','').replace(';', '\n').replace('\n\n', '\n')
        room_data = json.loads(re.search(r'varTT_ROOM_DATA=(.*)', info).group(1))
        if room_data['state'] == 'ON':
            self.status = True
            self.title = room_data['introduction']
            self.filename = '{}-{}.mp4'.format(self.title, time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())))
            return True
        else:
            self.status = False
            return False
        

