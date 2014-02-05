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
    def testTreeResult(self):
        self.fail("Not implemented yet")

if __name__ == "__main__":
    unittest.main()
