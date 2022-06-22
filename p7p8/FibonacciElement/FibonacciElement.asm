// Writing bootstrap
@256
D=A
@SP
M=D

// Writing call Sys.init0
@Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push argument
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push this
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition argument
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Sys.init
@Sys.init
0;JMP
(Sys.init$ret.0)

// writing function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@R13
M=D
(LOOP_Main.fibonacci)
@END_LOOP_Main.fibonacci
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
@LOOP_Main.fibonacci
0;JMP
(END_LOOP_Main.fibonacci)

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

// LT
@SP
A=M-1
A=A-1
D=M
@X_NEG0
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN0
D;JGT
@FALSE0
0;JMP
(X_NEG0)
@SP
A=M-1
D=M
@TRUE0
D;JGT
(SAME_SIGN0)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE0
D;JLT
(FALSE0)
@SP
A=M-1
D=M
A=A-1
M=0
@END0
0;JMP
(TRUE0)
@SP
A=M-1
D=M
A=A-1
M=-1
(END0)
@SP
M=M-1

// Writing if-goto Main.fibonacci.IF_TRUE
@SP
M=M-1
A=M
D=M
@Main.fibonacci.IF_TRUE
D;JNE

// Writing goto Main.fibonacci.IF_FALSE
@Main.fibonacci.IF_FALSE
0;JMP

// Writing Label Main.fibonacci.IF_TRUE
(Main.fibonacci.IF_TRUE)

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

// Writing Label Main.fibonacci.IF_FALSE
(Main.fibonacci.IF_FALSE)

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

// Writing call Main.fibonacci1
@Main.fibonacci$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push argument
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push this
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition argument
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.0)

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

// Writing call Main.fibonacci1
@Main.fibonacci$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push argument
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push this
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition argument
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
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

// writing function Sys.init 0
(Sys.init)
@0
D=A
@R13
M=D
(LOOP_Sys.init)
@END_LOOP_Sys.init
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
@LOOP_Sys.init
0;JMP
(END_LOOP_Sys.init)

// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing call Main.fibonacci1
@Main.fibonacci$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push argument
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push this
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition argument
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Main.fibonacci
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)

// Writing Label Sys.init.WHILE
(Sys.init.WHILE)

// Writing goto Sys.init.WHILE
@Sys.init.WHILE
0;JMP

