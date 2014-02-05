import unittest

from infix_eval.binary_node import BinaryNode

class TestBinaryNode(unittest.TestCase):
    def test_postfix_traverse(self):
        tree = BinaryNode(10)
        tree.right = BinaryNode(15)
        tree.left = BinaryNode(5)
        tree.left.left = BinaryNode(3)
        tree.left.right = BinaryNode(7)

        self.assertEqual(tree.postfix_traverse(), "3 7 5 15 10 ")

if __name__ == '__main__':
    unittest.main()
