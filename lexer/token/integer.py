from lexer.token import Token


class Integer(Token):
    def __init__(self, value):
        super().__init__("INT", value)
