from lexer.tokens import Token


class Operation(Token):
    def __init__(self, value: str) -> None:
        super().__init__("OP", value)
