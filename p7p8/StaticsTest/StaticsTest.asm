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

// writing function Class1.set 0
(Class1.set)
@0
D=A
@R13
M=D
(LOOP_Class1.set)
@END_LOOP_Class1.set
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
@LOOP_Class1.set
0;JMP
(END_LOOP_Class1.set)

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

// pop static 0
@Class1.0
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

// pop static 1
@Class1.1
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

// push constant 0
@0
D=A
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

// writing function Class1.get 0
(Class1.get)
@0
D=A
@R13
M=D
(LOOP_Class1.get)
@END_LOOP_Class1.get
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
@LOOP_Class1.get
0;JMP
(END_LOOP_Class1.get)

// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class1.1
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

// writing function Class2.set 0
(Class2.set)
@0
D=A
@R13
M=D
(LOOP_Class2.set)
@END_LOOP_Class2.set
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
@LOOP_Class2.set
0;JMP
(END_LOOP_Class2.set)

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

// pop static 0
@Class2.0
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

// pop static 1
@Class2.1
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

// push constant 0
@0
D=A
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

// writing function Class2.get 0
(Class2.get)
@0
D=A
@R13
M=D
(LOOP_Class2.get)
@END_LOOP_Class2.get
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
@LOOP_Class2.get
0;JMP
(END_LOOP_Class2.get)

// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class2.1
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

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing call Class1.set2
@Class1.set$ret.0
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
@2
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Class1.set
@Class1.set
0;JMP
(Class1.set$ret.0)

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

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// Writing call Class2.set2
@Class2.set$ret.0
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
@2
D=D-A
@ARG
M=D
// repositions local
@SP
D=M
@LCL
M=D
// Writing goto Class2.set
@Class2.set
0;JMP
(Class2.set$ret.0)

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

// Writing call Class1.get0
@Class1.get$ret.0
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
// Writing goto Class1.get
@Class1.get
0;JMP
(Class1.get$ret.0)

// Writing call Class2.get0
@Class2.get$ret.0
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
// Writing goto Class2.get
@Class2.get
0;JMP
(Class2.get$ret.0)

// Writing Label Sys.init.WHILE
(Sys.init.WHILE)

// Writing goto Sys.init.WHILE
@Sys.init.WHILE
0;JMP

