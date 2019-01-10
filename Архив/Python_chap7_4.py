import random
n = random.randint(1,10)
a = 99

print ("ВВЕДИ X ЧТОБЫ ВЫЙТИ")
while True:
    a = input('Введи любое число от 1 до 10: ')
    if a == "x":
        break
    if int(a) == n:
        print("ВЫ УГАДАЛИ!")
        break
    print("На самом деле число было:", n)
    print("Попробуйте еще раз.")
    n = random.randint(1,10)
