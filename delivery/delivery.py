class Delivery:
    def __init__(self, number):
        self.number = number

    def get_notification(self):
        return Notification("", True, "测试快递消息")


class Notification:
    def __init__(self, error, have_update, latest_msg):
        self.error = error
        self.have_update = have_update
        self.latest_msg = latest_msg
