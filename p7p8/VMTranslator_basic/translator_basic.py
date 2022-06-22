#!/usr/bin/env python3

"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This is the main program that drives the translation process, using the
services of Parser and CodeWriter module.
"""

import os
import sys
import typing
from parser import Parser
from codewriter_basic import CodeWriter

def VMTranslator(input_file: typing.TextIO, output_file: typing.TextIO) -> None:
    """
    The VMTranslator enters a loop that uses the Parser services for iterating
    through the input file and parsing each line as a VM command, barring 
    white space. For each parsed command, the VMTranslator uses the CodeWriter
    for generating Hack assembly code and emitting the generated code into 
    the output file.
    """
    
    code_writer.setFileName(
                    os.path.splitext(os.path.basename(input_file.name))[0])
    while parser.hasMoreLines():
        parser.advance()
        if parser.commandType() == parser.C_ARITHMETIC:
            code_writer.writeArithmetic(parser.arg1())
            continue
        elif parser.commandType() in {parser.C_POP, parser.C_PUSH}:
            code_writer.writePushPop(parser.commandType(), parser.arg1(), parser.arg2())
            continue
        elif parser.commandType() == parser.C_LABEL:
            code_writer.writeLabel(code_writer.functionName + "." + parser.arg1())
            continue
        elif parser.commandType() == parser.C_GOTO:
            code_writer.writeGoto(code_writer.functionName + "." + parser.arg1())
            continue
        elif parser.commandType() == parser.C_IF:
            code_writer.writeIf(code_writer.functionName + "." + parser.arg1())
            continue
        elif parser.commandType() == parser.C_RETURN:
            code_writer.writeReturn()
            continue
        if parser.commandType() == parser.C_CALL:
            if parser.arg1() in code_writer.function_calls_num:
                code_writer.function_calls_num[parser.arg1()] += 1
            else:
                code_writer.function_calls_num[parser.arg1()] = 0
            code_writer.writeCall(parser.arg1(), parser.arg2())
        elif parser.commandType() == parser.C_FUNCTION:
            code_writer.writeFunction(parser.arg1(), parser.arg2())

if __name__ == '__main__':
    """ 
    The VMTranslator accepts a single command-line argument "source". 
    - If source is a file name of the form ProgName.vm. The file name may
      contain a file path. If no path is specified, the VM translator operates 
      on the current folder. The first character in the file name must be an
      uppercase letter, and the vm extension is mandatory. The translator 
      creates an output file, named ProgName.asm, containing the assembly
      instructions that realize the VM commands. The output file ProgName.asm
      is stored in the same folder as that of the input. If the file 
      ProgName.asm already exists, it will be overwritten
    - If source is a folder, named, say, Prog, the VMTranslator constructs a
      Parser for handling each .vm file in the folder, and a single CodeWriter
      for generating Hack assembly code into the single output file Prog.asm.
      Each time the VMTranslator starts translating a new .vm file in the
      folder, it must inform the CodeWriter that a new file is now being  
      processed using setFileName() method.
    """
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: ./translator.py <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_translate = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
        output_path = os.path.join(argument_path, os.path.basename(
            argument_path))
    else:
        files_to_translate = [argument_path]
        output_path, extension = os.path.splitext(argument_path)
    output_path += ".asm"

    with open(output_path, 'w') as output_file:
        code_writer = CodeWriter(output_file)
        for input_path in files_to_translate:
            filename, extension = os.path.splitext(input_path)
            if extension.lower() != ".vm":
                continue
            with open(input_path, 'r') as input_file:
                parser = Parser(input_file)
                VMTranslator(input_file, output_file)
        code_writer.close()
        # Here is no need to call file.close() when using "with" statement. 
        # The "with" statement itself ensures proper acquisition and release
        # of resources.
