# random モジュールのrandinit関数を読み込む
from random import randint


point = randint(0, 100)
# 判定
if point >= 100:
    result = "Aクラス"
elif point >= 60:
    result = "Bクラス"
elif point >= 30:
    result = "Cクラス"
else:
    result = "不合格"

print(result)