numlist = [3, 4.2, 10, "x", 1, 9]
sum = 0
for num in numlist:
    
    if not isinstance(num, (int, float)):
        print(num, "数値ではない値が含まれていました")
        break
    sum += sum
else:
    print("合計", sum)