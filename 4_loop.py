# 1. 走過一個群集(list/set/dict/tuple/str)
scores = [30, 50, 80]
for s in scores:
    print(s)
    print("-" * 30)

# 2. 固定次數
# range(5) -> (0, 1, 2, 3, 4)
# range(2, 5) -> (2, 3, 4)
# range(2, 11, 3) -> (2, 5, 8)
total = 0
for i in range(10):
    total = total + (i + 1)
print(total)

# 3. 不固定次數
# while True + break(結束)
import random
lottery = set()
while len(lottery) < 6:
    n = random.randint(1, 49)
    lottery.add(n)
print(lottery)