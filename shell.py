from parser import Parser

from interpreter import Interpreter
from lexer import Lexer

print("ghoulscript")
while True:
    text: str = input("> ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    print(tokens)

    # parser = Parser(tokens=tokens)
    # tree = parser.parse()

    # output = Interpreter().interpret(tree=tree)

    # print(output)
