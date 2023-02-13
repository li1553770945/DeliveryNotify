class Query:
    def __init__(self,number):
        self.number = number

    def get_notification(self):
        return Notification(None)


class Notification:
    def __init__(self, msg,error_msg=""):
        self.error_msg = error_msg
        self.msg = msg
