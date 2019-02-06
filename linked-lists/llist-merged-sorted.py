
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
    def insert_tail(self,val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.nxt:
                curr = curr.nxt
            curr.nxt = new_node
    def find_middle(self):
        fst_ptr = self.head
        slow_ptr = self.head
        while fst_ptr and fst_ptr.nxt:
            fst_ptr = fst_ptr.nxt.nxt
            slow_ptr = slow_ptr.nxt
        return slow_ptr


def merge_sort(l1, l2):
    l1 = llist1
    l2 = llist2
    combined = linkedList()

    while llist1.head and llist2.head:
        if llist1.head.data < llist2.head.data:
            combined.insert_tail(llist1.head.data)
            llist1.head = llist1.head.nxt
        else:
            combined.insert_tail(llist2.head.data)
            llist2.head = llist2.head.nxt
    if not llist1.head:
        while llist2.head:
            combined.insert_tail(llist2.head.data)
            llist2.head = llist2.head.nxt
        return combined
    if not llist2.head:
        while llist1.head:
            combined.insert_tail(llist1.head.data)
            llist1.head = llist1.head.nxt
        return combined
        
    return combined

llist1 = linkedList(3)
llist1.insert_tail(4)
llist1.insert_tail(5)
llist1.insert_tail(8)
llist2 = linkedList(1)
llist2.insert_tail(7)
llist2.insert_tail(12)
llist2.insert_tail(13)
m = merge_sort(llist1, llist2)
print ("------------")
m.printList()


