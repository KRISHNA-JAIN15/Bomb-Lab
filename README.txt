####Bomb Defusal Game####

Description
This is a Python-based Bomb Defusal Game that consists of multiple phases. 
Each phase involves solving riddles, decoding Morse code, and performing programming challenges in C and Assembly. 
The objective is to solve all phases to defuse the bomb. Incorrect answers or incomplete tasks will trigger a simulated explosion!

### Phase 1: Password Retrieval
- Retrieve the password from `key.txt`.
- Use ubuntu commands to find the key.
- Run the bomb lab and enter the correct password.

### Phase 2: Implement `isEven(int x)`
- Complete the function in `solution.c`.
- The function should returns 1 if x is even, and 0 otherwise.
- Compile with: gcc -o solution solution.c

### Phase 3: Secret Value Retrieval
- Compile and Run the Assembly Code.
- Find the rax Value

### Phase 4: Message Decryption
- Decrypt the Encrypted Message.
- Enter the Decrypted Message

### Phase 5: Morse Code Decoding
- Decode the Morse Code.
- Enter the Decoded Word

### Phase 6: Riddle Solving
- Solve the Assigned Riddles.

### Phase 7: Encrypted Image Mystery
- Find Hidden Messages.
- Reveal the Secret Key

@@@@@@@@@@@@@@
#### Run the round using ./bomb_lab 
@@@@@@@@@@@@@@
///////////////////////////////////////////

@@Instructions to Install all dependencies@@

sudo apt update
sudo apt install -y build-essential gdb manpages-dev
sudo apt install python3 gcc nasm gdb
sudo apt install figlet toilet
sudo apt install ruby
sudo gem install lolcat
sudo apt install alsa-utils
python3 -m pip install pillow

gcc --version
gdb --version
nasm --version


////////////Morse code////////////////////////

'a': '#@', 'b': '@###', 'c': '@#@#', 'd': '@##', 'e': '#',
'f': '##@#', 'g': '@@#', 'h': '####', 'i': '##', 'j': '#@@@',
'k': '@#@', 'l': '#@##', 'm': '@@', 'n': '@#', 'o': '@@@',
'p': '#@@#', 'q': '@@#@', 'r': '#@#', 's': '###', 't': '@',
'u': '##@', 'v': '###@', 'w': '#@@', 'x': '@##@', 'y': '@#@@',
'z': '@@##', '0': '@@@@@', '1': '#@@@@', '2': '##@@@',
'3': '###@@', '4': '####@', '5': '#####', '6': '@####',
'7': '@@###', '8': '@@@##', '9': '@@@@#'

////////////Find Key///////////////////////////

Display the contents of a file
    cat filename.txt

Change to a specific directory
    cd /path/to/directory

Move up one directory
    cd ..

////////////Compile Assembly Code//////////////

nasm -f elf64 -o asm_phase.o asm_phase.asm
ld -o asm_phase asm_phase.o  # Link the object file
chmod +x asm_phase            # Make it executable

gdb ./asm_phase
(gdb) break _start
(gdb) run
(gdb) disassemble _start
(gdb) info registers
(gdb) stepi * 2



////////////Compile C Code//////////////
Open a File
   nano filename.c
Common Commands:

   Save changes: Ctrl + O (then press Enter to confirm)
   Exit nano: Ctrl + X
   Cut text: Ctrl + K
   Paste text: Ctrl + U
   Search for text: Ctrl + W

gcc -o solution solution.c
chmod +x solution  # Make it executable


///////////////Decode Image////////////
exiftool image.png

nano encoded_message.txt
//Write Hidden message in file
base64 -d encoded_message.txt > hidden_message.txt
cat hidden_message.txt



