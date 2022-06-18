"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference 
because I lack experience working with OOP and Python.

This is SymbolTable module that maintains the correspondence between symbols
and their meanings (RAM and ROM addresses)
"""

class SymbolTable:
    DEFAULT_START_MEM_ADDR = 16
    """    
    Note that the __init__ method lets the class initialize the object's
    attributes. The __init__() function is called automatically every time the 
    class is being used to create a new object.
    https://docs.python.org/3/tutorial/classes.html#class-objects
    """
    def __init__(self) -> None:
        self.symbol_table = {
            "R0": 0, "R1": 1 ,"R2": 2, "R3": 3, "R4": 4, "R5": 5, "R6": 6,
            "R7": 7, "R8": 8, "R9": 9, "R10": 10, "R11": 11, "R12": 12, 
            "R13": 13, "R14": 14, "R15": 15, "SP": 0, "LCL": 1, "ARG": 2,
            "THIS": 3, "THAT": 4, "SCREEN": 16384, "KBD": 24576
        }
        self.next_empty_memory = self.DEFAULT_START_MEM_ADDR
        
    def addEntry(self, symbol: str, address: int) -> None:
        self.symbol_table[symbol] = address
    
    def updateNextEmptyMemory(self):
        self.next_empty_memory += 1
        
    def contains(self, symbol: str) -> bool:
        return symbol in self.symbol_table
        
    def getAddress(self, symbol: str) -> int:
        return self.symbol_table[symbol]

            
