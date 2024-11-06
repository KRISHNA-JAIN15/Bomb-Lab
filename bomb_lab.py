import subprocess
import os
import random
import base64
import math
import string
import time
from PIL import Image, ImageDraw, PngImagePlugin

def countdown(seconds):
    """Display a countdown in the terminal."""
    for i in range(seconds, 0, -1):
        print(f"{i}...")
        
def show_boom_message():
    """Display 'BOOM!' with figlet and lolcat."""
    subprocess.run("figlet 'BOOM!' | lolcat", shell=True)

def show_success_message():
    """Display 'DEFUSED!' with figlet and lolcat."""
    subprocess.run("figlet 'DEFUSED!' | lolcat", shell=True)
    print("🎉 Congratulations! You successfully defused the bomb. 🎉")

def bomb_explosion():
    """Simulate bomb explosion."""
    print("💣 Tick... Tick... 💣")
    countdown(3)  # Dramatic 3-second countdown
    show_boom_message()
    print("💥 Your bomb exploded! Game over.")
    
def show_warning_message():
    print("🚨 During the execution ... multiple files will be created! 🚨")
    print("✋ If you change or edit those files, you will not be able to proceed")
    print("🚫 and hence will be disqualified! 🚫\n\n")
    
#############################################
def calculate_secret_key(x):
    """Calculates the secret key based on the formula: x^3 - 72x + 21x^2 - 11 + log(x)."""
    return x**3 - 72*x + 21*x**2 - 11 + math.log(x)

def create_nested_folders_with_hoax_keys(secret_key):
    """Creates a nested folder structure with hoax keys and places the real key in the innermost folder."""
    base_dir = "phase_1"  # Base directory name set to "phase_1"
    
    # Ensure base directory exists
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    # Create 5 levels of nested folders
    for level in range(1, 6):
        next_dir = os.path.join(base_dir, f"level_{level}")
        os.mkdir(next_dir)
        
        # Create a file in each folder
        if level <= 3:
            # Write hoax keys for levels 1 to 3
            key_file = os.path.join(next_dir, "key.txt")
            with open(key_file, "w") as f:
                f.write("Hoax key: This is not the correct key.\n")
        elif level == 4:
            # No file created in level 4
            pass
        else:  # Level 5
            # Write the secret key in level 5
            key_file = os.path.join(next_dir, "key.txt")
            with open(key_file, "w") as f:
                f.write(f"Secret key: {secret_key}\n")

def phase_1(Team_Number):
    print("=== Phase 1 ===\n")
    print("Your task is to calculate a secret key using a formula based on your input.")
    print("There are multiple folders for Phase 1")
    print("Search every folder for key")
    print("I can Bluff also .... hehehe \n \n ")

    # Check if the base directory "phase_1" already exists
    base_dir = "phase_1"
    if os.path.exists(base_dir):
        print("Folder structure already exists. Proceed to find the key in the folders. \n ")
        
        # Skip asking for team number and calculating secret key
        found_key = False
        for level in range(1, 6):  # Check levels 1 to 5 for the secret key
            key_file_path = os.path.join(base_dir, f"level_{level}", "key.txt")
            if os.path.exists(key_file_path):
                with open(key_file_path, "r") as f:
                    key_content = f.read().strip()
                    if "Secret key:" in key_content:
                        secret_key = key_content.split(": ")[1]  # Extract the secret key
                        found_key = True
                        break

        if not found_key:
            print("Could not find the secret key in existing folders. Exiting. \n")
            return False

    else:
        # Prompt user for a 3-digit team number
        x = Team_Number

        # Calculate the secret key
        secret_key = calculate_secret_key(x)

        # Create the nested folder structure with hoax keys
        create_nested_folders_with_hoax_keys(secret_key)
        print("Folders created. Now, proceed to find the key.")

    # Prompt the user to enter the secret key they found
    try:
        entered_key = float(input("Enter the secret key you found: ").strip())
        if math.isclose(entered_key, float(secret_key), rel_tol=1e-5):
            print("Phase 1 cleared!\n")
            return True
        else:
            print("Incorrect key. The bomb will now explode.")
            print("💣 You failed at Phase 1! 💣")
            bomb_explosion()
    except ValueError:
        print("Invalid input. The bomb will now explode.")
        bomb_explosion()
