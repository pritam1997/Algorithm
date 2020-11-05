
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class doubly:

    def __init__(self):
        self.head = None

    def add(self, data):
        Newnode = Node(data)
        Newnode.next = self.head
        if self.head is not None:
            self.head.prev = Newnode
        self.head = Newnode

    def listprint(self):
        node = self.head
        while node is not None:
            
            print(node.data)
            node = node.next

    # def


d = doubly()
d.add('first')
d.add('second')
d.add('third')
d.add('fourth')

d.listprint()
