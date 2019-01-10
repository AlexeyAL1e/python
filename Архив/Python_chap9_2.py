nameAnswer = input("Вопрос:")

with open("question.txt", "w") as temporaryVariable:
    temporaryVariable.write(nameAnswer)
    print(temporaryVariable)
