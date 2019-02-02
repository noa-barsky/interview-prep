class DNode():
    def __init__(self,data):
        self.nxt = None
        self.prev = None
        self.data = data

class DoublyLinked():
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
            temp = self.head
            self.head = new_node
            self.head.nxt = temp

        else:
            curr_ind = 0
            while curr:
                if count == index - 1:
                    break
                else:
                    count += 1
                    curr = curr.nxt
            temp = curr.nxt 
            new_node.nxt = temp
            temp.prev = new_node
            new_node.prev = curr
            curr.nxt = new_node
    def delete_node(self,index):
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




                



            
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt

a = DoublyLinked()
a.add_to_head(4)
a.add_to_tail(5)
a.add_to_tail(6)
a.delete_node(0)
# a.add_to_index(50, 0)
a.print_list()
