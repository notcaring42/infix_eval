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

    def evaluate(self, infix):
        infix = infix.strip()
        tokens = re.split(r' +', infix)

        operator_stack = []
        operand_stack = []

        for token in tokens:
            if token in self.operators.keys():
                if len(operator_stack) == 0:
                    operator_stack.append(token)
                else:
                    top_op = operator_stack[-1]
                    while (self.operators[top_op] >= self.operators[token]):
                        operand1 = operand_stack.pop()
                        operand2 = operand_stack.pop()

                        node = BinaryNode(operator_stack.pop())
                        node.left = operand2
                        node.right = operand1
                        operand_stack.append(node)

                        if len(operator_stack) == 0:
                            break
                        else:
                            top_op = operator_stack[-1]
                    operator_stack.append(token)
            elif self.is_num(token):
                operand_stack.append(BinaryNode(float(token)))
            else:
                raise ValueError("Invalid token: " + str(token))

        for op in operator_stack:
           operand1 = operand_stack.pop()
           operand2 = operand_stack.pop()

           node = BinaryNode(op)
           node.left = operand2
           node.right = operand1
           operand_stack.append(node)
            
        return operand_stack[0]
