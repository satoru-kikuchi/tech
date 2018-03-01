# スーパークラス
class Great():
    def hello(self):
        print("やあ！")
        
    def bye(self):
        print("さようなら")
        

# サブクラス
class Great2(Great):
    def hello(self, name=None):
        if name:
            print(name + "さん、こんにちは！")
        else:
            super().hello()
            