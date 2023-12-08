class Point:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num =num

n = int(input())
points = []

for i in range(1,n+1):
    x, y = tuple(map(int, input().split()))
    points.append(Point(x, y, i))

points.sort(key=lambda c: ((abs(c.x)+abs(c.y)), c.num))

for point in points:
    print(point.num)