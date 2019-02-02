
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
# print(new_node.head.data)
# new_node.insertHead(5)
# new_node.insertHead(6)
# new_node.insertHead(7)
# new_node.get_head()
new_node.printList()

