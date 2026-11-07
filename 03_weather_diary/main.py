'''
Дневник погоды. Данные температуры за месяц вводятся из файла. Программа
выводит: среднее, минимальный день, максимальный день, сколько дней было
ниже нуля. Готово: данные хранятся в списке, функции вынесены отдельно.
'''

def read_weather_data(file):
    with open(file, 'r') as file:
        content = file.readline().split()
        result = [int(elem) for elem in content]
        return result

def calculate_average(weather_list):
    result = sum(weather_list) / len(weather_list)
    return round(result, 2)

def find_min_day(weather_list):
    min_day = min(weather_list)
    day = weather_list.index(min_day) + 1
    return day

def find_max_day(weather_list):
    max_day = max(weather_list)
    day = weather_list.index(max_day) + 1
    return day

def count_subzero_days(weather_list):
    count = 0
    for day in weather_list:
        if day < 0:
            count += 1
    return count

def weather_view():
    weather_list = read_weather_data("weather.txt")
    weather_average = calculate_average(weather_list)
    min_day = find_min_day(weather_list)
    max_day = find_max_day(weather_list)
    subzero_days = count_subzero_days(weather_list)

    print(f"Средняя температура за месяц: {weather_average} ℃\n"
          f"Самый холодный день: {min_day} день\n"
          f"Самый теплый день: {max_day} день\n"
          f"Количество дней с температурой ниже нуля: {subzero_days} дней\n")

if __name__ == "__main__":
    weather_view()