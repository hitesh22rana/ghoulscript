from tokens.float import Float
from tokens.integer import Integer


class Interpreter:
    def __init__(self, tree, data):
        self.tree = tree
        self.data = data

    def read_INT(self, value):
        return int(value)

    def read_FLT(self, value):
        return float(value)

    def read_VAR(self, id):
        variable = self.data.read(id)
        variable_type = variable.type

        return getattr(self, f"read_{variable_type}")(variable.value)

    def compute_unary(self, operator, operand):
        operand_type = (
            "VAR" if str(operand.type).startswith("VAR") else str(operand.type)
        )

        operand = getattr(self, f"read_{operand_type}")(operand.value)

        if operator.value == "+":
            output = +operand

        elif operator.value == "-":
            output = -operand

        return Integer(output) if operand_type == "INT" else Float(output)

    def compute_bin(self, left_node, operator, right_node):
        left_node_type = (
            "VAR" if str(left_node.type).startswith("VAR") else str(left_node.type)
        )
        right_node_type = (
            "VAR" if str(right_node.type).startswith("VAR") else str(right_node.type)
        )

        # TODO: check if the variable who's value is being assigned is declared or not
        if operator.value == "=":
            left_node.type = f"VAR({right_node_type})"
            self.data.write(left_node, right_node)
            return self.data.read_all()

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

        # Unary operation
        if isinstance(tree, list) and len(tree) == 2:
            return self.compute_unary(tree[0], tree[1])

        elif not isinstance(tree, list):
            return tree

        # Binary operation
        left_node = tree[0]
        if isinstance(left_node, list):
            left_node = self.interpret(left_node)

        right_node = tree[2]
        if isinstance(right_node, list):
            right_node = self.interpret(right_node)

        operator = tree[1]

        return self.compute_bin(left_node, operator, right_node)
