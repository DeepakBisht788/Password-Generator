import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
x = int(input("How many letters would you like in your password?\n"))
y = int(input(f"How many symbols would you like to choose out of {len(symbols)}?\n"))
z = int(input(f"How many numbers would you like to choose out of {len(numbers)}?\n"))

# Easy Level - Order not randomised
print("Easy level")
g = ""
for i in range(0, x):
    k = random.randint(0, len(letters) - 1)
    g += letters[k]
for i in range(0, y):
    p = random.randint(0, len(symbols) - 1)
    g += symbols[p]
for i in range(0, z):
    r = random.randint(0, len(numbers) - 1)
    g += numbers[r]

print(f"Your secure Password:\n{g}")


print("Hard level")
t = []
for i in range(0, x):
    k = random.randint(0, len(letters) - 1)
    t.append(letters[k])
for i in range(0, y):
    p = random.randint(0, len(symbols) - 1)
    t.append(symbols[p])
for i in range(0, z):
    r = random.randint(0, len(numbers) - 1)
    t.append(numbers[r])

random.shuffle(t)
e = "".join(t)  # Join the list into a string
print(f"Your secure Password:\n{e}")
