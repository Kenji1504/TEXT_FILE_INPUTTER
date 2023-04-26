# Ken Leam G. Gamboa
# BSCPE 1-5
# This program will ask for the user's input, 
# then the inputted message will be appended to an assigned text file.

# open a text file
with open("mylife.txt", "a") as file_input:
    # ask for user's message input
    text_message = str(input("Input a message: "))
    # append user's input into the text file
    file_input.write(text_message + "\n")
# ask user if they want to input another message
try_again = str(input("Do you want to input another message into the text file? (yes/no)?"))
try_again = try_again.lower()
while True:
    # if answer is yes, repeat the program
    if try_again == "yes":
        with open("mylife.txt", "a") as file_input:
            text_message = str(input("Input a message: "))
            file_input.write(text_message + "\n")
        try_again = str(input("Do you want to input another message into the text file? (yes/no)?"))
        try_again = try_again.lower()
    # if no, end the program