number_of_coins = int(input("Введите количество монет "))
coin_sides = input("Укажите стороны монет (0 или 1)")
if number_of_coins == int(len(coin_sides)):
    heads = 0
    tails = 0
    result = 0
    for i in coin_sides:
        if int(i) == 1:
            heads = heads + 1
        elif int(i) == 0:
            tails = tails + 1
        else:
            print("Неверное значение сторны монеты", i, "значение должно быть 0 или 1")
            quit()
    if heads > tails:
        result = tails
    else:
        result = heads
    print(heads, tails)
    print("Необходимо перевернуть", result, "монет")
else:
    print("Введенное количество монет и колиество сторон не совпадют")