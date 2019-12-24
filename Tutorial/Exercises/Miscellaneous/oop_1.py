class Computer:
    def __init__(self,cpu,ram):
        self.cpu1=cpu
        self.ram1=ram

    def config(self):
        print("Configuration is ", self.cpu1,self.ram1)

com1= Computer('i5',16)
com2=Computer('i7',8)

com1.config()
com2.config()