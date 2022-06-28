"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module is a recursive top-down parser, as described in section 10.1.4.

CompilationEngine first generates tokens (JackTokenizer), then uses them to
generate symbol tables (SymbolTable), and finally writes the compiled output
(VMWriter).  
"""

import typing
from tokenizer import JackTokenizer
from tables import SymbolTable
from writer import VMWriter


class CompilationEngine:
    def __init__(self, input_file: typing.TextIO, 
                output_file: typing.TextIO) -> None:
        """
        Initialize the compilation engine to parse Jack grammar (Figure 10.5)
        """
        self.tokenizer = JackTokenizer(input_file)
        self.symbol_table = SymbolTable()
        self.vm_writer = VMWriter(output_file)
        
        self.current_class_name = None
        self.current_subroutine_name = None
        self.label_counter = 0

        self.compileClass() # every Jack program starts with token class
        
    def compileClass(self) -> None:
        """
        Compile a complete class; self.tokenizer.curr_token = "class"
        """
        self.current_class_name = self.tokenizer.advance()
        self.tokenizer.advance() # '{' symbol
        self.tokenizer.advance()
        while self.tokenizer.all_tokens[self.tokenizer.token_index] in ("field", "static"):
            self.compileClassVarDec()
            
        while self.tokenizer.all_tokens[self.tokenizer.token_index] in ("method", "function", "constructor"):
            self.compileSubroutine()
        self.tokenizer.advance()

    def compileClassVarDec(self) -> None:
        """
        Compile a static variable declaration or a field declaration
        """
        kind = self.tokenizer.all_tokens[self.tokenizer.token_index]
        type_ = self.tokenizer.advance()
        while self.tokenizer.all_tokens[self.tokenizer.token_index] != ';':
            name = self.tokenizer.advance
            #name = self.tokenizer.all_tokens[self.tokenizer.token_index]
            self.symbol_table.define(name, type_, kind)
            self.tokenizer.advance
        self.tokenizer.advance() # jump over ';'
        
    def compileSubroutine(self) -> None:
        """
        Compile a complete method, function, or constructor.
        """
        self.symbol_table.reset()
        if self.tokenizer.keyWord() == self.tokenizer.CONSTRUCTOR:
            self.tokenizer.advance() 
            self.current_subroutine_name = self.tokenizer.advance()
            self.tokenizer.advance()
        elif self.tokenizer.keyWord() == self.tokenizer.METHOD:
            self.symbol_table.define("this", self.current_class_name, 
                                        self.symbol_table.ARG)
            self.tokenizer.advance() # cur_token = return type
            self.current_subroutine_name = self.tokenizer.advance() # method name
            self.tokenizer.advance() # curr_toke = '('
        else:
            self.tokenizer.advance()
            self.current_subroutine_name = self.tokenizer.advance()
            self.tokenizer.advance()
        self.tokenizer.advance()
        self.compileParameterList()
        self.tokenizer.advance() # curr_token = '{'
        self.compileSubroutineBody()
        
    def compileParameterList(self) -> None:
        """
        Compile a parameter list, except parenthesis tokens
        """
        nVars = 0
        while self.tokenizer.all_tokens[self.tokenizer.token_index] != ")":
            if self.tokenizer.all_tokens[self.tokenizer.token_index] == ",":
                self.tokenizer.advance()
            else:
                type_ = self.tokenizer.all_tokens[self.tokenizer.token_index]
                name = self.tokenizer.advance()
                self.symbol_table.define(name, type_,
                                        self.symbol_table.ARG)
                nVars += 1
                self.tokenizer.advance()
        return nVars
        
    def compileSubroutineBody(self) -> None:
        """
        Compile a subroutine's body.
        """
        self.tokenizer.advance()
        while self.tokenizer.keyWord() == self.tokenizer.VAR:
            self.compileVarDec()
        self.vm_writer.writeFunction(self.current_class_name + '.' + 
        self.current_subroutine_name, 
        self.symbol_table.index[self.tokenizer.VAR])
        if self.current_subroutine_name == "new":
            self.vm_writer.writePush(self.vm_writer.CONSTANT,
                                      self.symbol_table.index[self.tokenizer.FIELD])
            self.vm_writer.writeCall("Memory.alloc", 1)
            self.vm_writer.writePop(self.vm_writer.POINTER, 0)
        elif self.symbol_table.typeOf("this"): # not None
            self.vm_writer.writePush(self.vm_writer.ARGUMENT, 0)
            self.vm_writer.writePop(self.vm_writer.POINTER, 0)
        self.compileStatements()
        self.tokenizer.advance()
        
    def compileVarDec(self) -> None:
        """
        Compile a var declararion.
        """
        type_ = self.tokenizer.advance()
        name = self.tokenizer.advance()
        self.symbol_table.define(name, type_, self.tokenizer.VAR)
        while self.tokenizer.advance() == ',':
            name = self.tokenizer.advance()
            self.symbol_table.define(name, type_, self.tokenizer.VAR)
        self.tokenizer.advance()
    
    def compileStatements(self) -> None:
        """
        Compile a squence of statements, except curly brackets
        """
        while self.tokenizer.keyWord() in ("let", "if", "while", "do", "return"):
            if self.tokenizer.keyWord() == self.tokenizer.LET:
                self.compileLet()
            if self.tokenizer.keyWord() == self.tokenizer.IF:
                self.compileIf()
            if self.tokenizer.keyWord() == self.tokenizer.WHILE:
                self.compileWhile()
            if self.tokenizer.keyWord() == self.tokenizer.DO:
                self.compileDo()
                self.vm_writer.writePop(self.vm_writer.TEMP, 0)
            if self.tokenizer.keyWord() == self.tokenizer.RETURN:
                self.compileReturn()
            self.tokenizer.advance()
        
    def compileLet(self) -> None:
        """
        Compiles a let statement
        """
        is_array = False
        while curr_token := self.tokenizer.advance() != '=':
            if self.tokenizer.tokenType() == self.tokenizer.IDENTIFIER or\
                    (self.tokenizer.tokenType() == self.tokenizer.KEYWORD
                     and self.tokenizer.keyWord() == self.tokenizer.THIS):
                name = curr_token
                if self.tokenizer.advance() == '[':
                    is_array = True
                    if self.symbol_table.kindOf(name):
                        self.vm_writer.writePush(
                        self.symbol_table.kindOf(name),
                        self.symbol_table.indexOf(name))
                    self.tokenizer.advance()
                    self.tokenizer.advance()
                    self.compileExpression()
                    self.vm_writer.writeArithmetic("add")
                    break
        if is_array:
            self.tokenizer.advance()
            self.tokenizer.advance()
        else:
            self.tokenizer.advance()
        self.compileExpression()
        if not is_array:
            self.vm_writer.writePop(self.symbol_table.kindOf(name),
                                     self.symbol_table.indexOf(name))
        else:
            self.vm_writer.writePop(self.vm_writer.TEMP, 0)
            self.vm_writer.writePop(self.vm_writer.POINTER, 1)
            self.vm_writer.writePush(self.vm_writer.TEMP, 0)
            self.vm_writer.writePop(self.vm_writer.THAT, 0)
        
    def compileIf(self) -> None:
        """
        Compile an if statement, possibly with a trailing else clause
        """
        self.tokenizer.advance()
        self.tokenizer.advance()
        
        self.compileExpression()
        
        self.tokenizer.advance()
        self.tokenizer.advance()
        
        self.vm_writer.writeArithmetic("not")
        
        label1 = self.current_subroutine_name + "." + "if-cond-false." + \
                    str(self.label_counter)
        label2 = self.current_subroutine_name + "." + "if-cond-true." + \
                    str(self.label_counter)     
        self.label_counter += 1
        
        self.vm_writer.writeIf(label1)
        self.compileStatements()
        self.vm_writer.writeGoto(label2)
        self.vm_writer.writeLabel(label1)

        # if the condition has an else statement too
        if self.tokenizer.advance() == "else":
            self.tokenizer.advance()
            self.tokenizer.advance()
            self.tokenizer.advance()
            self.compileStatements()

        self.vm_writer.writeLabel(label2)
        
    def compileWhile(self) -> None:
        """
        Compile a while statement.
        """
        self.tokenizer.advance()
        self.tokenizer.advance()
        
        label1 = self.current_subroutine_name + "." + "while-cond-true." +\
                    str(self.label_counter)
        label2 = self.current_subroutine_name + "." + "while-cond-false." +\
                    str(self.label_counter)
        self.label_counter += 1
        
        self.vm_writer.writeLabel(label1)
        self.compileExpression()
        self.vm_writer.write_arithmetic("not")
        
        self.vm_writer.writeIf(label2)
        self.tokenizer.advance()
        self.tokenizer.advance()
        
        self.compileStatements()
        self.vm_writer.writeGoto(label1)
        self.vm_writer.writeLabel(label2)
        
    def compileDo(self) -> None:
        """
        Compile a do statement
        """
        if self.tokenizer.advance() != ";":
            #self.compile_subroutine_call()
            if method_name := self.tokenizer.advance() == '(':
                self.tokenizer.advance()
                #self.tokenizer.advance()
                self.vm_writer.writePush(self.vm_writer.POINTER, 0)
                nArgs = self.compileExpressionList() # below
                self.vm_writer.writeCall(self.current_class_name + "." +
                                        method_name, nArgs+1)   
            if object_name := self.tokenizer.advance() == '.':
                if self.symbol_table.typeOf(object_name): # not None
                    self.vm_writer.writePush(
                    self.symbol_table.kindOf(object_name),
                    self.symbol_table.indexOf(object_name))
                
                self.tokenizer.advance()
                method_name = self.tokenizer.advance()
                
                self.tokenizer.advance()
                #self.tokenizer.advance()
                nArgs = self.compileExpressionList()
                
                if type_ := self.symbol_table.typeOf(object_name): # not None
                    self.vm_writer.writeCall(type_ + "." + 
                                                method_name, nArgs+1)
                else:
                    self.vm_writer.writeCall(object_name + "." + 
                                                method_name, nArgs)
        self.tokenizer.advance()
        
    def compileReturn(self) -> None:
        """
        Compile a return statement
        """
        if self.tokenizer.advance() != ";":
            self.compileExpression()
        else:
            self.vm_writer.writePush(self.vm_writer.CONSTANT, 0)
        self.vm_writer.writeReturn()
        
    def compileExpression(self) -> None:
        """
        Compile an expression
        """
        self.compileTerm()
        ops = []
        while curr_token := self.tokenizer.advance() in ('+', '-', '*', '/',
                                                    '&', '|', '<', '>', "="):
            ops.append(curr_token)
            self.tokenizer.advance()
            self.compileTerm()
        for op in ops[::-1]:  # infix to postfix notation
            if op == '+':
                self.vm_writer.writeArithmetic("add")
            elif op == '-':
                self.vm_writer.writeArithmetic("sub")
            elif op == '*':
                self.vm_writer.writeArithmetic("call Math.multiply 2")
            elif op == '/':
                self.vm_writer.writeArithmetic("call Math.divide 2")
            elif op == '&':
                self.vm_writer.writeArithmetic("and")
            elif op == '|':
                self.vm_writer.writeArithmetic("or")
            elif op == '<':
                self.vm_writer.writeArithmetic("lt")
            elif op == '>':
                self.vm_writer.writeArithmetic("gt")
            elif op == '=':
                self.vm_writer.writeArithmetic("eq")
        
    def compileTerm(self) -> None:
        """
        Compile a term.
        - If the current token is an identifier, the routine must resolve it
          into a variabler, an array element, or a subroutine call.
        - A single lookahead token, which may be [, (, or ., suffices to
          distinguish between the possiblities
        - Any other token is not part of this term, and should not be 
          advanced over
        """
        
        curr_token = self.tokenizer.all_tokens[self.tokenizer.token_index]
        if self.tokenizer.tokenType() == self.tokenizer.STRING_CONST:
            curr_token = curr_token[1:-1]
            nArgs = len(curr_token)
            self.vm_writer.writePush(self.vm_writer.CONSTANT, nArgs)
            self.vm_writer.writeCall("String.new", 1)
            for letter in curr_token:
                self.vm_writer.writePush(self.vm_writer.CONSTANT, ord(letter))
                self.vm_writer.writeCall("String.appendChar", 2)
        elif self.tokenizer.keyWord in (self.tokenizer.NULL,
                                        self.tokenizer.FALSE):
            self.vm_writer.writePush(self.vm_writer.CONSTANT, 0)
        elif self.tokenizer.keyWord == self.tokenizer.TRUE:
            self.vm_writer.writePush(self.vm_writer.CONSTANT, 1)
            self.vm_writer.writeArithmetic("neg")
        elif self.tokenizer.keyWord == self.tokenizer.THIS:
            self.vm_writer.writePush(self.vm_writer.POINTER, 0)
        elif self.tokenizer.tokenType() == self.tokenizer.INT_CONST:
            self.vm_writer.writePush(self.vm_writer.CONSTANT, curr_token)
        elif curr_token in ('-', '~'):
            self.tokenizer.advance()
            self.compileTerm() # RECUSRION!
            if curr_token == '-':
                self.vm_writer.writeArithmetic("neg")
            else:
                self.vm_writer.writeArithmetic("not")
        elif curr_token in ("(", "["):
            self.tokenizer.advance()
            self.compileExpression()
        elif curr_token := self.tokenizer.advance() in ['.', '(']:
            #self.compile_subroutine_call()
            if method_name := self.tokenizer.advance() == '(':
                self.tokenizer.advance()
                #self.tokenizer.advance()
                self.vm_writer.writePush(self.vm_writer.POINTER, 0)
                nArgs = self.compileExpressionList() # below
                self.vm_writer.writeCall(self.current_class_name + "." +
                                        method_name, nArgs+1)   
            if object_name := self.tokenizer.advance() == '.':
                if self.symbol_table.typeOf(object_name): # not None
                    self.vm_writer.writePush(
                    self.symbol_table.kindOf(object_name),
                    self.symbol_table.indexOf(object_name))
                
                self.tokenizer.advance()
                method_name = self.tokenizer.advance()
                
                self.tokenizer.advance()
                #self.tokenizer.advance()
                nArgs = self.compileExpressionList()
                
                if type_ := self.symbol_table.typeOf(object_name): # not None
                    self.vm_writer.writeCall(type_ + "." + 
                                                method_name, nArgs+1)
                else:
                    self.vm_writer.writeCall(object_name + "." + 
                                                method_name, nArgs)
        elif curr_token := self.tokenizer.advance() == '[':
            self.vm_writer.writePush(self.symbol_table.kindOf(curr_token),
                                    self.symbol_table.indexOf(curr_token))
            self.tokenizer.advance()
            self.tokenizer.advance()
            self.compileExpression()
            self.vm_writer.writeArithmetic("add")
            self.vm_writer.writePop(self.vm_writer.POINTER, 1)
            self.vm_writer.writePush(self.vm_writer.THAT, 0)
        else:
            if self.symbol_table.kindOf(curr_token):
                self.vm_writer.writePush(
                self.symbol_table.kindOf(curr_token),
                self.symbol_table.indexOf(curr_token))
        
    def compileExpressionList(self) -> int:
        """
        Compile a comma separated list of expressions.
        Returns the number of expressions in the list.
        """
        nArgs = 0
        curr_token = self.tokenizer.advance()
        while curr_token != ')':
            self.compileExpression()
            nArgs += 1
            if curr_token == ',':
                curr_token = self.toeknizer.advance()
        return nArgs
        
