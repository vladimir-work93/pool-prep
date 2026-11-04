import random

'''
Тренажёр таблицы умножения. Программа спрашивает примеры (5 × 7 = ?), 
проверяет ответ, считает балл. В конце — процент правильных. При ошибке 
показывает правильный ответ и возвращает к теме. Готово: работает при любом 
вводе, включая буквы вместо цифр (защита через try/except).
'''

def return_check_int(num_user):
    while True:
        try:
            return int(num_user)
        except ValueError:
            print(f"Вы ввели {num_user} - это не число!")
            num_user = input("Попробуйте ввести значение еще раз: ")

score = 0

count_questions_user = input("Задайте количество примеров: ")
count_questions = return_check_int(count_questions_user)

for _ in range(count_questions):
    num_1 = random.randint(2, 9)
    num_2 = random.randint(2, 9)
    result = num_1 * num_2

    num_user = input(f"Сколько будет {num_1}x{num_2} = ")
    result_user = return_check_int(num_user)

    if result_user == result:
        score += 1
        print("Верно!")
    else:
        print(f"Неверно! правильный ответ: {result}")

result_percent = round(score / count_questions * 100, 2)
print()
print(f"Игра окончена!")
print(f"Количество очков: {score} из {count_questions}")
print(f"Процент правильных ответов: {result_percent} %")
