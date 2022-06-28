"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module features a set of simple routines for writing VM commands into the output file (infix to postfix conversion), see Figure 11.4.
"""

import typing


class VMWriter:
    """
    virtual memory segments, Fig 7.4
    """
    ARGUMENT = "argument"
    LOCAL = "local"
    STATIC = "static"
    CONSTANT = "constant"
    THIS = "this" # mapping object fields
    THAT = "that" # mapping array elements
    POINTER = "pointer" # mapping array elements 
    TEMP = "temp" # compiling do statements
    
    """
    arithmetic-logical commands, Fig 7.5 + Fig 10.5 + 11.5
    """
    ADD = "add"
    SUB = "sub"
    NEG = "neg"
    EQ = "eq"
    GT = "gt"
    LT = "lt"
    AND = "and"
    OR = "or"
    NOT = "not"
    
    def __init__(self, output_file: typing.TextIO) -> None:
        """
        prepare for writing
        """
        self.output = output_file
        
    
    def writePush(self, segment: str, index: int) -> None:
        """
        Write a VM push command
        """
        self.output.write("push " + segment + " " + str(index) + "\n")
        
    def writePop(self, segment: str, index: int) -> None:
        """
        Write a VM pop command
        """
        self.output.write("pop " + segment + " " + str(index) + "\n")
        
    def writeArithmetic(self, command: str) -> None:
        """
        Write a VM arithmetic-logical command
        """
        self.output.write(command + "\n")
        
    def writeLabel(self, label: str) -> None:
        """
        Write VM label command
        """
        self.output.write("label " + label + "\n")
        
    def writeGoto(self, label: str) -> None:
        """
        Write VM goto command
        """
        self.output.write("goto " + label + "\n")
    
    def writeIf(self, label: str) -> None:
        """
        Write VM if-goto command
        """
        self.output.write("if-goto " + label + "\n")
        
    def writeCall(self, name: str, nArgs: int) -> None:
        """
        Write VM call command
        """
        self.output.write("call " + name + " " + str(nArgs) + "\n")
        
    def writeFunction(self, name: str, nVars: int) -> None:
        """
        Write VM function command
        """
        self.output.write("function " + name + " " + str(nVars) + "\n")
         
    def writeReturn(self) -> None:
        """
        Write VM return command
        """
        self.output.write("return\n")
        
    def close(self) -> None:
        """
        Close the output_file
        """
        self.output.close()
        
