class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLink(object):
    def __init__(self, node=None):
        self.__node = node

    def is_empty(self):
        return self.__node == None

    def length(self):
        cur = self.__node
        cout = 0
        while cur != None:
            cout += 1
            cur = cur.next
        print(cout)

    def travel(self):
        cur = self.__node
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self.__node
        self.__node = node

    def append(self, item):
        node = Node(item)
        cur = self.__node
        if self.is_empty():
            self.__node = node
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            cur = self.__node
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        cur = self.__node
        pre = None
        while cur !=None:
            if cur.elem == item:
                if cur == self.__node:
                    self.__node = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self,item):
       cur = self.__node
       while cur !=None:
           if cur.elem == item:
               return  True
           else:
               cur = cur.next
       return False








