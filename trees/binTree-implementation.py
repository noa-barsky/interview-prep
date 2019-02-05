class BinaryTree:
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


def inorder(root):
    if root:
        inorder(root.leftChild)
        print(root.key)
        inorder(root.rightChild)

r = BinaryTree(10)
r.insert(9)
r.insert(11)
inorder(r)
# print(inorder(r))
