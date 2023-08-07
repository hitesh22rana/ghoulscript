from lexer.token.integer import Integer
from lexer.token.float import Float
from lexer.token.operation import Operation


class Lexer:
    digits: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    operations: list[str] = ["+", "-", "*", "/"]
    stop_words: list[str] = [" "]

    def __init__(self, text: str) -> None:
        self.text: str = text
        self.idx: int = 0
        self.tokens: list[str] = []
        self.char = self.text[self.idx]
        self.token = None

    def tokenize(self) -> list[str]:
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token = self.extract_number()

            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.next()

            elif self.char in Lexer.stop_words:
                self.next()
                continue

            self.tokens.append(self.token)

        return self.tokens

    def next(self) -> None:
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

    def extract_number(self) -> Integer | Float:
        number: str = ""
        isFloat: bool = False

        while (self.char in Lexer.digits or self.char == ".") and self.idx < len(
            self.text
        ):
            if self.char == ".":
                isFloat = True

            number += self.char
            self.next()

        return Integer(number) if not isFloat else Float(number)
