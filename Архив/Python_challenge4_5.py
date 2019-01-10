def f():
    """
    возвращает число в типе float
    """
    x = input ("введите число: ")
    x = float(x)
    return x

try:
    print(f())
except ValueError:
    print ("Ошибка ввода.")

