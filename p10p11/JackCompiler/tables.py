"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module provides services for building, populating and using symbol tables
that keep track of the symbol properties name, type, kind and a running index
for each kind, see Figure 11.2.
"""

from tokenizer import JackTokenizer


class SymbolTable:
    """"
    Variable kinds, Figure 11.1
    Correspond to VM segments, Fig 7.4
    """
    # class-level symbol table
    STATIC = JackTokenizer.STATIC 
    FIELD = JackTokenizer.FIELD 
    # subroutine-level symbol table
    ARG = "arg" # Fig 7.4, Fig 8.2, function arguments
    VAR = JackTokenizer.VAR
    
    def __init__(self) -> None:
        """
        create new symbol tables
        """
        self.class_table = dict()
        self.subroutine_table = dict()
        self.index = {self.STATIC : 0, self.FIELD : 0, self.ARG : 0, 
                        self.VAR : 0}
        
    def reset(self) -> None:
        """
        When the compiler starts compiling a subroutine (constructor, method,
        or function) declaration, it resets the subroutine-level symbol table.
        """
        self.subroutine_table = dict()
        self.index[self.ARG] = 0
        self.index[self.VAR] = 0

    def define(self, name: str, type_: str, kind: str) -> None:
        """
        Adds to the table a new variable of the given name, type_ and kind.
        Assigns to it the index value of that kind and adds 1 to the index.
        """
        if kind in (self.STATIC, self.FIELD):
            self.class_table[name] = (type_, kind, self.index[kind])
            self.index[kind] += 1
        else:
            self.subroutine_table[name] = (type_, kind, self.index[kind])
            self.index[kind] += 1
        
    
    def varCount(self, kind: str) -> int:
        """
        Returns the number of variables of the given kind already defined in
        the table
        """
        return self.index[kind]

    def kindOf(self, name: str) -> str:
        """
        Returns the kind of the named identifier. 
        If the identifier is not found then returns NONE.
        """
        if name in self.subroutine_table:
            return self.subroutine_table[name][1]
        if name in self.class_table:
            return self.class_table[name][1]
        return None
        
    def typeOf(self, name: str) -> str:
        """
        Returns the type_ of the named variable.
        """
        if name in self.subroutine_table:
            return self.subroutine_table[name][0]
        if name in self.class_table:
            return self.class_table[name][0]
        return None
        
        
    def indexOf(self, name: str) -> int:
        """
        Returns the index of the named variable.
        """
        if name in self.subroutine_table:
            return int(self.subroutine_table[name][2])
        if name in self.class_table:
            return int(self.class_table[name][2])
        return None        
