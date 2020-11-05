
class Dequeue:

    def __init__(self):
        self.queue = []


    def append(self, data):
        return self.queue.append(data)

    def appendleft(self, data):
        return self.queue.insert(0 , data)
    
    def popright(self, data):
        return self.queue.remove(self.queue[0])

    def pop(self):
        return self.queue.pop()
    
    def __repr__(self):
        return f'{self.queue}'

d = Dequeue()
d.append('first')
d.append('second')
d.append('third')

print(d)
