#!/usr/bin/env python3

"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference 
because I lack experience working with OOP and Python.
"""

import os
import sys
import typing 
"""
Type hints help combine function/method signature and header
https://docs.python.org/3/library/typing.html
"""
from parser import Parser
from code import Code
from symboltable import SymbolTable

    
class HackAssembler:
    def __init__(self, input_file: typing.TextIO, output_file: typing.TextIO) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.parser = Parser(input_file)
        self.symbol_table = SymbolTable()
        self.code = Code()
        
    def firstPass(self) -> None:
        """
        The first pass results in adding to the symbol table all the 
        program’s label symbols, along with their corresponding values.
        """
        counter = 0
        while self.parser.hasMoreLines():
            self.parser.advance()
            if self.parser.instructionType() == self.parser.L_INSTRUCTION:
                self.symbol_table.addEntry(self.parser.symbol(), counter)
            else:
                counter += 1
    
    def createAinstruction(self, value: int) -> str:
        """
        For each A_INSTRUCTION of type @xxx, create a string of sixteen
        '0' and '1' characters during second pass.
        """
        return "0" + format(value, '015b')

    def createCinstruction(self, dest: str, comp: str, jump: str) -> str:
        """
        For each C_INSTRUCTION, assemble (concatenate) the binary codes 
        into a string consisting of sixteen '0' and '1' characters 
        during second pass.
        """
        if "<" in comp or ">" in comp:
            return "101" + self.code.comp_dict[comp] + \
            self.code.dest_dict[dest] + self.code.jump_dict[jump]
        return "111" + self.code.comp_dict[comp] + \
        self.code.dest_dict[dest] + self.code.jump_dict[jump]
        
    def secondPass(self) -> None:
        """
        The assembler goes again through the entire program.
        Each time an A_INSTRUCTION with a symbolic reference is encountered, 
        namely, @xxx, where xxx is a symbol and not a number, the assembler    
        looks up xxx in the symbol table. If the symbol is found, the 
        assembler replaces it with its numeric value and completes the
        instruction’s translation. If the symbol is not found, then it must 
        add new entry <xxx, value> to SymbolTable.
        The RAM space designated for storing variables starts at 16 and is
        incremented by 1 after each time a new variable is found in the code.
        """
        self.parser.line_num = self.parser.DEFAULT_START_PROG_ADDR
        self.parser.curr_instruction = None
        while self.parser.hasMoreLines():
            self.parser.advance()
            if self.parser.instructionType() == self.parser.A_INSTRUCTION:
                if self.parser.symbol().isnumeric():
                     self.output_file.write(
                     self.createAinstruction(int(self.parser.symbol())))
                     self.output_file.write("\n")
                else:
                    if not self.symbol_table.contains(self.parser.symbol()):
                        self.symbol_table.addEntry(self.parser.symbol(),
                        self.symbol_table.next_empty_memory)
                        self.symbol_table.next_empty_memory += 1
                    self.output_file.write(
                             self.createAinstruction(
                             int(self.symbol_table.getAddress(
                             self.parser.symbol()))))
                    self.output_file.write("\n")
            elif self.parser.instructionType() == self.parser.C_INSTRUCTION:
                           self.output_file.write(
                           self.createCinstruction(self.parser.dest(),
                           self.parser.comp(), self.parser.jump()))
                           self.output_file.write("\n")
    

def main() -> None:
    """ 
    The Hack assembler accepts a single command-line argument "Prog.asm". 
    The file name may contain a file path. 
    If no path is specified then the assembler operates on the current folder.
    The assembler creates an output file named "Prog.hack" and writes the 
    translated binary instructions into it.
    The output file is created in the same folder as the input file.
    If there is a file by this name in the folder, it will be overwritten.
    """
    if not len(sys.argv) == 2:
        sys.exit("Invalid usage, please use: ./assembler.py <input path>")
    argument_path = os.path.abspath(sys.argv[1])
    if os.path.isdir(argument_path):
        files_to_assemble = [
            os.path.join(argument_path, filename)
            for filename in os.listdir(argument_path)]
    else:
        files_to_assemble = [argument_path]
    for input_path in files_to_assemble:
        filename, extension = os.path.splitext(input_path)
        if extension.lower() != ".asm":
            continue
        output_path = filename + ".hack"
        with open(input_path, 'r') as input_file, \
                open(output_path, 'w') as output_file:
                assembler = HackAssembler(input_file, output_file)
                assembler.firstPass()
                assembler.secondPass()

if __name__ == '__main__':
    """
    Code within this block won’t run unless the module is executed in the 
    top-level environment. Putting as few statements as possible in the 
    block below can improve code clarity and correctness. 
    https://docs.python.org/3/library/__main__.html#idiomatic-usage
    """
    main()
    

