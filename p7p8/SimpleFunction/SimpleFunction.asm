// writing function SimpleFunction.test 2
(SimpleFunction.test)
@2
D=A
@R13
M=D
(LOOP_SimpleFunction.test)
@END_LOOP_SimpleFunction.test
D;JEQ
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@R13
M=M-1
D=M
@LOOP_SimpleFunction.test
0;JMP
(END_LOOP_SimpleFunction.test)

// push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 1
@1
D=A
@LCL
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

// NOT
@SP
A=M-1
M=!M

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

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

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

// SUB
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1

// writing return
// endFrame = LCL
@LCL
D=M
@R14
M=D
// retAddr = *(endFrame - 5)
@R14
D=M
@5
A=D-A
D=M
@R15
M=D
// *ARG = pop()
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// SP = ARG +1
@ARG
D=M+1
@SP
M=D
@R14
M=M-1
A=M
D=M
@THAT
M=D
@R14
M=M-1
A=M
D=M
@THIS
M=D
@R14
M=M-1
A=M
D=M
@ARG
M=D
@R14
M=M-1
A=M
D=M
@LCL
M=D
// goto retAddr
@R15
A=M
0;JMP

