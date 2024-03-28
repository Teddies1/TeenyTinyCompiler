from lexer import *
from emit import *
from parse import *
import sys
from flask import Flask, request, send_file
import os

app = Flask(__name__)

# def main():
#     print("Teeny Tiny Compiler")

#     if len(sys.argv) != 2:
#         sys.exit("Error: Compiler needs source file as argument.")
#     with open(sys.argv[1], 'r') as inputFile:
#         source = inputFile.read()

#     # Initialize the lexer, emitter, and parser.
#     lexer = Lexer(source)
#     emitter = Emitter("out.c")
#     parser = Parser(lexer, emitter)

#     parser.program() # Start the parser.
#     emitter.writeFile() # Write the output to file.
#     print("Compiling completed.")


@app.route('/')
def index():
    return send_file('index.html')

@app.route('/compile_and_return', methods=['POST'])
def compile_and_return():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    # Save the uploaded file
    uploaded_file_path = 'uploaded_file.teeny'
    file.save(uploaded_file_path)
    
    print("Teeny Tiny Compiler")
    with open(uploaded_file_path) as inputFile:
        source = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    emitter = Emitter("files/output.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
    
    # Return the compiled C file
    return send_file("../"+emitter.fullPath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
