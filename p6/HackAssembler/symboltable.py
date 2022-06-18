"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference 
because I lack experience working with OOP and Python.

This is SymbolTable module that maintains the correspondence between symbols
and their meanings (RAM and ROM addresses)
"""

class SymbolTable:
    DEFAULT_START_MEM_ADDR = 16

    def __init__(self) -> None:
        """
        The assembler creates a symbol table and initializes it with 
        all the predefined symbols and their pre-allocated values.
        The predefined symbols of Hack assembly programs (section 6.2.2).
        Also, the variable symbols are mapped to consecutive RAM locations 
        as they are first encountered, starting at RAM address 16.
        """
        self.symbol_table = {
            "R0": 0, "R1": 1 ,"R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6,
            "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, 
            "R13": 13, "R14": 14, "R15": 15, "SP": 0, "LCL": 1, "ARG": 2,
            "THIS": 3, "THAT": 4, "SCREEN": 16384, "KBD": 24576
        }
        self.next_empty_memory = self.DEFAULT_START_MEM_ADDR
        
    def addEntry(self, symbol: str, address: int) -> None:
        """
        adds <symbol, address> to the table
        """
        self.symbol_table[symbol] = address
        
    def contains(self, symbol: str) -> bool:
        """
        checks if the table contains the given symbol.
        """
        return symbol in self.symbol_table
        
    def getAddress(self, symbol: str) -> int:
        """
        returns the address associated with the symbol
        """
        return self.symbol_table[symbol]
