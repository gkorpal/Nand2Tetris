#!/usr/bin/env python3

"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module drives the compilation process. 
"""

import typing
import sys
import os
from engine import CompilationEngine


def JackCompiler() -> None:
    """
    It operates on either a file name of the form Xxx.jack or on a folder 
    name containing one or more such files. 
    For each source Xxx.jack file, the program:
    1. creates an output file named Xxx.vm; and
    2. uses a CompilationEngine for parsing the input file and emitting the
       translated VM code into the output file.
    """
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: ./compiler.py <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".jack":
            continue
        output_path = filename + ".vm"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
            CompilationEngine(input_file, output_file)
            
if __name__ == '__main__':
  JackCompiler()
