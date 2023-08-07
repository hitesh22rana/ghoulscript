from lexer import Lexer

print("ghoulscript")
while True:
    text: str = input("> ")
    tokenizer = Lexer(text=text)
    tokens = tokenizer.tokenize()

    print(tokens)