#############################################
def phase_2():
    print("=== Phase 2 ===\n")
    print("Your task: Implement the `isEven(int x)` function in `solution.c`.") 
    print("use nano to add your code to solution.c")
    print("Compile it with: gcc -o solution solution.c") 
    print("Run it with: ./solution \n\n")
    
    # Check if the `solution` executable exists
    if not os.path.isfile("solution"):
        print("\n🚨 File 'solution' not found! It looks like you haven't compiled your solution.")
        print("Make sure you've created 'solution.c' and compiled it with:")
        print("gcc -o solution solution.c")
        
        # Ask the user if they’ve created and compiled the file
        user_confirmation = input("\nDid you create and compile the solution file? (yes/no): ").strip().lower()
        
        # If they confirm and it’s still missing, trigger the bomb
        if user_confirmation == "yes":
            print("\nBOOM! The file 'solution' still doesn’t exist even after your confirmation.")
            print("💣 You failed at Phase 2! 💣")
            bomb_explosion()
            return

        print("\nPlease create and compile 'solution.c' correctly, then run this phase again.")
        return

    try:
        # If file exists, proceed to run and check the output
        result = subprocess.run(["./solution"], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip() == "1":
            print("Phase 2 cleared!\n")
            return True
        else:
            print("🚨 Incorrect output. Check your code in `solution.c`.")
            bomb_explosion()
    except Exception as e:
        print(f"BOOM! Error occurred: {e}")
        bomb_explosion()
#############################################
def phase_3(Team_Number):
    print("=== Phase 3 ===\n")
    print("This phase requires you to find a secret value in `rax` based on your team number.")
    print("HINT : Key will be of 4 digits")
    print("Inspect rax till its value is of 4 digits \n\n")
    # Calculate expected rax value
    secret_value = Team_Number + 1313

    # Update asm_phase.asm file with team_number
    with open("asm_phase.asm", "w") as asm_file:
        asm_file.write(f"""
; asm_phase.asm
global _start

section .data
Team_Number dq {Team_Number}  ; Team number inserted dynamically

section .text
_start:
    ; Load team number and add 1313 to create the secret value
    mov rax, [Team_Number]    ; Load team number
    add rax, 1313             ; Add 1313 to get the secret value

    ; Exit syscall
    mov rax, 60               ; syscall: exit
    xor rdi, rdi              ; exit code 0
    syscall
        """)

    print("Please compile and run the assembly code manually.")

    # Additional GDB Instructions
    print("Run the assembly code with GDB to find the value in `rax`. Commands:")
    print("  gdb ./asm_phase.o")
    print("  (gdb) break _start")
    print("  (gdb) run")
    print("  (gdb) info registers")
    print("  key will be a 4 digit rax value")

    # Prompt user to enter the rax value they found
    user_input = input("\nAfter running in GDB, enter the value in `rax`: ").strip()
    if user_input == str(secret_value):
        print("Phase 3 cleared!\n")
        return True
    else:
        print("Incorrect value in `rax`. The bomb will now explode.")
        print("💣 You failed at Phase 3! 💣")
        bomb_explosion()

###########################################
def phase_4(Team_Number):
    print("=== Phase 4 === \n")
    
    # Predefined encrypted sentences using Caesar cipher with a shift of 1
    encrypted_sentences = [
        "Uifsf jt b tfdsfu dpef!",  # There is a secret code!
        "Xjscsf bsz b tfdsfu dpef!",  # What’s up is a secret code!
        "Sfnq mfu uif mbwf!",  # Send me the love!
        "Hsbcmf mfu tfdsfu!",  # Garden has secret!
        "Ibnqmpu zpv b zfdb!",  # Aloud you a ycode!
        "Bohqmf uif xjsc!",  # Applend the wind!
        "Tfsf jg b tfdsfu!",  # There is a secret!
        "Zpv bsf efdpef qmfbt!",  # You are decoded peace!
        "Uif dpef jt b xfbs!",  # The code is a wave!
        "Sfbm b qbsu!",  # Read a part!
        "Hpef! Fwfs dpef.",  # Code! Every code.
        "Hsbcmf mfu czqb!",  # Garden has great!
        "Xjscsf zpv gspn jg!",  # What’s you from it!
        "Gsjm! Hpef sfbm!",  # Fun! Every read!
        "Mfu tbnqmf xjsc!",  # You explained wind!
    ]
    
    # Map the team number to an encrypted sentence
    index = Team_Number % len(encrypted_sentences)  # Simple mapping
    encrypted_message = encrypted_sentences[index]

    print("Caesar Cipher 🠞 -1 \n")
    print(f"Decrypt this message: {encrypted_message}")

    user_input = input("Enter the decrypted message: ").strip()
    
    # Check against the expected decrypted message
    correct_messages = [
        "There is a secret code!",
        "What’s up is a secret code!",
        "Send me the love!",
        "Garden has secret!",
        "Aloud you a ycode!",
        "Applend the wind!",
        "There is a secret!",
        "You are decoded peace!",
        "The code is a wave!",
        "Read a part!",
        "Code! Every code.",
        "Garden has great!",
        "What’s you from it!",
        "Fun! Every read!",
        "You explained wind!",
    ]
    
    if user_input in correct_messages:
        print("Phase 4 cleared!\n")
        return True
    else:
        print("💣 You failed at Phase 4! 💣")
        bomb_explosion()
##########################################

# Custom Morse code dictionary using #, @, and !
custom_morse_code_dict = {
    'a': '#@', 'b': '@###', 'c': '@#@#', 'd': '@##', 'e': '#',
    'f': '##@#', 'g': '@@#', 'h': '####', 'i': '##', 'j': '#@@@',
    'k': '@#@', 'l': '#@##', 'm': '@@', 'n': '@#', 'o': '@@@',
    'p': '#@@#', 'q': '@@#@', 'r': '#@#', 's': '###', 't': '@',
    'u': '##@', 'v': '###@', 'w': '#@@', 'x': '@##@', 'y': '@#@@',
    'z': '@@##', '0': '@@@@@', '1': '#@@@@', '2': '##@@@',
    '3': '###@@', '4': '####@', '5': '#####', '6': '@####',
    '7': '@@###', '8': '@@@##', '9': '@@@@#'
}

def display_morse_code(text):
    """Display each symbol in the custom Morse code sentence one by one, then delete the sentence."""
    morse_sentence = ''
    for letter in text:
        if letter in custom_morse_code_dict:
            morse_sentence += custom_morse_code_dict[letter] + ' '
    
    # Display each symbol one by one
    for symbol in morse_sentence:
        print(symbol, end='', flush=True)
        time.sleep(0.5)
    
    # Pause before deleting the sentence
    time.sleep(10)
    
    # Delete the entire sentence at once
    print('\r' + ' ' * len(morse_sentence) + '\r', end='', flush=True)

def phase_5(Team_Number):
    print("=== Phase 5 ===\n")
    print("Decode the Morse code displayed as symbols (#, @) into text!")
    print("You have 10 seconds to read the symbols and type the decoded text.")
    print("You will get to see it 2 times ...")
    
    # Predefined sentences to convert to Morse code
    sentences = [
        'keep calm and carry on', 'the quick brown fox jumps', 
        'a journey of a thousand miles', 'life is what you make it', 
        'to be or not to be', 'actions speak louder than words', 
        'better late than never', 'time and tide wait for none',
        'every cloud has a silver lining', 'fortune favors the brave soul', 
        'practice makes perfect in life', 'the best time is now', 
        'honesty is the best policy', 'look before you leap always', 
        'curiosity killed the curious cat', 'patience is a virtue indeed', 
        'make hay while sun shines', 'an apple a day keeps doctor', 
        'a penny saved is earned', 'absence makes heart grow fonder'
    ]
    
    # Check if the c.txt file exists
    if os.path.exists('a.txt'):
        with open('a.txt', 'r') as file:
            # Read the Base64 encoded sentence
            encoded_sentence = file.read().strip()
            # Decode the sentence
            correct_sentence = base64.b64decode(encoded_sentence).decode('utf-8')
            print("Loaded sentence from file.")
    else:
        # Prompt for team number and choose a sentence
        team_number = Team_Number
        
        # Map the team number to a sentence (you can customize this mapping)
        index = int(team_number) % len(sentences)  # Simple mapping
        correct_sentence = sentences[index]

        # Encode the sentence in Base64
        encoded_sentence = base64.b64encode(correct_sentence.encode('utf-8')).decode('utf-8')

        # Save the encoded sentence in c.txt
        with open('a.txt', 'w') as file:
            file.write(encoded_sentence)

    # Inform the user to watch carefully
    print("Watch carefully for the custom Morse code...")

    # Display the Morse code for the chosen sentence
    display_count = 0
    while display_count < 2:
        watch = input("Do you want to see the Morse code? (yes/no): ").strip().lower()
        if watch == 'yes':
            display_morse_code(correct_sentence)
            display_count += 1
        else:
            break

    # Give a hint after two tries
    if display_count >= 2:
        print(f"Hint: The sentence starts with '{correct_sentence.split()[0]}' and ends with '{correct_sentence.split()[-1]}'.")

    # Ask the user for the correct text
    user_input = input("Enter the decoded text: ").strip().lower()
    
    if user_input == correct_sentence:
        print("Phase 5 cleared!\n")
        return True
    else:
        print("💣 You failed at Phase 5! 💣")
        bomb_explosion()
####################################################################################

riddles = [
    ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "echo"),
    ("You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. What am I?", "candle"),
    ("I have keys but open no locks. I have space but no room. You can enter, but you can't go outside.", "keyboard"),
    ("What has to be broken before you can use it?", "egg"),
    ("The more you take, the more you leave behind. What am I?", "footstep"),
    ("I am not alive, but I grow. I don’t have lungs, but I need air. I don’t have a mouth, and I can drown. What am I?", "fire"),
    ("I am tall when I am young, and short when I am old. What am I?", "candle"),
    ("What comes once in a minute, twice in a moment, but never in a thousand years?", "m"),
    ("I’m light as a feather, yet the strongest man can’t hold me for much more than a minute. What am I?", "breath"),
    ("What can travel around the world while staying in a corner?", "stamp"),
    ("What begins with T, ends with T, and has T in it?", "teapot"),
    ("I am taken from a mine, and shut up in a wooden case, from which I am never released. What am I?", "pencil lead"),
    ("I can be cracked, made, told, and played. What am I?", "joke"),
    ("What has many teeth, but cannot bite?", "comb"),
    ("I can fly without wings. I can cry without eyes. Whenever I go, darkness flies. What am I?", "cloud"),
    ("I have branches, but no fruit, trunk, or leaves. What am I?", "bank"),
    ("What is so fragile that saying its name breaks it?", "silence"),
    ("I have a neck but no head, and wear a cap. What am I?", "bottle"),
    ("What can you catch but not throw?", "cold"),
    ("I can be long or short; I can be grown or bought; I can be painted or left bare; I can be round or square. What am I?", "nail")
]

