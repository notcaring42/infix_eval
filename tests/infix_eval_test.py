import unittest

from infix_eval.evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator()
    def testNumericalResult(self):
        self.assertEqual(self.evaluator.evaluate("2 + 5"), 7)
        self.assertEqual(self.evaluator.evaluate("3 + 5 * 2"), 13)
        self.assertEqual(self.evaluator.evaluate("8 * 7 / 2"), 28)
        self.assertEqual(self.evaluator.evaluate("8 + 6 * 2 / 3 - 1"), 11)
        self.assertEqual(self.evaluator.evaluate(" 2+  3"), 5)
        self.assertEqual(self.evaluator.evaluate("1/2"), 0.5)
    def testTreeResult(self):
        self.fail("Not implemented yet")

if __name__ == "__main__":
    unittest.main()
