# class so():
#     def __init__(self):
#         self.stack = []
#         self.help = []
#
#     def add(self, Newnum):
#         self.stack.append(Newnum)
#
#     def sor(self):
#         while self.stack:
#             num = self.stack.pop()
#             if self.help == [] or num > self.help[-1]:
#                 self.help.append(num)
#             else:
#                 while num < self.help[-1]:
#                     self.stack.append(self.help.pop())
#                 self.help.append(num)
#
#             return self.help

def sor(stack):
    help = []
    while stack:
        cur = stack.pop()
        while len(help) != 0 and help[-1] < cur:
            stack.append(help.pop())
        help.append(cur)

    while help:
        stack.append(help.pop())

    return stack

print(sor([3,2,5,4,1]))
