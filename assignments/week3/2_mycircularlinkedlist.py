class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None and current != self.tail:
            s = s + " -> " + str(current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.head == None:
            self.tail = ListNode(e,self)
            self.tail.next = self.tail
        else:
            self.tail.next = ListNode(e,self.tail.next)
            self.tail = self.tail.next

    def delete(self,e):
        if self.tail:
            if self.tail.data == e:
                if self.tail.next == self.tail:
                    self.tail = None
                else:
                    self.tail = self.tail.next
            else:
                current = self.tail
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current

if __name__ == '__main__':
    mylist =  MyLinkedList()
    print(mylist)
    mylist.addLast(1)
    mylist.addLast(2)
    mylist.addLast(3)
    print(mylist)
    mylist.delete(2)
    print(mylist)
    mylist.delete(1)
    print(mylist)
    mylist.delete(3)
    print(mylist)
