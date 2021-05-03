from plugins.plugin import plugin
import requests
import json
import time

class bilibili(plugin):
    def DetectLiveStream(self):
        room_id = self.url.replace('https://live.bilibili.com/', '')
        api = 'https://api.live.bilibili.com/room/v1/Room/get_info?id={room_id}'.format(room_id=room_id)
        res = json.loads(requests.get(api).text)
        status = res['data']['live_status']
        if status == 0:
            self.status = False
            return False
        else:
            self.status = True
            self.title = res['data']['title']
            self.filename = '{}-{}.mp4'.format(
                self.title, 
                time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
            )
            return True