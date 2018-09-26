class TwostackQueue():
    def __init__(self):
        self.stackpush = []
        self.stackpop = []

    def add(self,Newnum):
        self.stackpush.append(Newnum)

    def push(self):
        while self.stackpush:
             self.stackpop.append(self.stackpush.pop())
        return self.stackpop.pop()

queue = TwostackQueue()
queue.add([1,2,3])
print(queue.push())



