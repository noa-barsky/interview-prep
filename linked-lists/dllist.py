class DNode:
    def __init__(self,data, nxt=None, prev=None):
        self.nxt = nxt
        self.prev = prev
        self.data = data

class DoublyLinked:
    def __init__(self, head = None):
        self.head = DNode(head)    
    def add_to_head(self, new_data):
        new_node = DNode(new_data, self.head)
        self.head.prev = new_node
        self.head = new_node
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt
a = DoublyLinked(0)
a.add_to_head(4)
a.add_to_head(5)
a.print_list()

