# Password-Generator-Manager
import random

u_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ';', ':', '?', '/', '\\', '|', '`']

new_pw = []
pw_length = int(input("Enter your desired password length: "))

# Make and if statement, asking if there are specfics to the password characters. 
# If the answer is no, then go directly to the next step, generating the PW.    
# Ask how many u_letters are needed?
# Ask how many numbers are needed?
# How many symbols are needed?
# l_letters can automatically fill rest that is needed. 


while len(new_pw) < pw_length:
    r_list = random.choice([u_letters, l_letters, numbers, symbols])
    r_char = random.choice(r_list)
    new_pw.append(r_char)

new_pw = ''.join(new_pw)
print(f"Your new password is: {new_pw}")
# The next step it to be more specific on how many characters I can choose in every list
