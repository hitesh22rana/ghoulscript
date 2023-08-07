from tokens.float import Float
from tokens.integer import Integer


class Interpreter:
    def __init__(self, tree=None):
        self.tree = tree

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def compute_bin(self, left_node, operator, right_node):
        left_node_type = left_node.type
        right_node_type = right_node.type

        left_node_value = getattr(self, f"read_{left_node_type}")(left_node.value)
        right_node_value = getattr(self, f"read_{right_node_type}")(right_node.value)

        if operator.value == "+":
            output = left_node_value + right_node_value

        elif operator.value == "-":
            output = left_node_value - right_node_value

        elif operator.value == "*":
            output = left_node_value * right_node_value

        elif operator.value == "/":
            output = left_node_value / right_node_value

        return (
            Integer(output)
            if left_node_type == "INT" and right_node_type == "INT"
            else Float(output)
        )

    def interpret(self, tree=None):
        if tree is None:
            tree = self.tree

        left_node = tree[0]

        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]

        return self.compute_bin(left_node, operator, right_node)
