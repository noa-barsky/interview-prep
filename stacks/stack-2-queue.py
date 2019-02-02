class QueuetoStack:
    def __init__(self):
        self.q1 = []
        self.q2 = [] #will act as empty temp Queue

    def push(self,x):
        self.q1.insert(0,x) #enqueue

    def pop(self):
        #move all items to q2
        q2 = self.q2
        q1 = self.q1
        i = 1
        l = len(q1)
        while i <= l:
            p = q1.pop()
            q2.append(p)
            i += 1
        return q2.pop()
    def size(self):
	    return len(self.q1)

    def print_stack(self):
	    return self.q1, self.q2


a = QueuetoStack()
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
