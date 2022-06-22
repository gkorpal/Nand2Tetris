"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module handles the parsing of a single .vm file.
"""

import typing

class Parser:
    """
    constants defined here to avoid magic numbers
    """
    DEFAULT_START_PROG_ADDR = 0
    COMMENT_PREFIX = "//"
    C_ARITHMETIC = "arithmetic"
    C_PUSH = "push"     #push/pop command, sec 7.3
    C_POP = "pop"      #push/pop command, sec 7.3
    C_LABEL = "label"    #branching command
    C_GOTO = "goto"     #branching command, unconditional
    C_IF = "if-goto"       #branching command, conditional
    C_FUNCTION = "function" #function command, fig 8.5
    C_CALL = "call"     #function command, fig 8.5
    C_RETURN = "return"   #function command, fig 8.5
        
    def __init__(self, input_file: typing.TextIO) -> None:
        """
        Gets ready to parse the opened input_file
        arithmetic-logical commands from fig 7.5
        """
        self.input_lines = input_file.readlines()
        self.line_num = self.DEFAULT_START_PROG_ADDR
        self.curr_command = None    # same as "" empty string
        
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
        self.curr_command = \
        self.input_lines[self.line_num].split(self.COMMENT_PREFIX)[0].strip()
        while (self.curr_command == "" or
            self.curr_command.strip().startswith(self.COMMENT_PREFIX)) \
                and self.hasMoreLines():
            self.line_num += 1
            self.curr_command = \
            self.input_lines[self.line_num].split(self.COMMENT_PREFIX)[0].strip()
        self.line_num += 1
        
    def commandType(self) -> str:
        """
        Returns the type of the current instruction constant.
        """
        command_type = self.curr_command.split()[0]
        if command_type in ['add', 'sub', 'neg', 
                            'eq', 'gt', 'lt',
                            'and', 'or', 'not']:
            return self.C_ARITHMETIC
        elif command_type == "push":
            return self.C_PUSH
        elif command_type == "pop":
            return self.C_POP
        elif command_type == "label":
            return self.C_LABEL
        elif command_type == "goto":
            return self.C_GOTO
        elif command_type == "if-goto":
            return self.C_IF
        elif command_type == "function":
            return self.C_FUNCTION
        elif command_type == "call":
            return self.C_CALL
        elif command_type == "return":
            return self.C_RETURN
        else:
            return "UNKNOWN_COMMAND"
    
    def arg1(self) -> str:
        """
        This is not called if the commandType() == C_RETURN
        In case of C_ARITHMETIC the command itself is returned.
        Otherwise, it returns the first argument of the curr_command
        - "push segment index" -> "segment"
        - "pop segment index" -> "segment"
        - "label symbol" -> "symbol"
        - "goto symbol command" -> "symbol"
        - "if-goto symbol command" -> "symbol"
        - "function f nVars" -> "f"
        - "call f nArgs" -> "f"
        """
        if self.commandType() == self.C_ARITHMETIC:
            return self.curr_command.split()[0]
        else:
            return self.curr_command.split()[1]
            
    def arg2(self) -> int:
        """
        Only called when commandType() == C_PUSH, C_POP, C_FUNCTION or C_CALL
        returns the second argument of the curr_command
        """
        return int(self.curr_command.split()[2])
