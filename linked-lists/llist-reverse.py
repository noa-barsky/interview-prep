
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
    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            n = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = n
        self.head = prev

new_node = linkedList()
new_node.insertHead(4)
new_node.insertHead(6)
new_node.insertHead(8)
new_node.insertHead(9)
new_node.reverse()
new_node.printList()

