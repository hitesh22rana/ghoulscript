from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

print("ghoulscript")
while True:
    text: str = input("> ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens=tokens)
    tree = parser.parse()

    output = Interpreter().interpret(tree=tree)

    print(output)
