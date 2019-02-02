
class Node:
    def __init__(self,data, nxt=None):
        self.data = data
        self.nxt = nxt


class linkedList:
    def __init__(self,head=None):
        self.head = Node(head)
    def insertHead(self, val):
        newNode = Node(val,self.head)
        self.head = newNode
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt
    def get_head(self):
        print(self.head.data)

new_node = linkedList(3)
new_node.printList()

