import re
import collections

from infix_eval.binary_node import BinaryNode

# Class for evaluating an infix expression
class Evaluator(object):
    def __init__(self):
        # Class for returning the results
        self.Result = collections.namedtuple('Result', ['result', 'tree'])

        # Maps operators to a precedence
        self.operators = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}

    # Tests if num is a valid number
    def is_num(self, num):
        try:
            float(num)
        except ValueError:
            return False

        return True

    # Separates the operators and operands in the string
    def _separate_ops(self, string):
        for op in self.operators.keys():
            if op in string:
                string = string.replace(op, ' %s ' % op)

        return string

    # Returns the arithmetic result of 'operand1 op operand2'
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

    # Pops operands from the operand stack and an operator
    # from the operator stack
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

    # Evaluates the infix expression
    def evaluate(self, infix):
        # Remove whitespace and turn the infix expression
        # into a list of operators and operands
        infix = infix.strip()
        infix = self._separate_ops(infix)
        tokens = re.split(r' +', infix)

        operator_stack = []
        node_stack = []
        operand_stack = []
        
        # Parse the expression
        for token in tokens:
            # If the token is an operator..
            if token in self.operators.keys():
                if len(operator_stack) == 0:
                    operator_stack.append(token)
                else:
                    # Compare this op's precedence to one at the
                    # top of the operator stack
                    # While the operator on top has higher precedence,
                    # pop from the operator stack and 2 operators
                    top_op = operator_stack[-1]
                    while (self.operators[top_op] >= self.operators[token]):
                        self._pop_operands(operator_stack.pop(), node_stack,
                                           operator_stack, operand_stack)

                        if len(operator_stack) == 0:
                            break
                        else:
                            top_op = operator_stack[-1]
                    
                    # Add the new operator
                    operator_stack.append(token)
            # If the token is a number, add a BinaryNode and
            # the number to node and operand stacks
            elif self.is_num(token):
                node_stack.append(BinaryNode(float(token)))
                operand_stack.append(float(token))
            # Throw an exception, the token is invalid
            else:
                raise ValueError("Invalid token: " + str(token))

        # Pop the remaining operators
        for op in reversed(operator_stack):
            self._pop_operands(op, node_stack, operator_stack, operand_stack)

        return self.Result(tree=node_stack[0], result=operand_stack[0])
