class Node :
    def __init__(self, value, left=None, right=None, isRoot=False, isLeaf=True) -> None:
        self.value = value
        self.left = left
        self.right = right
        self.isRoot = isRoot
        self.isLeaf = isLeaf

    def setLeft(self, node) :
        if not self.search(self, node.value) :
            self.left = node
            self.isLeaf = False
        else : return False
                         
    def setRight(self, node) :
        self.right = node
        self.isLeaf = False
    
    def setRoot(self) :
        self.isRoot =  True
    
    def setValue(self, value) :
        self.value = value
    
    def is_root(self) :
        return self.isRoot
    
    def is_leaf(self) :
        return self.isLeaf
    
    def is_binary_node(self) :
        return self.left != None and self.right != None
    
    def is_leaf_node(self) :
        return self.left == None and self.right == None
    
    def search(self, node, value) :
        existRight = False
        existLeft = False
        if node == None :
            return False
        if node.value == value :
            return True
        else : 
            existRight = self.search(node.right, value)
            existLeft = self.search(node.left, value)
        return existLeft or existRight
        
    def parcours(self, node):
        if node == None : 
            return
        
        self.parcours(node.right)
        print(node.value)
        self.parcours(node.left)

    def is_binaryTree(self, node) :
        leftBinary = False
        rightBinary = True
        if node == None : 
            return False
        if node.is_leaf() : return True
        if node.is_binary_node() :
            leftBinary = self.is_binaryTree(node.left)
            rightBinary = self.is_binaryTree(node.right)
        return leftBinary and rightBinary

    def display(self, node, level=0, prefix="Root:") :
        if node == None : 
            return
        print(" " * (level * 4) + prefix + str(node.value))
        self.display(node.left, level + 1, "L--- ")
        self.display(node.right, level + 1, "R--- ")

    def insert_element(self, root,value) :
        if root == None :
            return Node(value)
        if root.value > value :
            root.left = self.insert_element(root.left, value)
        if root.value < value : 
            root.right = self.insert_element(root.right, value)
        return root

    def create_BTree(self, entiers) :
        root = None
        for n in entiers : 
            root = self.insert_element(root, n)
        return root

        

if __name__ == "__main__" :
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root.setRoot()
    root.setLeft(node2)
    root.setRight(node3)
    node3.setLeft(node4)
    node3.setRight(node5)

    node4.setLeft(node6)
    node5.setLeft(node6)
    
    root.display(root)
    numbers = [5, 3, 7, 2, 4, 6, 8]
    btree = root.create_BTree(numbers)
    btree.display(btree)

    

    
    
