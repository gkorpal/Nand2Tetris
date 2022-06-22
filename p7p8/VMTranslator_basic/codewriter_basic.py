"""
Author: Gaurish Korpal
I used https://github.com/OrrMatzkin/nand2tetris-Minesweeper as reference
because I lack experience working with OOP and Python.

This module translates a parse VM command into Hack assembly code.
This is a basic version which lacks start-up code implementation.
"""

import typing

class CodeWriter:
    def __init__(self, output_file: typing.TextIO) -> None:
        """
        Prepares the output_file to write into.
        No bootstrap code.
        """
        self.output_file = output_file
        self.filename = None # same as empty string ""
        self.label_counter = 0    # keeping track of L_INSTRUCTIONS
        self.functionName = ""
        self.function_calls_num = dict()
    
    def setFileName(self, fileName: str) -> None:
        """
        Informs that the translation of a new VM file has started.
        """
        self.fileName = fileName
        
    def writeArithmetic(self, command: str) -> None:
        """
        Writes to the output_file the assembly code that implements
        the given arithmetic-logical command, see chapter 4 and fig 7.5
        """
        asm_commands = ""
        if command == "add":
            asm_commands = ["// ADD",
                            "@SP",
                            "A=M-1",
                            "D=M",
                            "A=A-1",
                            "M=M+D",
                            "@SP",
                            "M=M-1"]
        elif command == "sub":
            asm_commands = ["// SUB",
                            "@SP",
                            "A=M-1",
                            "D=M",
                            "A=A-1",
                            "M=M-D",
                            "@SP",
                            "M=M-1"]
        elif command == "neg":
            asm_commands = ["// NEG",
                            "@SP",
                            "A=M-1",
                            "D=M",
                            "M=-D"]
        elif command == "eq":
            asm_commands = ["// EQUAL",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=M-D",
                              "D=M",
                              "@TRUE" + str(self.label_counter),
                              "D;JEQ",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=0",
                              "@END" + str(self.label_counter),
                              "0;JMP",
                              "(TRUE" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=-1",
                              "(END" + str(self.label_counter) + ")",
                              "@SP",
                              "M=M-1"]
        elif command == "gt":
            asm_commands = ["// GT",
                              "@SP",
                              "A=M-1",
                              "A=A-1",
                              "D=M",
                              "@X_NEG" + str(self.label_counter),
                              "D;JLT",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "@SAME_SIGN" + str(self.label_counter),
                              "D;JGT",
                              "@TRUE" + str(self.label_counter),
                              "0;JMP",
                              "(X_NEG" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "@FALSE" + str(self.label_counter),
                              "D;JGT",
                              "(SAME_SIGN" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=M-D",
                              "D=M",
                              "@TRUE" + str(self.label_counter),
                              "D;JGT",
                              "(FALSE" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=0",
                              "@END" + str(self.label_counter),
                              "0;JMP",
                              "(TRUE" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=-1",
                              "(END" + str(self.label_counter) + ")",
                              "@SP",
                              "M=M-1"]
        elif command == "lt":
            asm_commands = ["// LT",
                              "@SP",
                              "A=M-1",
                              "A=A-1",
                              "D=M",
                              "@X_NEG" + str(self.label_counter),
                              "D;JLT",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "@SAME_SIGN" + str(self.label_counter),
                              "D;JGT",
                              "@FALSE" + str(self.label_counter),
                              "0;JMP",
                              "(X_NEG" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "@TRUE" + str(self.label_counter),
                              "D;JGT",
                              "(SAME_SIGN" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=M-D",
                              "D=M",
                              "@TRUE" + str(self.label_counter),
                              "D;JLT",
                              "(FALSE" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=0",
                              "@END" + str(self.label_counter),
                              "0;JMP",
                              "(TRUE" + str(self.label_counter) + ")",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=-1",
                              "(END" + str(self.label_counter) + ")",
                              "@SP",
                              "M=M-1"]
        elif command == "and":
            asm_commands = ["// AND",
                               "@SP",
                               "A=M-1",
                               "D=M",
                               "A=A-1",
                               "M=M&D",
                               "@SP",
                               "M=M-1"]
        elif command == "or":
            asm_commands = ["// OR",
                              "@SP",
                              "A=M-1",
                              "D=M",
                              "A=A-1",
                              "M=M|D",
                              "@SP",
                              "M=M-1"]
        elif command == "not": 
            asm_commands = ["// NOT",
                               "@SP",
                               "A=M-1",
                               "M=!M"]                     
        else:
            asm_commands = "COMMAND DOES NOT EXIST"
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        self.label_counter += 1
        
    def writePushPop(self, command: str, segment: str, index: int) -> None:
        """
        Write the assembly code that implements the given push or pop command
        section 7.3 (also table 7.4) and table in section 7.4.1
        """
        asm_commands = ""
        if command == "push":
            if segment == "argument":
                asm_commands = ["// push argument " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@ARG",
                                "A=M+D",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "local":
                asm_commands = ["// push local " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@LCL",
                                "A=M+D",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "static":
                asm_commands = ["// push static " + str(index),
                                "@" + self.fileName + "." + str(index),
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "constant":
                asm_commands = ["// push constant " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "this":
                asm_commands = ["// push this " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@THIS",
                                "A=M+D",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "that":
                asm_commands = ["// push that " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@THAT",
                                "A=M+D",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
            elif segment == "pointer":
                if index == 0:
                    asm_commands = ["// push pointer this",
                                    "@THIS",
                                    "D=M",
                                    "@SP",
                                    "A=M",
                                    "M=D",
                                    "@SP",
                                    "M=M+1"]
                elif index == 1:
                    asm_commands = ["// push pointer that",
                                    "@THAT",
                                    "D=M",
                                    "@SP",
                                    "A=M",
                                    "M=D",
                                    "@SP",
                                    "M=M+1"]
            elif segment == "temp":
                asm_commands = ["// push temp " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@5",
                                "A=A+D",
                                "D=M",
                                "@SP",
                                "A=M",
                                "M=D",
                                "@SP",
                                "M=M+1"]
        elif command == "pop":
            if segment == "argument":
                asm_commands = ["// pop argument " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@ARG",
                                "A=M+D",
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
            elif segment == "local":
                asm_commands = ["// pop local " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@LCL",
                                "A=M+D",
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
            elif segment == "static":
                asm_commands = ["// pop static " + str(index),
                                "@" + self.fileName + "." + str(index),
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
            elif segment == "this":
                asm_commands = ["// pop this " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@THIS",
                                "A=M+D",
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
            elif segment == "that":
                asm_commands = ["// pop that " + str(index),
                                "@" + str(index),
                                "D=A",
                                "@THAT",
                                "A=M+D",
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
            elif segment == "pointer":
                if index == 0:
                    asm_commands = ["// pop pointer this",
                                    "@SP",
                                    "M=M-1",
                                    "A=M",
                                    "D=M",
                                    "@THIS",
                                    "M=D"]
                elif index == 1:
                    asm_commands = ["// pop pointer that",
                                    "@SP",
                                    "M=M-1",
                                    "A=M",
                                    "D=M",
                                    "@THAT",
                                    "M=D"]
            elif segment == "temp":
                asm_commands = ["// pop temp " + str(index),
                                "@" + str(5 + index),
                                "D=A",
                                "@R13",
                                "M=D",
                                "@SP",
                                "M=M-1",
                                "A=M",
                                "D=M",
                                "@R13",
                                "A=M",
                                "M=D"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        
    def writeLabel(self, label: str) -> None:
        """
        Write assembly code that effects the label command
        section 8.2, 8.4
        """
        asm_commands = ["// Writing Label " + label,
                        "(" + label + ")"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        
    def writeGoto(self, label: str) -> None:
        """
        Write assembly code that effects the goto command
        section 8.2, 8.4
        """
        asm_commands = ["// Writing goto " + label,
                        "@" + label,
                        "0;JMP"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        
    def writeIf(self, label: str) -> None:
        """
        Write assembly code that effects the if-goto command
        section 8.2, 8.4
        """
        asm_commands = ["// Writing if-goto " + label,
                        "@SP",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@" + label,
                        "D;JNE"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        
    def writeFunction(self, functionName: str, nVars: int) -> None:
        """
        Write assembly code that effects the function command
        Figure 8.5
        """
        self.functionName = functionName
        asm_commands = ["// writing function " + functionName + " " + str(nVars),
                        "(" + functionName + ")",
                        "@" + str(nVars),
                        "D=A",
                        "@R13",
                        "M=D",
                        "(LOOP_" + functionName + ")",
                        "@END_LOOP_" + functionName,
                        "D;JEQ",
                        "// push constant " + str(0),
                        "@" + str(0),
                        "D=A",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "@R13",
                        "M=M-1",
                        "D=M",
                        "@LOOP_" + functionName,
                        "0;JMP",
                        "(END_LOOP_" + functionName + ")"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')

    
    def writeCall(self, functionName: str, nArgs: int) -> None: 
        """
        Write assembly code that effects the call command
        figure 8.6
        """
        asm_commands = ["// Writing call " + functionName + str(nArgs),
                        "@" + functionName + "$ret." + str(self.function_calls_num[functionName]),
                        "D=A",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "// push local",
                        "@LCL",
                        "D=M",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "// push argument",
                        "@ARG",
                        "D=M",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "// push this",
                        "@THIS",
                        "D=M",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "// push that",
                        "@THAT",
                        "D=M",
                        "@SP",
                        "A=M",
                        "M=D",
                        "@SP",
                        "M=M+1",
                        "// reposition argument",
                        "@SP",
                        "D=M",
                        "@5",
                        "D=D-A",
                        "@" + str(nArgs),
                        "D=D-A",
                        "@ARG",
                        "M=D",
                        "// repositions local",
                        "@SP",
                        "D=M",
                        "@LCL",
                        "M=D",
                        "// Writing goto " + functionName,
                        "@" + functionName,
                        "0;JMP",
                        "(" + functionName + "$ret." +
                                 str(self.function_calls_num[functionName]) + ")"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
    
    def writeReturn(self) -> None:
        """
        Write assembly code that effects the return command
        figure 8.3
        """
        asm_commands = ["// writing return",
                        "// endFrame = LCL",
                        "@LCL",
                        "D=M",
                        "@R14",
                        "M=D",
                        "// retAddr = *(endFrame - 5)",
                        "@R14",
                        "D=M",
                        "@5",
                        "A=D-A",
                        "D=M",
                        "@R15",
                        "M=D",
                        "// *ARG = pop()",
                        "@SP",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@ARG",
                        "A=M",
                        "M=D",
                        "// SP = ARG +1",
                        "@ARG",
                        "D=M+1",
                        "@SP",
                        "M=D",
                        "@R14",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@THAT",
                        "M=D",
                        "@R14",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@THIS",
                        "M=D",
                        "@R14",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@ARG",
                        "M=D",
                        "@R14",
                        "M=M-1",
                        "A=M",
                        "D=M",
                        "@LCL",
                        "M=D",
                        "// goto retAddr",
                        "@R15",
                        "A=M",
                        "0;JMP"]
        for instruction in asm_commands:
            self.output_file.write(instruction + '\n')
        self.output_file.write('\n')
        
    def close(self) -> None:
        """Closes the output file."""
        self.output_file.close()
