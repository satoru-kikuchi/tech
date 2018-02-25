while True:
    num = input("何個ですが？（qで終了）")
    if num == "q":
        print("終了しました")
        break
    
    try:
        price = 120 * int(num)
        print("合計金額", price)
    except:
        print("エラーです。正しい数値を入力してください")
        