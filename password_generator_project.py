import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("----Welcome to the Python password generator----")
letters_input = int(input("How many letters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like in your password?\n"))
numbers_input = int(input("How many numbers would you like in your password?\n"))
password = []
for lets in range(1, letters_input + 1):
    random_letters = random.choice(letters)
    password += random_letters
    # print(password, end="")
for sym in range(1, symbols_input + 1):
    random_symbols = random.choice(symbols)
    password += random_symbols
    # print(password, end="")
for nums in range(1, numbers_input + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers
    # print(password, end="")
random.shuffle(password)
# print(password)
final_password = ""
for passes in password:
    final_password += passes
print(f"Here is your password: {final_password}", end="")


