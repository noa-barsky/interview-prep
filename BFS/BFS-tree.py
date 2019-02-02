class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def DFS(root):
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
r.insertLeft(8)
r.insertLeft(9)
r.insertRight(12)
r.insertRight(11)

BFS(r)