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
    # if answer is yes, repeat the program
    # if no, end the program