class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def append(self, val):
        node = Node()
        node.val = val
        node.next = None
        if self.head == None:
            self.head = node
        else:
            p = self.head
            while p:
                if p.next != None:
                    p = p.next
                else:
                    p.next = node
                    break
    def insert(self, pos, val):
        node = Node()
        p = self.head
        i = 0
        while p:
            p = p.next
            i += 1
            if i == pos:
                break
        node.val = val
        p.next = node
        node.next = p.next.next






class LinkList(object):

    def val(self, index):
        return self.lst[index]

    def next(self, index):
        if index == len(self.lst):
            return None
        else:
            return self.lst[index + 1]

    def __init__(self):
        self.lst = []
        self.index = 0