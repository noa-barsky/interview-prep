
class Node:
    def __init__(self,data, nxt=None):
        self.data = data
        self.nxt = nxt


class linkedList:
    def __init__(self,head=None):
        self.head = head
    def insert_head(self, val):
        newNode = Node(val,self.head)
        self.head = newNode
    def insert_tail(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.nxt:
                curr = curr.nxt
            curr.nxt = new_node

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt


new_node = linkedList()
new_node.insert_tail(4)
new_node.insert_tail(6)
new_node.insert_tail(8)
new_node.insert_tail(9)
new_node.insert_tail(10)
new_node.printList()

