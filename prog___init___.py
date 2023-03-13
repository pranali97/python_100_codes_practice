# print(type(__name__))

class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # print("i5","i8","ryzen")
        print("config is", self.cpu, self.ram)


cum1 = computer("i8",32)
cum2 = computer("i9",8)
cum1.config()
cum2.config()