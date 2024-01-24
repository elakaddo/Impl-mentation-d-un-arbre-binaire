import unittest, sys
from hamcrest import *
sys.path.append("samples/")
from binaryTree import Node


class BinaryTreeTest(unittest.TestCase) :
    def test_is_root(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.setRoot()
        node1.setLeft(node3)
        node1.setRight(node2)
        node3.setLeft(node4)

        assert_that(True, equal_to(node1.is_root()))
        assert_that(False, equal_to(node2.is_root()))
        assert_that(False, equal_to(node3.is_root()))
        assert_that(False, equal_to(node4.is_root()))
    
    def test_search(self) :
        root = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        root.setRoot()
        root.setLeft(node3)
        root.setRight(node2)
        node3.setLeft(node4)

        assert_that(True, equal_to(root.search(root, 1)))
        assert_that(False, equal_to(root.search(root, 5)))
        assert_that(False, equal_to(root.search(root, -1)))
        assert_that(False, equal_to(root.search(root, 0)))
    
    def test_is_binary(self) : 
        root = Node(1)
        assert_that(True, equal_to(root.is_binaryTree(root)))

        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)

        root.setRoot()
        root.setLeft(node3)
        root.setRight(node2)
        node3.setLeft(node4)
        print(root.is_binaryTree(root))
        
        assert_that(False, equal_to(root.is_binaryTree(root)))

        node3.setRight(node5)
        node5.setRight(node6)

        root.parcours(root)

        print(node5.setLeft(node7))

        assert_that(True, equal_to(root.is_binaryTree(root)))

def test_add(self) : 
    entiers = [5, 3, 7, 7, 2, 4, 6, 8]
    assert_that(True, equal_to(Node.createBTree(entiers)))




