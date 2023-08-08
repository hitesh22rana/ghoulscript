from tokens import Token


class Comparison(Token):
    def __init__(self, value):
        super().__init__("CMP", value)
