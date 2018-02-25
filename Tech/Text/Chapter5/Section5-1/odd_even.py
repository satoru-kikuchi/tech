from random import randint


num = randint(0, 100)
if num % 2:
    result = "奇数"
else:
    result = "偶数"
    
print(num, result)
