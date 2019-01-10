import csv

firstList = ["Звёздные войны", "Терминатор", "Искусственный интеллект"]
secondList = ["Дурак", "Матильда", "Левиафан"]
thirdList = ["Люди в чёрном", "Я - робот", "Эволюция"]

commonList = [firstList, secondList, thirdList]

with open("commonList.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in commonList:
        w.writerow(i)
