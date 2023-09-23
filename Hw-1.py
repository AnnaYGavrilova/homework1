numbers = list(map(int, input("Введите ряд чисел ").split()))
for x in numbers:
    if x % 2 == 0:
        print(x, end=" ")
    if x == 237:
        break
