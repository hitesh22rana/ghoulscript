from tokens.boolean import Boolean
from tokens.comparison import Comparison
from tokens.declaration import Declaration
from tokens.float import Float
from tokens.integer import Integer
from tokens.operation import Operation
from tokens.variable import Variable


class Lexer:
    digits: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letters: list[str] = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    operations: list[str] = ["+", "-", "*", "/", "(", ")", "="]
    stop_words: list[str] = [" "]
    boolean_operators: list[str] = ["and", "or", "not"]
    declarations: list[str] = ["ghoul"]
    comparisons: list[str] = ["<", ">", "<=", ">=", "?="]
    special_characters: list[str] = [">", "<", "=", "?"]

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

            elif self.char in Lexer.letters:
                word: str = self.extract_word()

                if word in Lexer.declarations:
                    self.token = Declaration(word)

                elif word in Lexer.boolean_operators:
                    self.token = Boolean(word)

                else:
                    self.token = Variable(word)

            elif self.char in Lexer.special_characters:
                comparison_operator: str = ""
                while self.char in Lexer.special_characters and self.idx < len(
                    self.text
                ):
                    comparison_operator += self.char
                    self.next()

                self.token = Comparison(comparison_operator)

            self.tokens.append(self.token)

        return self.tokens

    def next(self) -> None:
        self.idx += 1
        if self.idx < len(self.text):
            self.char = self.text[self.idx]

    def extract_number(self):
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

    def extract_word(self):
        word: str = ""

        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.next()

        return word