# Function to assign random riddles to a team and store it in a file
def assign_riddles_to_team():
    # Filename for storing the assigned riddles
    filename = "b.txt"
    
    # Check if the file already exists (if yes, read the riddles from it)
    if os.path.exists(filename):
        with open(filename, "r") as file:
            assigned_riddles = [
                tuple(base64.b64decode(line.strip()).decode().split(" | ")) for line in file.readlines()
            ]
    else:
        # Randomly select 4 unique riddles for the team
        assigned_riddles = random.sample(riddles, 4)
        # Save the assigned riddles to the file in Base64 format
        with open(filename, "w") as file:
            for question, answer in assigned_riddles:
                encoded_line = base64.b64encode(f"{question} | {answer}".encode()).decode()
                file.write(f"{encoded_line}\n")
    
    return assigned_riddles

# Function to run the assigned riddles for the team
def run_team_riddles(assigned_riddles):
    for index, (question, correct_answer) in enumerate(assigned_riddles, start=1):
        print(f"\n=== Riddle {index} ===")
        print(question)

        for attempt in range(2):
            answer = input("Your answer: ").strip().lower()
            if answer == correct_answer:
                print("\nCorrect! You solved the riddle.\n")
                break
            else:
                if attempt == 0:
                    print("That's not quite right. Try again!")
                else:
                    print("That's your second attempt. Moving on to the next riddle.\n")
        else:
            return False  # If the user fails after two attempts

    return True  # All riddles solved

