num = int(input("Введите число "))
i = 1
result = [i]
while True:
    i = i * 2
    if i < num:
        result.append(i)
    else:
        break
print(result)
