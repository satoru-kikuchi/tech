def calc(num):
    unit_price = 180
    if num.isdigit():
        price = int(num) * unit_price
        return price
    else:
        return None
    
while True:
    num = input("個数を入れてください（qで終了）")
    if num == "":
        continue
    elif num == "q":
        break
    
    result = calc(num)
    print(result)
