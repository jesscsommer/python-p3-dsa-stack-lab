class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for i in items[:100]:
            self.items.append(i)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if len(self.items) > 0: 
            return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return (len(self.items))

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        return False 

    def search(self, target):
        if target in self.items: 
            ti = self.items.index(target)
            return (len(self.items) - 1) - ti
        return -1
