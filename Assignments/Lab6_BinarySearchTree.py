class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insertNode(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._insertNode(val, self.root)

    def _insertNode(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._insertNode(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._insertNode(val, node.r)
            else:
                node.r = Node(val)

    def search(self, val):
        if(self.root != None):
            return self._search(val, self.root)
        else:
            return None

    def _search(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._search(val, node.l)
        elif(val > node.v and node.r != None):
            self._search(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
def main():
    tree = Tree()
# givenArray = map(int,raw_input("Enter the input elements with delimiter as space :").split());
    givenArray=[55,10,2,33,12,44]
    print ("Given Array ", givenArray)
    for i in givenArray :
        tree.insertNode(i)
    tree.printTree()
main()