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
    def findval(self, val):
        if val < self.key:
            if self.leftChild is None:
                return True
            return self.leftChild.findval(val)
        elif val > self.key:
            if self.rightChild is None:
                return False
            return self.rightChild.findval(val)
        else:
            return True

r = BinaryTree(10)
r.insertLeft(9)
r.insertRight(11)
print(r.findval(10))