from tokens import Token


class Variable(Token):
    def __init__(self, value):
        super().__init__("VAR", value)
