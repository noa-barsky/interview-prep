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
                    self.left.insert(data)
            elif data > self.key:
                if self.rightChild is None:
                    self.rightChild = BinaryTree(data)
                else:
                    self.right.insert(data)
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
    def findval(self, val):
        if self.key:
            if val == self.key:
                return True
            elif val < self.key and self.leftChild:
                self.leftChild.findval(val)
            elif val > self.key and self.rightChild:
                self.rightChild.findval(val)
        return False

r = BinaryTree(10)
r.insert(9)
r.insert(11)
print(r.findval(12))