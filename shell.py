from lexer import Lexer
from parser import Parser

print("ghoulscript")
while True:
    text: str = input("> ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens=tokens)
    tree = parser.parse()

    print(tree)
