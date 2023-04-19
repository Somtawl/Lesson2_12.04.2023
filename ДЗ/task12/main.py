s = int(input("Введите суммг чисел "))
p = int(input("Введите произведение чисел "))
for i in range(s+p):
    for y in range(s*p):
        if s == i+y and p == i*y:
            print("x =",i ,"y =",y)
            quit()
print("Нет решения")