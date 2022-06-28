"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module enables accessing the input one token at a time and parses the 
type of each token, as defined by the Jack grammar.
"""

import typing
import re

class JackTokenizer:
    """
    The Jack language tokens fall into 5 categories.
    see Figure 10.2 and Figure 10.5
    """
    # defining constants. can change them to any value.
    KEYWORD = "keyword"
    SYMBOL = "symbol"
    IDENTIFIER = "identifier"
    INT_CONST = "integerConstant"
    STRING_CONST = "stringConstant"
    # keywords, Fig 9.6
    # program components
    CLASS = "class" 
    METHOD = "method"
    FUNCTION = "function"
    CONSTRUCTOR = "constructor"
    # primitive types, section 9.3.2
    INT = "int"
    BOOLEAN = "boolean"
    CHAR = "char" 
    VOID = "void"
    # variable delarations, Figure 9.7
    VAR = "var" # local
    STATIC = "static"
    FIELD = "field"
    # statements, Fig 9.8
    LET = "let"
    DO = "do"
    IF = "if"
    ELSE = "else"
    WHILE = "while"
    RETURN = "return"
    # constant values
    TRUE = "true"
    FALSE = "false"
    NULL = "null"
    # object reference
    THIS = "this"   
    
    
    def __init__(self, input_file: typing.TextIO) -> None:
        """
        gets ready to tokenize the input .jack file
        Skips over white space and comments, Figure 9.6
        Separates the input file into Jack's valid tokens
        """
        self.all_tokens = []
        self.token_index = 0
        self.curr_token = ""
        line = input_file.readline()
        c_regex = "^\s*(\w+)"
        s_regex = "^\s*({|}|\(|\)|\[|\]|\.|,|;|\+|-|\*|\/|\&|\||<|>|=|~|\^|#)"
        q_regex = "^\s*(\"[^\"]*\")"
        comment_flag = False
        while line:
            start = 0
            while_flag = True
            while while_flag or symbol or chars or quote or \
                    comment_line or comment_para_start or comment_para_end:
                while_flag = False
                comment_line = re.search("^\s*\/\/", line[start:])
                comment_para_start = re.search("^\s*\/\*", line[start:])
                comment_para_end = re.search("^\s*\*\/", line[start:])
                chars = re.search(c_regex, line[start:])
                symbol = re.search(s_regex, line[start:])
                quote = re.search(q_regex, line[start:])
                if comment_line:
                    break
                elif comment_para_start:
                    comment_flag = True
                    start += comment_para_start.end()
                elif comment_para_end:
                    comment_flag = False
                    start += comment_para_end.end()
                elif symbol:
                    if not comment_flag:
                        self.all_tokens.append(symbol.group(1))
                    start += symbol.end()
                elif chars:
                    if not comment_flag:
                        self.all_tokens.append(chars.group(1))
                    start += chars.end()
                elif quote:
                    if not comment_flag:
                        self.all_tokens.append(quote.group(1))
                    start += quote.end()
                else:
                    if comment_flag and line.find("*/") >= 0:
                        start = line.find("*/")
                        while_flag = True
            line = input_file.readline()
        
        
    def hasMoreTokens(self) -> bool:
        """
        Checks for more tokens in the input.
        """
        return self.token_index+1 < len(self.all_tokens)
        
    def advance(self) -> str:
        """
        Gets the next token from the input and makes it the current token
        This method is only called when hasMoreTokens is true.
        Initially, there is no current token.
        """
        if self.hasMoreTokens():
            self.token_index += 1
            self.curr_token = self.all_tokens[self.token_index] 
            if self.tokenType() == self.STRING_CONST:
                self.curr_token = self.curr_token[1:-1]
        return self.curr_token
        
    def tokenType(self) -> str:
        """
        Returns the current token type; Figure 10.5
        """
        self.curr_token = self.all_tokens[self.token_index]
        if self.curr_token in ('class', 'constructor', 'function', 'method',
                            'field', 'static', 'var', 'int', 'char',
                            'boolean', 'void', 'true', 'false', 'null',
                            'this', 'let', 'do', 'if', 'else', 'while',
                            'return'):
            return self.KEYWORD
        elif self.curr_token in ('{', '}', '(', ')', '[', ']', '.', ',', ';', '+',
                            '-', '*', '/', '&', '|', '<', '>', '=', '~'):
            return self.SYMBOL
        elif self.curr_token.startswith('"'):
            return self.STRING_CONST
        elif self.curr_token.isdigit():
            return self.INT_CONST
        else:
            return self.IDENTIFIER
        
    def keyWord(self) -> str:
        """
        Returns the keyword when the of current tokenType is KEYWORD
        """
        self.curr_token = self.all_tokens[self.token_index]
        if self.curr_token == "class":
            return self.CLASS
        elif self.curr_token == "method":
            return self.METHOD
        elif self.curr_token == "function":
            return self.FUNCTION
        elif self.curr_token == "constructor":
            return self.CONSTRUCTOR
        elif self.curr_token == "int":
            return self.INT
        elif self.curr_token == "boolean":
            return self.BOOLEAN
        elif self.curr_token == "char":
            return self.CHAR
        elif self.curr_token == "void":
            return self.VOID
        elif self.curr_token == "var":
            return self.VAR
        elif self.curr_token == "static":
            return self.STATIC
        elif self.curr_token == "filed":
            return self.FIELD
        elif self.curr_token == "let":
            return self.LET
        elif self.curr_token == "do":
            return self.DO
        elif self.curr_token == "if":
            return self.IF
        elif self.curr_token == "else":
            return self.ELSE
        elif self.curr_token == "while":
            return self.WHILE
        elif self.curr_token == "return":
            return self.RETURN
        elif self.curr_token == "true":
            return self.TRUE
        elif self.curr_token == "false":
            return self.FALSE
        elif self.curr_token == "null":
            return self.NULL
        elif self.curr_token == "this":
            return self.THIS
        
    def symbol(self) -> str:
        """
        Returns the symbol when the current tokenType is SYMBOL
        """
        return self.all_tokens[self.token_index]
        
    def identifier(self) -> str:
        """
        Returns the identifier when the current tokenType is IDENTIFIER
        """
        return self.all_tokens[self.token_index]
        
    def intVal(self) -> int:
        """
        Returns the integer value when the current tokenType is INT_CONST
        """
        return int(self.all_tokens[self.token_index])
        
    def stringVal(self) -> str:
        """
        Returns the string value when the current token type is STRING_CONST
        """
        return self.all_tokens[self.token_index]
