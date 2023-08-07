from parser import Parser

from interpreter import Interpreter
from lexer import Lexer
from lib import Data

data = Data()

print("ghoulscript")
while True:
    text: str = input("> ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    parser = Parser(tokens=tokens)
    tree = parser.parse()

    interpreter = Interpreter(tree=tree, data=data)

    output = interpreter.interpret()

    print(output)
