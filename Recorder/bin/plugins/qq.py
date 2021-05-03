from bs4 import BeautifulSoup
from plugins.plugin import plugin
import requests
import json
import time


class qq(plugin):
    def DetectLiveStream(self):
        api = self.url
        res = BeautifulSoup(requests.get(api).text, 'html5lib')
        info = res.find(id='__NEXT_DATA__').string
        room_data = json.loads(info)['props']['initialState']['roomInfo']['roomInfo']['room_info']
        if 'status' in room_data and room_data['status'] == 1:
            self.status = True
            self.title = room_data['room_name']
            self.filename = '{}-{}.mp4'.format(self.title, time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())))
            return True
        else:
            self.status = False
            return False
