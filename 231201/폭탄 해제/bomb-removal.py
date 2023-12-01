class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

bomb1 = Bomb("branch","G",34)

print(f"code : {bomb1.code}\ncolor : {bomb1.color}\nsecond : {bomb1.sec}")