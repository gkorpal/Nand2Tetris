# Nand2Tetris

Platform: Fedora Linux 36 (Workstation Edition) 

Java (OpenJDK): `sudo dnf install java-17-openjdk-17.0.3.0.7-1.fc36.x86_64`

Create symbolic links for the software tools:
````
$ mkdir ~/bin
$ cd ~/bin
$ ln -s ~/nand2tetris/tools/HardwareSimulator.sh HardwareSimulator
$ chmod +x HardwareSimulator
$ ln -s ~/nand2tetris/tools/CPUEmulator.sh CPUEmulator
$ chmod +x CPUEmulator
$ ln -s ~/nand2tetris/tools/VMEmulator.sh VMEmulator
$ chmod +x VMEmulator
$ ln -s ~/nand2tetris/tools/Assembler.sh Assembler
$ chmod +x Assembler
$ ln -s ~/nand2tetris/tools/JackCompiler.sh JackCompiler
$ chmod +x JackCompiler
````
