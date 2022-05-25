def add2number(n1, n2):
    return n1 + n2

print(add2number(3, 4))

# https://docs.python.org/zh-tw/3/reference/datamodel.html#basic-customization
# 物件導向: 自訂型態
# 1. value 2. method
class Point:

    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def d_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "(x, y) = ({}, {})".format(self.x, self.y)

p1 = Point(3, 4)
distance = p1.d_from_origin()
# str(p1) -> p1.__str__()
print(p1)
print(distance)