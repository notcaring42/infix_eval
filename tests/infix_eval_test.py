import unittest

from infix_eval.evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()
    def testNumericalResult(self):
        self.assertEqual(self.evaluator.evaluate("2 + 5").result, 7)
        self.assertEqual(self.evaluator.evaluate("3 + 5 * 2").result, 13)
        self.assertEqual(self.evaluator.evaluate("8 * 7 / 2").result, 28)
        self.assertEqual(self.evaluator.evaluate("8 + 6 * 2 / 3 - 1").result, 11)
        self.assertEqual(self.evaluator.evaluate(" 2 +  3").result, 5)
        self.assertEqual(self.evaluator.evaluate("1 / 2").result, 0.5)
        self.assertEqual(self.evaluator.evaluate("2 ^ 2 * 5").result, 20)
        self.assertEqual(self.evaluator.evaluate("7 * 2 ^ 3").result, 56)
        self.assertEqual(self.evaluator.evaluate("7*2^3").result, 56)
        self.assertEqual(self.evaluator.evaluate("8+6*2/3-1").result, 11)
    def testTreeResult(self):
        tree = self.evaluator.evaluate("8 + 6 * 2 / 3 - 1").tree

        self.assertEqual(tree.data, '-')
        self.assertEqual(tree.right.data, 1)
        self.assertEqual(tree.left.data, '+')
        self.assertEqual(tree.left.left.data, 8)
        self.assertEqual(tree.left.right.data, '/')
        self.assertEqual(tree.left.right.right.data, 3)
        self.assertEqual(tree.left.right.left.data, '*')
        self.assertEqual(tree.left.right.left.left.data, 6)
        self.assertEqual(tree.left.right.left.right.data, 2)

if __name__ == "__main__":
    unittest.main()
