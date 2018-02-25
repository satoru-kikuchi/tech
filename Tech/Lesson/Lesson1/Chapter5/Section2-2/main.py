import sys

x = 0

while True:
    x += 1
    if x < 2:
        print(x)
        continue
    if x == 2:
        print("素数")
        continue

    y = 3
    isPrime = True
    while y**2 <= x:
        if x % y == 0:
            print(x)
            isPrime = False
            break
        y = y + 2
        
    if isPrime:
        print("素数")