from random import randint


a = randint(0, 100)
b = randint(0, 100)

if a >= 40 and b >= 40 and (a + b) >= 120:
    result = "合格"
else:
    result = "不合格"
    
text = f"a {a}、b {b}、合計{a+b}：{result}"
print(text)
