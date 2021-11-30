#  Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome():
    word = input("Введите значение :  ").replace(' ', '').lower()
    if word == word[::-1]:
        print('Палиндром')
        return
    else:
        print('Не палиндром')


if __name__ == "__main__":
    palindrome()
