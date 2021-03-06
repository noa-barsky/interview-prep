class DNode:
    def __init__(self,data=None, nxt=None,prev=None):
        self.nxt = nxt
        self.prev = prev
        self.data = data

class DoublyLinked:
    def __init__(self, head=None):
        self.head = DNode(head)  
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
                n = curr
                curr = curr.nxt
                curr.prev = n
            curr.nxt = new_node
            new_node.prev = curr
    def add_to_index(self, val, index):
        new_node = DNode(val)
        curr = self.head
        count = 0
        if index == 0:
            self.add_to_head(val)
        else:
            curr_ind = 0
            while curr:
                if count == index - 1:
                    break
                else:
                    count += 1
                    curr = curr.nxt
            new_node.nxt = curr.nxt
            new_node.prev = curr
            curr.nxt = new_node
    def delete_node(self,index):
        if self.head.data:
            count = 0
            curr = self.head
            if index == 0:
                self.head = self.head.nxt
            else:
                while curr:
                    if count == (index - 1):
                        break
                    else:
                        count += 1
                        curr = curr.nxt
                curr.nxt = curr.nxt.nxt
                curr.nxt.prev = curr
    def print_list(self):
        if self.head:
            curr = self.head
            while curr:
                print(curr.data)
                curr = curr.nxt

a = DoublyLinked(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.delete_node(1)
print(a.head.nxt.prev.data)
a.print_list()
