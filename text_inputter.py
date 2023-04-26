# Ken Leam G. Gamboa
# BSCPE 1-5
# This program will ask for the user's input, 
# then the inputted message will be appended to an assigned text file.

import time
import pyfiglet
# print the title
PROGRAM_TITLE = "T E X T  F I L E  I N P U T T E R"
print("\033[1m" + "\033[96m" + pyfiglet.figlet_format(PROGRAM_TITLE.center(70), font= "mini")) 

# open a text file
with open("mylife.txt", "a") as file_input:
    # ask for user's message input
    text_message = str(input("\nInput a message: "))
    # append user's input into the text file
    file_input.write(text_message + "\n")
# ask user if they want to input another message
try_again = str(input("\nDo you want to input another message into the text file? (yes/no): "))
try_again = try_again.lower()
while True:
    # if answer is yes, repeat the program
    if try_again == "yes":
        with open("mylife.txt", "a") as file_input:
            text_message = str(input("\nInput a message: "))
            file_input.write(text_message + "\n")
        try_again = str(input("\nDo you want to input another message into the text file? (yes/no): "))
        try_again = try_again.lower()
    # if no, end the program
    elif try_again == "no":
        break
    # if invalid program, ask the user again
    else:
        print("\033[1m" + "\nINVALID INPUT\n")
        time.sleep(1)
        try_again = str(input("Do you want to input another message into the text file? (yes/no): "))
        try_again = try_again.lower()

END_PROGRAM = "END"
time.sleep(1)
print ("\n" + "\033[1m" + END_PROGRAM.center(90, "-"))
