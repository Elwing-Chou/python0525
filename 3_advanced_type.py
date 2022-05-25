# 四大群集型態
# 1. List(清單): 一群同類型的東西
l = [80, 30, 60, 50]
# 語法ok, 但習慣上很差 [20, "eh", 30, "hi"]
# 清單操作跟字串很像
# key-value: key -> value
# str/list: key被自動產生(0, 1, 2, ...)
# 只要有key: 查詢操作 東西[key]
print(l[0], l[-1], l[::-1])
print(len(l))
print(sorted(l, reverse=True))
# !!! 這個沒有複製一份
a = l
a[0] = 2000
print(a, l)
# !!! 這個有複製一份
a = l[:]
a[0] = 10000
print(a, l)