import re

class Evaluator(object):
    def __init__(self):
        self.operators = {'+': 0, '-': 0, '*': 1, '/': 1}

    def is_num(self, num):
        try:
            float(num)
        except ValueError:
            return False

        return True

    def compare_operators(self, op1, op2, operator_stack):
        if self.operators[op1] < self.operators[op2]:
            operator_stack.append(op2)
            return ""
        else:
            return operator_stack.pop() + " "

    def evaluate(self, infix):
        infix = infix.strip()
        tokens = re.split(r' +', infix)

        operator_stack = []
        postfix = ""

        for token in tokens:
            if token in self.operators.keys():
                if len(operator_stack) == 0:
                    operator_stack.append(token)
                else:
                    op1 = operator_stack[-1]
                    postfix += self.compare_operators(op1, token, operator_stack)
            elif self.is_num(token):
                postfix += (token + " ")
            else:
                raise ValueError("Invalid token: " + str(token))

        for op in operator_stack:
            postfix += (op + " ")

        return postfix.rstrip()
