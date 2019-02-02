class DNode():
    def __init__(self,data, nxt=None, prev=None):
        self.nxt = nxt
        self.prev = prev
        self.data = data

class DoublyLinked():
    def __init__(self, head = None):
        self.head = DNode(head)    
    def add_to_head(self, new_data):
        new_node = DNode(new_data, self.head)
        self.head.prev = new_node
        self.head = new_node
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.nxt
        print("\n")

a = DoublyLinked(0)
# new_node = DNode(1)
# new_node.nxt = DNode(2)
# a.head = new_node
a.add_to_head(4)
a.add_to_head(5)
# a.add_to_head(6)
# print(a.nxt.data)
print(a.head.nxt.prev.data)
a.print_list()

