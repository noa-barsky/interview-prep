
class Node():
    def __init__(self,data, nxt=None):
        self.data = data
        self.nxt = nxt


class linkedList():
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
    def delete_node(self, index):
        count = 0
        curr = self.head
        if index == 0:
            self.head = curr.nxt
        else:
            while curr:
                if count == (index - 1):
                    break
                else:
                    count += 1
                    curr = curr.nxt
            temp = curr.nxt
            curr.nxt = temp.nxt
    def remove_dup(self):
        curr = self.head
        while curr and curr.nxt:
            if curr.data == curr.nxt.data:
                curr.nxt = curr.nxt.nxt
            else:
                curr = curr.nxt
    def merge_sorted(self, lst):
        merged = linkedList()
        l1 = self.head
        l2 = lst.head
        while l1 and l2:
            # merged.insert_tail(l1.data)
            # merged.insert_tail(l2.data)
            # l1 = l1.nxt
            # l2 = l2.nxt
            if l1.data <= l2.data:
                

        merged.printList()






new_node = linkedList()
new_node.insert_tail(4)
new_node.insert_tail(6)
new_node.insert_tail(8)
new_node.insert_tail(8)
new_node.insert_tail(8)
new_node.insert_tail(9)
new_node.insert_tail(10)
new_node.insert_tail(10)
new_node.insert_tail(10)
new_node.insert_tail(10)
new_node.insert_tail(45)
new_node.insert_tail(54)


new_node1 = linkedList()
new_node1.insert_tail(4)
new_node1.insert_tail(6)
new_node1.insert_tail(8)
new_node1.insert_tail(9)

new_node.merge_sorted(new_node1)
# new_node.printList()
# print("-------------")
# new_node.remove_dup()
# new_node.printList()
# print("-------------")

