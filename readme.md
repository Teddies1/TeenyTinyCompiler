# Compiler App
#### Video Demo:  https://youtu.be/91aEuqMsSIw

## Introduction
I am Hon Joo, a incoming senior majoring in Computer Science. I wanted to learn more about compilers because it was interesting to me. Learning about compilers can also help boost my fundamental knowledge with regards to data structures, algorithms and how langugages work. I will be enrolling in a upper level
compilers elective class this upcoming semester. I hope to learn more about compilers and have fun in the
process!

I stumbled upon the TeenyTinyCompiler [tutorial](https://austinhenley.com/blog/challengingprojects.html) by Austin Henley, which was a gateway to learning about compilers. With the compiler I made from the tutorial's help, I decided to wrap that compiler into a simple web application for the CS50 final project.

This application is not complete, of course. After the completion of CS50, the application will be maintained and continually iterated on. The compiler is a simple one, and advanced features like handling methods and data structures are in the works. The webpage can stand to look prettier too.

## Description

This application is a simple web application for users to compile Tiny BASIC code into GCC compilable,
runnable C code. The interface is a simple static webpage for users to upload Tiny BASIC code files,
with extension `.tiny`. After uploading the code file, the compiler compiles the file, and returns
to the user a `.c` file. This file can then be compiled in the command line using GCC, and then run.

The webpage also features a quick start guide, with simple Tiny BASIC programs to help users to get started.
This is because some users may not be familiar with Tiny BASIC syntax. The featured programs allow users
to compute the average of N numbers, as well as print out the first N Fibonacci numbers.

## Project Directory
### /code
This directory contains the files for the compiler. The compiler is written in Python, using the TeenyTinyCompiler
tutorial. The compiler consists of a lexer, parser and emitter.
#### emit.py
The emitter's job is to format the parsed tokens into compilable, runnable C code. This is done by calling the emitter to print the appropriate token onto the output code. If a new line is needed, the emitter handles it too. Non-token code, like import statements can also be emitted.
#### lexer.py
The lexer takes input code and breaks it down into tokens. It does this by iterating through the input code, and converting each input block into a token. For example, an operator like a `+` sign is a token, a variable is also a token. It can also skip comments, and detect the end of file (EOF) character `\0`.
#### parse.py
The parser parses these tokens into the output programming language. It iterates through all the tokens, and prints the correct output code with the help of the emitter.
#### teenytiny.py
This file contains the main function for the compiler. It imports and initialises the lexer, parser and emitter for use in the compiling process.

### /files
This directory is for users to store any input `.tiny` or output `.c` files. This is a simple storage solution to keep all our input/output files. However, the application currently does not support automatic retrieval of input files and placing of output files. This could be a potential extension of the application.

### /templates
#### index.html
This directory contains any template HTML files for our web interface. Currently it only contains `index.html` as it is a simple webpage. The index page contains a `<script>` tag to handle the compiling logic. After the user uploads and submits the file, an EventHandler is called. The `/compile_and_return` route is called, where the input file is compiled and returned to the user as a file download.

### /static
#### styles.css
This directory contains our `.css` styling files. Currently, the project only uses vanilla CSS with no frameworks. Most of the styling is done with Flexbox. A future extension is to make use of frameworks like Tailwind or Bootstrap to beautify the page.

### app.py
This file contains our Flask app. The application contains a route `/compile_and_return` which takes the input file and passes it into the lexer. The tokens are then passed into the parser, and the emitter is called to return the output `.c` file.

