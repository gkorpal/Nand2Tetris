// push argument 1
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop pointer that
@SP
M=M-1
A=M
D=M
@THAT
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 0
@0
D=A
@THAT
A=M+D
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop that 1
@1
D=A
@THAT
A=M+D
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// SUB
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

// pop argument 0
@0
D=A
@ARG
A=M+D
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// Writing Label .MAIN_LOOP_START
(.MAIN_LOOP_START)

// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// Writing if-goto .COMPUTE_ELEMENT
@SP
M=M-1
A=M
D=M
@.COMPUTE_ELEMENT
D;JNE

// Writing goto .END_PROGRAM
@.END_PROGRAM
0;JMP

// Writing Label .COMPUTE_ELEMENT
(.COMPUTE_ELEMENT)

// push that 0
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push that 1
@1
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

// pop that 2
@2
D=A
@THAT
A=M+D
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// push pointer that
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

// pop pointer that
@SP
M=M-1
A=M
D=M
@THAT
M=D

// push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// SUB
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

// pop argument 0
@0
D=A
@ARG
A=M+D
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// Writing goto .MAIN_LOOP_START
@.MAIN_LOOP_START
0;JMP

// Writing Label .END_PROGRAM
(.END_PROGRAM)

