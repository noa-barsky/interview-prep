class DNode:
    def __init__(self,data, nxt=None, prev=None):
        self.nxt = nxt
        self.prev = prev
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
    def add_to_tail(self, new_data):
        new_node = DNode(new_data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.nxt:
                curr = curr.nxt
            curr.nxt = new_node
            new_node.prev = curr
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt

a = DoublyLinked()
a.add_to_head(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.print_list()
