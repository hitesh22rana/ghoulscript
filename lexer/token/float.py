from lexer.token import Token


class Float(Token):
    def __init__(self, value):
        super().__init__("FLT", value)
