from tokens import Token


class Declaration(Token):
    def __init__(self, value):
        super().__init__("DECL", value)
