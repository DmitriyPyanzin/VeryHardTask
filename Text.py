a = "2x**2+4x+5"
a1 = "4x**2+5x+9"
b = a.split('+')
b1 = a1.split('+')
lst = list()
lst1 = list()
lst2 = list()


for string in b:
    for i in string:
        lst.append(int(i))
        break
print(lst)

for string in b1:
    for i in string:
        lst1.append(int(i))
        break
print(lst1)

for i in range(len(b)):
    lst2.append(lst[i] + lst1[i])
print(lst2)