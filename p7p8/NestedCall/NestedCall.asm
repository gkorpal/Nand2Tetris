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

// push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer this
@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5000
@5000
D=A
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

// Writing call Sys.main0
@Sys.main$ret.0
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
// Writing goto Sys.main
@Sys.main
0;JMP
(Sys.main$ret.0)

// pop temp 1
@6
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

// Writing Label Sys.init.LOOP
(Sys.init.LOOP)

// Writing goto Sys.init.LOOP
@Sys.init.LOOP
0;JMP

// writing function Sys.main 5
(Sys.main)
@5
D=A
@R13
M=D
(LOOP_Sys.main)
@END_LOOP_Sys.main
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
@LOOP_Sys.main
0;JMP
(END_LOOP_Sys.main)

// push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer this
@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5001
@5001
D=A
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

// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 1
@1
D=A
@LCL
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

// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 2
@2
D=A
@LCL
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

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop local 3
@3
D=A
@LCL
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

// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing call Sys.add121
@Sys.add12$ret.0
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
// Writing goto Sys.add12
@Sys.add12
0;JMP
(Sys.add12$ret.0)

// pop temp 0
@5
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

// push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1

// push local 4
@4
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

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

// ADD
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1

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

// writing function Sys.add12 0
(Sys.add12)
@0
D=A
@R13
M=D
(LOOP_Sys.add12)
@END_LOOP_Sys.add12
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
@LOOP_Sys.add12
0;JMP
(END_LOOP_Sys.add12)

// push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// pop pointer this
@SP
M=M-1
A=M
D=M
@THIS
M=D

// push constant 5002
@5002
D=A
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

// push constant 12
@12
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

