class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    def get_as_list(self):
        return self.items
    
    
    
    
    
N=[12,13,34,56,68,19,21,89]
st=Stack()
for i in N:
    if i%2==0:
        st.push(i)
print(st.get_as_list())        
    