class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def print(self):
        value = self.head
        while value is not None:
            print(value.data)
            value = value.next

    def addfirst(self, element):
        newnode = Node(element)

        newnode.next = self.head
        self.head = newnode

    def addend(self, element):
        newnode = Node(element)

        if self.head is None:
            self.head = newnode
            return

        now = self.head

        while now.next:
            now = now.next
        now.next = newnode


l = Linkedlist()

e1 = Node('first')
l.head = e1

e2 = Node('second')
l.head.next = e2

e3 = Node('third')
e2.next = e3

n = 'four'
l.addfirst(n)

l.addend('adjkalsdjalsdlask')

l.print()
