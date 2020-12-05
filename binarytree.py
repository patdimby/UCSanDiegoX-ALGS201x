class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

class BinaryTree(object):

    def __init__(self):        
        self.root = None

    def getRoot(self):
        return self.root    

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        if data < node.getData():
            if node.left is None:
                node.left = Node(data)               
            else:
                self._add(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)                
            else:
                self._add(data, node.right)


def recursiveGetMaxDepth(root):    
    if not root:
        return 0 
    return 1 + max([recursiveGetMaxDepth(root.getLeft()), recursiveGetMaxDepth(root.getRight())])
