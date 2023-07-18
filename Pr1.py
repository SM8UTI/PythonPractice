class Computer:

    def __init__(self,cpu,ram):
        self.cpuName = cpu
        self.ramSize = ram

    def MinSystem(self):
        print("Min System : ",self.cpuName,self.ramSize)
    

com = Computer("Ryzen 5",16)


Computer.MinSystem(com)