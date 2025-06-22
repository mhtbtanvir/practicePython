import random

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
          "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print("Welcome to the Password Generator!")

nmbrofletters = int(input("How many letters you want?:"))
nmbrofNumbers = int(input("How many numbers You Want?:"))
nmbrofSymbols = int(input("How many symbols you want?:"))

password = ""  # variable
for char in range(0, nmbrofletters):
    password += random.choice(letter)
for char in range(0, nmbrofNumbers):
    password += random.choice(number)
for char in range(0, nmbrofSymbols):
    password += random.choice(symbols)

password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)  # convert a list to a string
print(f"your password is : {final_password}")
print(f"list = {password_list}")
print(f"string in order = {password}")
