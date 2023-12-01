class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = list(input().split())
sec = int(sec)
bomb1 = Bomb(code, color, sec)
print(f"code : {bomb1.code}\ncolor : {bomb1.color}\nsecond : {bomb1.sec}")