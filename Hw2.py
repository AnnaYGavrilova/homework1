arbit = int(input("Введите произвольное число: "))
front = int(input("Введите пограничное число: "))
if arbit > front *3:
    print (arbit, end=" ,больше пограничного числа больше чем в 3 раза")
elif arbit > front:
    print(arbit, end=" больше пограничного числа" )
else: 
    print(arbit, end=" меньше пограничного числа" )

