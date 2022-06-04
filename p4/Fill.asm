// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

    // n = 0; 16-bit address counter in the SCREEN array
    @n
    M=0
(LOOP)
    // check if RAM[KBD] value is non-zero; KBD = 24576
    // D = RAM[KBD]
    @KBD
    D=M
    @BLACK
    D;JGT
    @WHITE
    D;JEQ
(BLACK)
    // if (n >= 8192) goto LOOP
    @n
    D=M
    @8192
    D=D-A
    @LOOP
    D;JGE
    // *(R0 + n) = -1 
    @n
    D=M
    @SCREEN
    A=D+A
    M=-1
    // n = n + 1
    @n
    M=M+1
    // goto LOOP
    @LOOP
    0;JMP
(WHITE)
    // if (n < 0) goto LOOP; back-tracing the BLACK pixels
    @n
    D=M
    @LOOP
    D;JLT
    // *(R0 + n) = 0
    @n
    D=M
    @SCREEN
    A=D+A
    M=0
    // n = n - 1
    @n
    M=M-1
    // goto LOOP
    @LOOP
    0;JMP
    
// I followed the code in Figure 4.7
// Here R0 = SCREEN[0], top-left-corner of the screen as per the screen-memory-map
// SCREEN = 16384; 
// 8k memory after RAM[SCREEN] contains information about the 16-bit pixel array
// Eg: RAM[16384] to RAM[16415] is the first row (32 16-bit words)
// See slides to for info about accessing SCREEN bitmap array
// Here R1 = 8k = 8*1024 = 8192 = number of 16-bit blocks of pixels
