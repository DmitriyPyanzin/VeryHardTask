# # 4 домашнее задание
# # 1 task

# n = int(input('Введите 1-ое число: '))
# m = int(input('Введите 2-ое число: '))
# summaFirstDiv = 0
# summaSecondDiv = 0

# i = 1
# while i < n:
# if n % i == 0:
# summaFirstDiv += i
# i += 1
# i = 1
# while i < m:
# if m % i == 0:
# summaSecondDiv += i
# i += 1

# if summaSecondDiv == n and summaFirstDiv == m:
# print('yes')
# else:
# print('no')

# 4 домашнее задание
# 1 task

n = int(input('Введите 1-ое число: '))
m = int(input('Введите 2-ое число: '))
d = {}
resultArray = list()

for i in range(n, m + 1):
summa = 0
for j in range(1, round(i / 2) + 1):
if i % j == 0:
summa += j
d[i] = summa
for i in d:
for j in d:
if d[i] == j and d[j] == i and i != j and (i, j) not in resultArray and (j, i) not in resultArray:
resultArray.append((i, j))
for i in resultArray:
print(*i)