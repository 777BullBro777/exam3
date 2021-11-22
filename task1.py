# Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

def card_hide(card):
    try:
        card = input("Введите номер карты :  ")
    except ValueError:
        print(ValueError)
    else:
        while True:
            if card.isalpha():
                print("Ошибка! Ввод нечисловых данных")
                break
            if card.isalnum():
                return '*' * len(card[:-4]) + card[-4:]


if __name__ == "__main__":
    card = None
    print(card_hide(card))
