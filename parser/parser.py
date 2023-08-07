class Parser:
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens
        self.idx = 0
        self.token = self.tokens[self.idx]

    def next(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.token = self.tokens[self.idx]

    def factor(self) -> str:
        if self.token.type == "INT" or self.token.type == "FLT":
            return self.token

        elif self.token.value == "(":
            self.next()
            expression = self.expression()
            return expression

    def term(self) -> str | list:
        left_node = self.factor()
        self.next()

        while self.token.value == "*" or self.token.value == "/":
            operation = self.token
            self.next()

            right_node = self.factor()
            self.next()
            left_node = [left_node, operation, right_node]

        return left_node

    def expression(self) -> str | list:
        left_node = self.term()

        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.next()

            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def parse(self) -> str | list:
        return self.expression()
