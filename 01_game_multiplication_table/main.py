import random

score = 0

for _ in range(3):
    num_1 = random.randint(2, 9)
    num_2 = random.randint(2, 9)
    result = num_1 * num_2
    while True:
        try:
            input_user = input(f"Сколько будет {num_1}x{num_2} = ")
            result_user = int(input_user)
            break
        except ValueError:
            print(f"Вы ввели {input_user} - это не число!")

    if result_user == result:
        score += 1
        print("Верно!")
    else:
        print(f"Неверно! правильный ответ: {result}")

result_percent = round(score / 3 * 100, 2)
print()
print(f"Игра окончена!")
print(f"Количество очков: {score} из 3")
print(f"Процент правильных ответов: {result_percent} %")