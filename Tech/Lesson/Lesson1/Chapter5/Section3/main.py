import random
import string

password = ""
for i in range(0, 10):
    password += string.printable[random.randint(0, len(string.printable) - 1)]
# print(password)
print(string.printable[23])