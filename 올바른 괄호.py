class Stack:
    def __init__(self):
        self.data = []
    
    def push(self,item):
        self.data.append(item)
        
    def pop(self):
        if self.data:
            return self.data.pop(-1)
        else:
            return None
    
    def size(self):
        return len(self.data)
        
    def isEmpty(self):
        return self.size() == 0

def solution(s):
    stack = Stack()
    for i in s:
        if i == '(':
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            stack.pop()
    if not stack.isEmpty():
        return False

    return True
