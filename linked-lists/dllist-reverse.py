class DNode:
    def __init__(self,data):
        self.nxt = None
        self.prev = None
        self.data = data

class DoublyLinked:
    def __init__(self):
        self.head = None    
    def add_to_head(self, new_data):
        new_node = DNode(new_data)
        new_node.nxt = self.head
        if self.head != None:
            self.head.prev = new_node
        self.head = new_node
    def reverse(self):
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.nxt
            curr.nxt = temp
            curr = curr.prev
        if temp != None:
            self.head = temp.prev
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt

a = DoublyLinked()
a.add_to_head(4)
a.add_to_head(5)
a.add_to_head(6)
a.print_list()
print("-------")
a.reverse()
a.print_list()
