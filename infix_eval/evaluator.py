import re

from infix_eval.binary_node import BinaryNode

class Evaluator(object):
    def __init__(self):
        self.operators = {'+': 0, '-': 0, '*': 1, '/': 1}

    def is_num(self, num):
        try:
            float(num)
        except ValueError:
            return False

        return True

    def _pop_operands(self, op, node_stack, operator_stack):
        operand1 = node_stack.pop()
        operand2 = node_stack.pop()

        node = BinaryNode(op)
        node.left = operand2
        node.right = operand1
        node_stack.append(node)

    def evaluate(self, infix):
        infix = infix.strip()
        tokens = re.split(r' +', infix)

        operator_stack = []
        node_stack = []

        for token in tokens:
            if token in self.operators.keys():
                if len(operator_stack) == 0:
                    operator_stack.append(token)
                else:
                    top_op = operator_stack[-1]
                    while (self.operators[top_op] >= self.operators[token]):
                        self._pop_operands(operator_stack.pop(), node_stack, 
                                           operator_stack)

                        if len(operator_stack) == 0:
                            break
                        else:
                            top_op = operator_stack[-1]
                    operator_stack.append(token)
            elif self.is_num(token):
                node_stack.append(BinaryNode(float(token)))
            else:
                raise ValueError("Invalid token: " + str(token))

        for op in operator_stack:
           self._pop_operands(op, node_stack, operator_stack)            

        return node_stack[0]
