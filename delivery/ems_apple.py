import requests

from delivery.delivery import Delivery,Notification


class EmsApple(Delivery):
    def __init__(self, number):
        super().__init__(number)
        self.latest_msg = self.query()

    def query(self):
        url = "https://www.ems.com.cn/apple/getMailNoRoutes"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Connection": "keep-alive",
            "Content-Length": "21",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Host": "www.ems.com.cn",
            "Origin": "https://www.ems.com.cn",
            "Referer": "https://www.ems.com.cn/apple/items?mailNo=EZ175087808CN",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Microsoft Edge\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41",
            "X-Requested-With": "XMLHttpRequest",
        }
        data = {"mailNum": self.number}
        req = requests.post(url, data=data,headers=headers)
        result = req.json()['trails'][0][0]['optime']+ req.json()['trails'][0][0]['processingInstructions']

        return result

    def get_notification(self):
        result = self.query()
        if result != self.latest_msg:
            self.latest_msg = result
            return Notification("",True,result)

        return Notification("",False,result)
