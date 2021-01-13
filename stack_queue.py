#Writting wrapper classes fir Queue and Stack using python list

from collections import deque


class Queue():
    def __init__(self):
        self.queue = deque()
        pass

    def push(self, item):
        self.queue.append(item)
        pass

    def pushleft(self, item):
        self.queue.appendleft(item)
        pass

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return None
        pass       

    def popleft(self):
        if len(self.queue) > 0:
            return self.popleft()
        pass
        
    def __str__(self):
        return str(self.queue) 
        pass

class Stack():
    def __init__(self):
        self.stack = list()
        pass

    def push(self, item):
        self.stack.append(item)
        pass

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        pass   
    def peep(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
        pass
            
        
    def __str__(self):
        return str(self.stack) 
        pass


"""my_queue = Queue()
print(my_queue)
my_queue.push(6)
my_queue.pushleft(29)
print(my_queue)
my_queue.push(7)
my_queue.push(9)
print(my_queue)"""


"""my_stack = Stack()
my_stack.push(1)
my_stack.push(5)
my_stack.push(8)
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.peep())
print(my_stack.pop())
print(my_stack.pop())"""
