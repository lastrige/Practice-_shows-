items=[]
while True:
    val = int(input('Введите для включения в список '))
    if val == 0:
        break
    items.append(val)
print(items)