class Notify:
    def __init__(self,key):
        self.key = key

    def send(self,title,message):
        print(title,message)