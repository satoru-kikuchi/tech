class Car:
    # クラス変数
    maker = "PEACH"
    count = 0
    
    # 初期化メソッド
    def __init__(self, color="while"):
        self.color = color
        self.mileage = 0
        
    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)
        