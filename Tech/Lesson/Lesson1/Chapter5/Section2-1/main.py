import sys


x = 15

if x < 0:
    sys.exit()

if x == 2:
    print("素数")
    
if x % 2 == 0:
    sys.exit()

y = 3
while y**2 <= x:
    if x % y == 0:
        sys.exit()
    y = y + 2
    
print(f"{x}素数")
