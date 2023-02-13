import requests

from notify.notify import Notify


class ServerJiang(Notify):
    def __init__(self, key):
        super().__init__(key)

    def send(self, title, message):
        url = "https://sctapi.ftqq.com/{}.send".format(self.key)
        data = {
            "title": title,
            "desp": message,
        }
        req = requests.post(url, data=data)
