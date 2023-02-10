class MyQ:
    def __init__(self):
        self.queue=list()
        
    def add2Q(self,dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        else:
            return False
    
    def size(self):
        return len(self.queue)

    def show(self):
        return self.queue
    
    def delet(self):
        self.queue.pop()

    def delet1(self):
        self.queue.pop(0)

        

TheQ=MyQ()
TheQ.add2Q('mon')
TheQ.add2Q('Tue')
TheQ.add2Q('Fri')
print(TheQ.show())
TheQ.delet1()
print(TheQ.show())