from random import randint


tickets = 5
fmt = "{:>3}"
point = 0
while tickets > 0:
    v = randint(1, 20)
    print(fmt.format(v))
    point += v
    tickets -= 1
    
print("-" * 3)
print(fmt.format(point))
