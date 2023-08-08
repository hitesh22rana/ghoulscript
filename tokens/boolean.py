from tokens import Token


class Boolean(Token):
    def __init__(self, value):
        super().__init__("BOOL", value)
