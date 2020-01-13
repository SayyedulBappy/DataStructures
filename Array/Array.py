import array

class Array:
    def __init__(self):
        self.items = array.array('i',[])

    def append(self,item):
        return self.items.append(item)
    
    def insert(self,index,item):
        return self.items.insert(index,item)
    
    def pop(self):
        return self.items.pop()
    
    def remove(self,item):
        return self.items.remove(item)
    
    def index(self,item):
        return self.items.index(item)
    
    def reverse(self):
        return self.items.reverse()
