class Stack:
      def __init__(self):
            self.items = []
      def push(self,item):
            self.items.append(item)
      def pop(self):
            return self.items.pop()
      def peek (self):
            print(self.items[-1])
      def isEmpty(self):
            return len(self.items) == 0
      def size(self):
            return len(self.items)

new_stack = Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.pop()
new_stack.peek()
