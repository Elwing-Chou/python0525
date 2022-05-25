# 四大基礎: 1. 數字 2. 字串 3. 布林 4. 無
# 1. 數字
a = 2
b = 2.0
import decimal
ans = decimal.Decimal("0.3") / decimal.Decimal("0.1")
print(ans)

# 2. 字串
print("abc" * 5)
s = "abcde"
print(s[0])
# !!!!!反向索引
print(s[len(s)-1], s[-1])
# 字串[開始索引:結束索引(不包含)]
print(s[1:3])
print(s[1:-1])
# 字串[開始:結束(不包含):幾個一跳]
print(s[::2])
print(s[1::2])
# !!!跳號可以是負的(開始要比結束右邊)
print(s[3:1:-1])
# !!!!!!!!
print(s[::-1])

print("apple" == "apple")

# 3. 布林
a = True
b = False

print(not 6 > 5)
print(not "ap" in "apple")

# 而且: and 或者: or
# 2 < a < 10
a = 5
print(2 < a < 6)
print(a > 2 and a < 6)
print(a > 3 or a < -2)

# 4. 無
a = None
print(a == None)
# 瑣碎
# is: == 進階, 不僅值相等, 還必須是同一個東西
print(a is None)
print(not a is None)
print(a is not None)
