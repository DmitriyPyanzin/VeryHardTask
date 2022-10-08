data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)

# Вариант 1 создать ф-ю и ее применить
def where(f, col):
    return [x for x in col if f(x)]

res = where(lambda x: not x%2, res)
print(res)

# Вариант 2 использовать ф-ю filter()
res = list(filter(lambda x: not x%2, res))
print(res)