# 普通功能(function): 功能(對象)
# 專屬功能(method): 型態.功能()
s = "hello" * 5
b = s.replace("hello", "bye", 3)
print(s)
print(b)
s = s.replace("hello", "good")
print(s)

s = "2022-05-25"
date_split = s.split("-")
print(date_split)

new = "/".join(date_split)
print(new)

# list method
l = [2, 3, 4]
b = l.append(200)
print(l)
print(b)

# Error1: print(l.append(1000))
# Fatal Error: l = l.append(2000)
l.append(10000)
print(l)

# 2種
# str: b = s.replace  s: old   b: new
# list b = s.append   s: new   b: None