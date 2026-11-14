"""
Частотный анализ. Дан текстовый файл. Выведите: топ-10 слов по частоте (без учёта регистра и пунктуации),
общее число слов, число уникальных слов. Готово: решение через словарь, аккуратно обрабатывает знаки препинания.
"""

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    clean_text = []
    for char in text.lower():
        if char.isalpha() or char.isspace() or char == "-":
            clean_text.append(char)
        else:
            clean_text.append(" ")

    clean_text = "".join(clean_text).split()

    word_counts = {}

    for word in clean_text:
        if word in word_counts:
            word_counts[word] += 1
        elif word == "-":
            pass
        else:
            word_counts[word] = 1

    number_of_unique_words = len(word_counts)
    total_number_of_words = sum(word_counts.values())

    print(f"Число уникальных слов: {number_of_unique_words}\n"
          f"Общее число слов: {total_number_of_words}\n")

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    top_10_words = sorted_words[:10]

    print("ТОП-10 слов:\n")

    for i, (word, count) in enumerate(top_10_words, start=1):
        print(f"{i}-е место: {word} = {count}")