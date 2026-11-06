'''
2. Число прописью. Программа принимает на вход целое число от 0 до 999 и
выводит его текстовое представление (например, 231 - это «двести тридцать один»).
Неправильно вводимые данные (буквы, пустой ввод или числа вне диапазона)
не ломают программу, а просят пользователя повторить ввод.

'''


def get_number():
    while True:
        try:
            input_user = input("Введите число от 0 до 999: ")
            number_user = int(input_user)
            if 0 <= number_user <= 999:
                return number_user
            else:
                print(f"Вы ввели число '{number_user}', которое не "
                      f"соответствует условию 0 <= X <= 999")
        except ValueError:
            print(f"Вы ввели '{input_user}', попробуйте еще "
                  f"раз: ")


def number_to_words(number):
    number_int = int(number)
    dict_units = {
        0: 'ноль',
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
        10: 'десять',
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать',
    }
    dict_tens = {
        1: 'десять',
        2: 'двадцать',
        3: 'тридцать',
        4: 'сорок',
        5: 'пятьдесят',
        6: 'шестьдесят',
        7: 'семьдесят',
        8: 'восемьдесят',
        9: 'девяносто',
    }
    dict_hundreds = {
        1: 'сто',
        2: 'двести',
        3: 'триста',
        4: 'четыреста',
        5: 'пятьсот',
        6: 'шестьсот',
        7: 'семьсот',
        8: 'восемьсот',
        9: 'девятьсот',
    }

    hundreds = number_int // 100
    tens = number_int % 100
    units = number_int % 10
    result = []

    if number_int == 0:
        return dict_units[number_int]

    if hundreds > 0:
        result.append(dict_hundreds[hundreds])
    if 1 <= tens <= 19:
        result.append(dict_units[tens])
    if 20 <= tens:
        tens = tens // 10
        result.append(dict_tens[tens])
        if units != 0:
            result.append(dict_units[units])

    return ' '.join(result)


if __name__ == "__main__":
    number = get_number()
    print(number_to_words(number))