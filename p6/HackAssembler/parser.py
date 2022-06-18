"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference 
because I lack experience working with OOP and Python.

This is Parser module for parsing the input into instructions and instructions 
and instructions into fields.
"""

import typing 
"""
Type hints help combine function/method signature and header
https://docs.python.org/3/library/typing.html
"""


class Parser:
    """
    constants defined here to avoid magic numbers
    source: https://codereview.stackexchange.com/a/163627/259829
    """
    DEFAULT_START_PROG_ADDR = 0
    COMMENT_PREFIX = "//"
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

    def __init__(self, input_file: typing.TextIO) -> None:
        """
        Gets ready to parse the opened input_file
        """
        self.input_lines = input_file.read().splitlines()
        self.line_num = self.DEFAULT_START_PROG_ADDR
        self.curr_instruction = None
        
    def hasMoreLines(self) -> bool:
        """
        Checks for more lines in the input_file
        """
        return self.line_num < len(self.input_lines)
    
    def advance(self) -> None:
        """
        Skips over white space and comments, if necessary.
        Reads the next instruction from the input_file and makes
        is the current instruction.
        This routine is called only if hasMoreLines is true.
        Initially there is no current instruction.
        """
        self.curr_instruction = \
        self.input_lines[self.line_num].split(self.COMMENT_PREFIX)[0]
        while (self.curr_instruction == "" or
            self.curr_instruction.strip().startswith(self.COMMENT_PREFIX)) \
                and self.hasMoreLines():
            self.line_num += 1
            self.curr_instruction = self.input_lines[self.line_num]
        self.line_num += 1
        
    def instructionType(self) -> int:
        """
        Returns the type of the current instruction:
        A_INSTRUCTION for @xxx, where xxx is either a decimal or a symbol
        C_INSTRUCTION for dest=comp;jump, where only comp is mandatory
        L_INSTRUCTION for (xxx), where xxx is a symbol.
        """
        starts_with = self.curr_instruction.strip()[0]
        if starts_with == "@":
            return self.A_INSTRUCTION
        elif starts_with == "(":
            return self.L_INSTRUCTION
        else:
            return self.C_INSTRUCTION
            
    def symbol(self) -> str:
        """
        Should be called only if instructionType is A_INSTRUCTION or
        L_INSTRUCTION.
        If A_INSTRUCTION @xxx then returns xxx (as string)
        If L_INSTRUCTION (xxx) then returns xxx (as string)
        """
        if self.instructionType() == self.A_INSTRUCTION:
            return self.curr_instruction.strip()[1:]
        elif self.instructionType() == self.L_INSTRUCTION:
            return self.curr_instruction.strip()[1:-1]
            
    def dest(self) -> str:
        """
        Should be called only if instructionType is C_INSTRUCTION
        Returns dest part (if exists)
        """
        if self.instructionType() == self.C_INSTRUCTION:
            equal_pos = self.curr_instruction.find("=")
            if equal_pos != -1:
                return self.curr_instruction[:equal_pos].strip()
            else:
                return ""
    
    def comp(self) -> str:
        """
        Should be called only if instructionType is C_INSTRUCTION
        Returns comp part (always exists)
        """
        if self.instructionType() == self.C_INSTRUCTION:
            equal_pos = self.curr_instruction.find("=")
            semicolon_pos = self.curr_instruction.find(";")
            if semicolon_pos == -1:
                semicolon_pos = len(self.curr_instruction)
            return self.curr_instruction[equal_pos + 1:semicolon_pos].strip()
    
    def jump(self) -> str:
        """
        Should be called only if instructionType is C_INSTRUCTION
        Returns jump part (if exists)
        """
        if self.instructionType() == self.C_INSTRUCTION:
            semicolon_pos = self.curr_instruction.find(";")
            if semicolon_pos != -1:
                return self.curr_instruction[semicolon_pos + 1:].strip()
            else:
                return ""
