// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// EQUAL
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE0
D;JEQ
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

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// EQUAL
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE1
D;JEQ
@SP
A=M-1
D=M
A=A-1
M=0
@END1
0;JMP
(TRUE1)
@SP
A=M-1
D=M
A=A-1
M=-1
(END1)
@SP
M=M-1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// EQUAL
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE2
D;JEQ
@SP
A=M-1
D=M
A=A-1
M=0
@END2
0;JMP
(TRUE2)
@SP
A=M-1
D=M
A=A-1
M=-1
(END2)
@SP
M=M-1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
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
@X_NEG3
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN3
D;JGT
@FALSE3
0;JMP
(X_NEG3)
@SP
A=M-1
D=M
@TRUE3
D;JGT
(SAME_SIGN3)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE3
D;JLT
(FALSE3)
@SP
A=M-1
D=M
A=A-1
M=0
@END3
0;JMP
(TRUE3)
@SP
A=M-1
D=M
A=A-1
M=-1
(END3)
@SP
M=M-1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
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
@X_NEG4
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN4
D;JGT
@FALSE4
0;JMP
(X_NEG4)
@SP
A=M-1
D=M
@TRUE4
D;JGT
(SAME_SIGN4)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE4
D;JLT
(FALSE4)
@SP
A=M-1
D=M
A=A-1
M=0
@END4
0;JMP
(TRUE4)
@SP
A=M-1
D=M
A=A-1
M=-1
(END4)
@SP
M=M-1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
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
@X_NEG5
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN5
D;JGT
@FALSE5
0;JMP
(X_NEG5)
@SP
A=M-1
D=M
@TRUE5
D;JGT
(SAME_SIGN5)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE5
D;JLT
(FALSE5)
@SP
A=M-1
D=M
A=A-1
M=0
@END5
0;JMP
(TRUE5)
@SP
A=M-1
D=M
A=A-1
M=-1
(END5)
@SP
M=M-1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// GT
@SP
A=M-1
A=A-1
D=M
@X_NEG6
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN6
D;JGT
@TRUE6
0;JMP
(X_NEG6)
@SP
A=M-1
D=M
@FALSE6
D;JGT
(SAME_SIGN6)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE6
D;JGT
(FALSE6)
@SP
A=M-1
D=M
A=A-1
M=0
@END6
0;JMP
(TRUE6)
@SP
A=M-1
D=M
A=A-1
M=-1
(END6)
@SP
M=M-1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// GT
@SP
A=M-1
A=A-1
D=M
@X_NEG7
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN7
D;JGT
@TRUE7
0;JMP
(X_NEG7)
@SP
A=M-1
D=M
@FALSE7
D;JGT
(SAME_SIGN7)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE7
D;JGT
(FALSE7)
@SP
A=M-1
D=M
A=A-1
M=0
@END7
0;JMP
(TRUE7)
@SP
A=M-1
D=M
A=A-1
M=-1
(END7)
@SP
M=M-1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// GT
@SP
A=M-1
A=A-1
D=M
@X_NEG8
D;JLT
@SP
A=M-1
D=M
@SAME_SIGN8
D;JGT
@TRUE8
0;JMP
(X_NEG8)
@SP
A=M-1
D=M
@FALSE8
D;JGT
(SAME_SIGN8)
@SP
A=M-1
D=M
A=A-1
M=M-D
D=M
@TRUE8
D;JGT
(FALSE8)
@SP
A=M-1
D=M
A=A-1
M=0
@END8
0;JMP
(TRUE8)
@SP
A=M-1
D=M
A=A-1
M=-1
(END8)
@SP
M=M-1

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
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

// push constant 112
@112
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

// NEG
@SP
A=M-1
D=M
M=-D

// AND
@SP
A=M-1
D=M
A=A-1
M=M&D
@SP
M=M-1

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// OR
@SP
A=M-1
D=M
A=A-1
M=M|D
@SP
M=M-1

// NOT
@SP
A=M-1
M=!M

