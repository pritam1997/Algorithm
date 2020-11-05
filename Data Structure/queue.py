
class Queue:

    def __init__(self):
        self.queue = list()

    def add(self, data):
        if data not in self.queue :
            self.queue.insert(0, data)
            return True
        return False

    def size(self):
        return len(self.queue)
    
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return 'No Elements in Queue!'

        

q = Queue()
q.add('Mon')
q.add('Tue')
q.add('Wed')
print(q.queue)

print(q.size())
d = q.remove()

print(q.queue)

