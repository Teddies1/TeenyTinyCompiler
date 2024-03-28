from lexer import *
from emit import *
from parse import *
import sys
from flask import Flask, request, send_file
import os

app = Flask(__name__)

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
    uploaded_file_path = 'files/' + file.filename
    
    print("Teeny Tiny Compiler")
    with open(uploaded_file_path) as inputFile:
        source = inputFile.read()

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(source)
    emitter = Emitter("files/compiledoutput.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")
    
    # Return the compiled C file
    return send_file("../"+emitter.fullPath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