# Main function for phase 6
def phase_6():
    print("=== Phase 6 ===\n")
    print("Solve the four assigned riddles to defuse the bomb!\n")

    # Assign riddles for the team
    assigned_riddles = assign_riddles_to_team()

    # Run the riddles for the team
    if run_team_riddles(assigned_riddles):
        print("\nPhase 6 cleared!")
        return True
    else:
        print("You failed to solve all riddles. The bomb will now explode.")
        print("💣 You failed at Phase 6! 💣")
        bomb_explosion()


###############################################################################
def generate_secret_key():
    """Generate a random 4-digit number and return it as a string."""
    random_number = random.randint(1, 30)
    return str(random_number)

def save_secret_key_to_file(secret_key):
    """Save the secret key in base64 encoding with random characters appended to c.txt."""
    encoded_key = base64.b64encode(secret_key.encode()).decode()
    
    # Generate random characters to append
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    with open('c.txt', 'w') as file:
        file.write(encoded_key + random_chars)  # Append random characters

def read_secret_key_from_file():
    """Read and decode the secret key from c.txt."""
    with open('c.txt', 'r') as file:
        content = file.read().strip()
    
    # Extract only the base64 part before the random characters
    encoded_key = content[:len(content) - 8]  # Assuming last 8 characters are random
    return base64.b64decode(encoded_key).decode()

def get_secret_key():
    """Retrieve the secret key, either by generating or reading from c.txt."""
    if os.path.exists('c.txt'):
        print("Reading secret key from 'c.txt'.")
        return read_secret_key_from_file()
    else:
        print("Generating a new secret key.")
        secret_key = generate_secret_key()
        save_secret_key_to_file(secret_key)
        return secret_key

