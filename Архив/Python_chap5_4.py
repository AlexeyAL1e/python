# словарь
slovar = {"рост":195,
          "цвет":"фиолетовый",
          "актер":"Бред Питт",
          "девайс":"Macbook",
          "жена":"Мария"}

per = input("введите запрос:")
if per in slovar:
    vivod = slovar[per]
    print (vivod)
else:
    print("Не найдено.")



