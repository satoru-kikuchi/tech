
result = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 5 == 0 else "Buzz" if i % 3 == 0 else i for i in range(1, 301)]
print(result)

list = []
for i in range(1, 301):
    if i % 15 == 0:
        list.append("FizzBuzz")
    else:
        if i % 3 == 0:
            list.append("Fizz")
        else:
            if i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(i)
print(list)
