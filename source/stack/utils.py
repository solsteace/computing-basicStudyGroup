class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        return self.top.data
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
class Stack_2:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()