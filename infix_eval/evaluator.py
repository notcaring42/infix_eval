import re
import collections

from infix_eval.binary_node import BinaryNode


class Evaluator(object):
    def __init__(self):
        self.Result = collections.namedtuple('Result', ['result', 'tree'])
        self.operators = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

    def is_num(self, num):
        try:
            float(num)
        except ValueError:
            return False

        return True

    def _separate_ops(self, string):
        for op in self.operators.keys():
            if op in string:
                string = string.replace(op, ' %s ' % op)

        return string

    def _calc(self, op, operand1, operand2):
        if op == "+":
            return operand1 + operand2
        elif op == "-":
            return operand1 - operand2
        elif op == "/":
            return operand1 / operand2
        elif op == "*":
            return operand1 * operand2
        elif op == "^":
            return operand1 ** operand2
        else:
            raise ArgumentError("Operator invalid")

    def _pop_operands(self, op, node_stack, operator_stack, operand_stack):
        operand_node2 = node_stack.pop()
        operand_node1 = node_stack.pop()

        node = BinaryNode(op)
        node.left = operand_node1
        node.right = operand_node2
        node_stack.append(node)

        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operand_stack.append(self._calc(op, operand1, operand2))

    def evaluate(self, infix):
        infix = infix.strip()
        infix = self._separate_ops(infix)
        tokens = re.split(r' +', infix)

        operator_stack = []
        node_stack = []
        operand_stack = []

        for token in tokens:
            if token in self.operators.keys():
                if len(operator_stack) == 0:
                    operator_stack.append(token)
                else:
                    top_op = operator_stack[-1]
                    while (self.operators[top_op] >= self.operators[token]):
                        self._pop_operands(operator_stack.pop(), node_stack,
                                           operator_stack, operand_stack)

                        if len(operator_stack) == 0:
                            break
                        else:
                            top_op = operator_stack[-1]
                    operator_stack.append(token)
            elif self.is_num(token):
                node_stack.append(BinaryNode(float(token)))
                operand_stack.append(float(token))
            else:
                raise ValueError("Invalid token: " + str(token))

        for op in reversed(operator_stack):
            self._pop_operands(op, node_stack, operator_stack, operand_stack)

        return self.Result(tree=node_stack[0], result=operand_stack[0])
