
class Stack:

    def __init__(self):
        self.stack = []

    # push element into stack
    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False

    def peek(self):
        return self.stack[-1]
    
    # pop element from stack
    def pop(self):
        self.stack.pop()
        

a = Stack()
a.push('Mon')
a.push('Tue')
a.push('Wed')

a.pop()

print(a.stack)

