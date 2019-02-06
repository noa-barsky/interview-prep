class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
# Compare the new value with the parent node
        if self.key:
            if data < self.key:
                if self.leftChild is None:
                    self.leftChild = BinaryTree(data)
                else:
                    self.leftChild.insert(data)
            elif data > self.key:
                if self.rightChild is None:
                    self.rightChild = BinaryTree(data)
                else:
                    self.rightChild.insert(data)
        else:
            self.key = data
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def BFS(root):
    """In BFS the Node Values at each level of the Tree are traversed before going to next level"""
    to_visit = []
    if root:
        to_visit.append(root)
    while to_visit:
        current = to_visit.pop(0)
        print(current.key)
        if current.leftChild:
            to_visit.append(current.leftChild)
        if current.rightChild:
            to_visit.append(current.rightChild)


r = BinaryTree(10)
r.insert(8)
r.insert(9)
r.insert(12)
r.insert(11)

BFS(r)