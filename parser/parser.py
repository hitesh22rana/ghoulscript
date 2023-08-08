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
            expression = self.boolean_expression()
            return expression

        elif self.token.value == "not":
            operator = self.token
            self.next()
            return [operator, self.boolean_expression()]

        elif self.token.type.startswith("VAR"):
            return self.token

        elif self.token.value == "+" or self.token.value == "-":
            operator = self.token
            self.next()
            opperand = self.boolean_expression()

            return [operator, opperand]

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

    def comparison_expression(self):
        left_node = self.expression()

        while self.token.type == "CMP":
            operator = self.token
            self.next()

            right_node = self.expression()
            left_node = [left_node, operator, right_node]

        return left_node

    def boolean_expression(self):
        left_node = self.comparison_expression()

        while self.token.type == "BOOL":
            operator = self.token
            self.next()

            right_node = self.comparison_expression()
            left_node = [left_node, operator, right_node]

        return left_node

    def expression(self) -> str | list:
        left_node = self.term()

        while self.token.value == "+" or self.token.value == "-":
            operation = self.token
            self.next()

            right_node = self.term()
            left_node = [left_node, operation, right_node]

        return left_node

    def variable(self) -> str:
        if self.token.type.startswith("VAR"):
            return self.token

    def statement(self):
        if self.token.type == "DECL":
            # Variable assignment
            self.next()
            left_node = self.variable()
            self.next()

            if self.token.value == "=":
                operation = self.token
                self.next()

                right_node = self.boolean_expression()

                return [left_node, operation, right_node]

        elif (
            self.token.type == "INT"
            or self.token.type == "FLT"
            or self.token.type == "OP"
            or self.token.value == "not"
        ):
            # Arithmetic expression
            return self.boolean_expression()

    def parse(self) -> str | list:
        return self.statement()
