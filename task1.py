# Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.
# Остальные цифры должны заменяться звездочками

def card_hide():
    try:
        card = input("Введите номер карты :  ")
    except ValueError:
        print(ValueError)
    else:
        if card.isalpha():
            print("Ошибка! Ввод нечисловых данных")
        if card.isdigit():
            return '*' * len(card[:-4]) + card[-4:]


if __name__ == "__main__":
    print(card_hide())
