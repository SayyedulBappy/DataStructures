from collections import deque ## for quicker operations

class Queue:
    def __init__(self):
        self.items = deque()
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, item):
        self.items.append(item)
 
    def dequeue(self):
        return self.items.popleft()

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[len(self.items)-1]
 