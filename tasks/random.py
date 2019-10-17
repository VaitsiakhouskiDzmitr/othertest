import random
number = random.randrange(15)
x = 0
while x < 11:
    x = x+1
    print ('попробуйте угадать число , у вас  есть 10 попыток')
    a = int(input())
    print ('вы вбрали число : ' + str(a))
    if x > 10:
        print(f"у вас закончились попытки , было загадано число {number}")
    elif a == number:
        print('вы угадали число')
        break
    elif a > number:
        print('число слишком велико')
    else:
        print("число слишком мало")
