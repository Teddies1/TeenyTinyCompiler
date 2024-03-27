from lexer import *

def main():
    source =  "420teddyIF\"teddy\"+>=<"
    lexer = Lexer(source)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()