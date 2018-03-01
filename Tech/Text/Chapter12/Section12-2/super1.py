# スーパークラス
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        

class Player(Person):
    def __init__(self, number, position):
        self.number = number
        self.position = position
        