def create_images_with_hidden_texts(num_images=10):
    """Create a folder with subfolders for images containing hidden texts, if not already created."""
    main_folder = 'phase_7_images'
    
    if os.path.exists(main_folder):
        print(f"The folder '{main_folder}' already exists. Skipping image creation.")
        return

    os.makedirs(main_folder, exist_ok=True)
    
    hoax_messages = [
        "Hoax: The secret lies in the stars.",
        "Hoax: The answer is 7.",
        "Hoax: Look for the light.",
        "Hoax: Trust the process.",
        "Hoax: All roads lead to nowhere.",
        "Hoax: The cake is a lie.",
        "Hoax: Beware the Ides of March.",
        "Hoax: It's not the destination, it's the journey.",
        "Hoax: Follow the white rabbit."
    ]
    
    indices = list(range(num_images))
    random.shuffle(indices)

    secret_key = get_secret_key()  # Retrieve the secret key

    for i in range(num_images):
        subfolder = os.path.join(main_folder, f'{i + 1}_image')
        
        if os.path.exists(subfolder):
            print(f"The folder '{subfolder}' already exists. Skipping image creation for this folder.")
            continue
        
        os.makedirs(subfolder, exist_ok=True)
        
        image = Image.new('RGB', (200, 100), color='lightblue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 40), f"Image {i + 1}", fill="black")

        # Assign the secret key to the first randomized index, others get hoax messages
        if i == indices[0]:
            message = secret_key
        else:
            message = hoax_messages[i % len(hoax_messages)]
        
        encoded_message = base64.b64encode(message.encode()).decode()

        png_info = PngImagePlugin.PngInfo()
        png_info.add_text("hidden_message", encoded_message)

        image_file_path = os.path.join(subfolder, 'image.png')
        image.save(image_file_path, "PNG", pnginfo=png_info)

def reveal_message():
    """Display instructions without directly giving away the solution."""
    print("=== Phase 7: Encrypted Mystery ===\n")
    print("Your task is to find the hidden messages encoded within the images in 'phase_7_images'.")
    print("Hints:")
    print("- Each image contains a hidden message.")
    print("- Use Linux tools to extract and decode the hidden messages.")
    print("\n💡 Remember: Not everything is as it seems. Some messages are hoaxes.")
    print("Good luck!")

def attempt_reveal(secret_key):
    """Allow the user to attempt to reveal the hidden messages."""
    print("You can enter the secret key to reveal the hidden messages.")
    print("Type 'exit' to quit anytime.")

    while True:
        command = input("Enter the secret key to reveal (or type 'exit' to quit): ").strip()
        
        if command.lower() == 'exit':
            print("Exiting the command input.")
            break
        
        if command == secret_key:
            show_success_message()  # Show success message if the key is correct
            return True
        else:
            print("💣 You failed at Phase 7! 💣")
            bomb_explosion()  # Trigger bomb explosion for incorrect input

def phase_7():
    create_images_with_hidden_texts(num_images=10)
    secret_key = get_secret_key()  # Get the secret key dynamically
    reveal_message()
    attempt_reveal(secret_key)
    
#################################################################################
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("💣 Welcome to the Bomb Defusal Game! 💣\n\n")
    show_warning_message()

    # Check if the team_number.txt file exists
    if os.path.exists('team_number.txt'):
        with open('team_number.txt', 'r') as file:
            # Read the Base64 encoded team number
            encoded_team_number = file.read().strip()
            # Decode the team number
            Team_Number = int(base64.b64decode(encoded_team_number).decode('utf-8'))
            print(f"Loaded Team Number from file: {Team_Number}")
    else:
        while True:
            try:
                print("!!! Warning !!!")
                print("Be careful while entering your Team number ...")
                print("It can be entered only once \n \n")
                Team_Number = int(input("Enter your Team Number (100 - 999): ").strip())
                if 100 <= Team_Number <= 999:
                    # Encode the team number in Base64
                    encoded_team_number = base64.b64encode(str(Team_Number).encode('utf-8')).decode('utf-8')

                    # Save the encoded team number in team_number.txt
                    with open('team_number.txt', 'w') as file:
                        file.write(encoded_team_number)

                    print(f"Team Number {Team_Number} saved.")
                    break
                else:
                    print("Please enter a valid Team Number.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")  
    
    if phase_1(Team_Number):
        if phase_2():
            if phase_3(Team_Number):
                if phase_4(Team_Number):
                    if phase_5(Team_Number):
                        if phase_6():
                            if phase_7():
                                pass

if __name__ == "__main__":
    main()
