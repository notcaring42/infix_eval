class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def postfix_traverse(self):
        result = ''
        if self.left is not None:
            result += self.left.postfix_traverse()
        if self.right is not None:
            result += self.right.postfix_traverse()
        result += str(self.data)
        return result + ' '
