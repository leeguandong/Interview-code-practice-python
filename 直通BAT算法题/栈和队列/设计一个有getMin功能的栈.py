class Newstack():
    def __init__(self):
        self.stackData = []
        self.stackMin = []

    def push(self, newNum):
        self.stackData.append(newNum)
        if self.stackMin == [] or newNum <= self.getMin():
            self.stackMin.append(newNum)

    def getMin(self):
        if len(self.stackMin) == 0:
            return []
        return self.stackMin[-1]

    def pop(self):
        value = self.stackData.pop()
        if self.getMin() == value:
            self.stackMin.pop()
        return value

s = Newstack()
print(s.push(1))
print(s.pop())
print(s.push(2))
print(s.push(3))
print(s.getMin())
print(s.push(1))
