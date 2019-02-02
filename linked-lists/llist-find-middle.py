
class Node:
    def __init__(self,data, nxt=None):
        self.data = data
        self.nxt = nxt


class linkedList:
    def __init__(self,head=None):
        self.head = Node(head)
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
    def insert_index(self,val, index):
        new_node = Node(val)
        count = 0
        curr = self.head
        if index == 0:
            temp = self.head
            self.head = new_node
            self.head.nxt = temp
            temp.prev = new_node
        else:
            while curr:
                if (count == index - 1):
                    break
                else:
                    count += 1
                    curr = curr.nxt
            new_node.nxt = curr.nxt
            curr.nxt = new_node
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.nxt
    def find_middle(self):
        fst_ptr = self.head
        slow_ptr = self.head
        while fst_ptr and fst_ptr.nxt:
            fst_ptr = fst_ptr.nxt.nxt
            slow_ptr = slow_ptr.nxt
        print(slow_ptr.data)

new_node = linkedList()
new_node.insert_tail(4)
new_node.insert_tail(6)
new_node.insert_tail(8)
new_node.insert_tail(9)
new_node.insert_tail(10)
new_node.insert_tail(54)
new_node.insert_tail(45)
new_node.printList()
print("-------------")
new_node.find_middle()

