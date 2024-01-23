import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

print("Password Generator!")

n_letters = int(input("Please input the number of letters\n"))
n_numbers = int(input("Please input the number of numbers\n"))
n_symbols = int(input("Please input the number of symbols\n"))

password_list = []

for char in range(1, n_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, n_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, n_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your random password is: {password}")
