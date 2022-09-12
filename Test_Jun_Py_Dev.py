import re

#Прочитал файл и вывел в список
with open('PythonTest.txt', 'r', encoding='utf-8') as file:
    list1 = []
    for line in file:
        list1.append(line.strip().replace('\t', ' '))

#Преобразовал список в строку для работы с регулярными выражениями
string = (" ".join(list1))

#Функция для английских слов
def List_eng_word():
    for i in string:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            List_eng_word = re.findall(r"(?i)[\d+a-zA-Z\s]+", string)
            if List_eng_word:
                word_eng = list(filter(len, map(str.strip, List_eng_word)))
                return word_eng


with open('English.txt', 'w', encoding='utf-8') as file:
    for word in List_eng_word():
        file.write(word)
        file.write('\n')

#Функция для русских слов
def List_ru_word():
    for i in string:
        if i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            List_ru_word = re.findall(r"(?i)[+а-яА-Я\s]+", string)
            if List_ru_word:
                word_ru = list(filter(len, map(str.strip, List_ru_word)))
                return word_ru


with open('Russian.txt', 'w', encoding='utf-8') as file:
    for word in List_ru_word():
        file.write(word)
        file.write('\n')



