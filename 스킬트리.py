class Queue:
    def __init__(self):
        self.data = []
        
    def enqueue(self, item):
        self.data.append(item)
        
    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]

def solution(skill, skill_trees):
    count = 0
    for elem in skill_trees:
        
        q = Queue()
        for x in skill:
            q.enqueue(x)
        for i in elem:
            if i not in skill:
                k = 1
                continue
            if i == q.peek():
                q.dequeue()
                k = 1
            else:
                k = 0
                break
                
        if k == 1:
            count += 1
    return count
