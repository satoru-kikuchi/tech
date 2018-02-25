from random import randint


a = randint(0, 100)
b = randint(0, 100)
if a > b:
    bigger = a
else:
    bigger = b
    
text = f"{a}と{b}では、{bigger}が大きい"
print(text)
