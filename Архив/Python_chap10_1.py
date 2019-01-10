import random


def hangman(object_word):

    wrong_count = 0
    stages = ["",
              "________       ",
              "|       |      ",
              "|       |      ",
              "|       0      ",
              "|      /|\     ",
              "|      / \     ",
              "|              ",
              "|              "]
    list_symbols = list(object_word)
    board = ["__"] * len(object_word)
    win = False

    print("Добро пожаловать на казнь!")

    while wrong_count < len(stages) - 1:
        print("\n")
        message = "Введите букву: "
        letter = input(message)

        if letter in list_symbols:
            list_symbols_index = list_symbols.index(letter)
            # 0 = [к, о, т].index(к)

            board[list_symbols_index] = letter
            # _ _ _ [0] =  "к _ _"

            list_symbols[list_symbols_index] = '$'

        else:
            wrong_count += 1
        print((" ".join(board)))
        e = wrong_count + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("Вы выйграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong_count]))
        print("Вы проиграли! Было загадано слово {}.".format(object_word))


list_words = ["кот", "собака", "птица"]
selection_count = random.randint(1, 3)
hangman(list_words[selection_count])
