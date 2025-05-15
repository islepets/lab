import csv
import os

def _dir(directory):
    count = 0
    for el in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, el)):
            count += 1
    return count

def gener_dict():
    data_dict = {}
    try:
        with open('data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 3:
                    key = row[0]
                    value = row[1:]
                    data_dict[key] = value
    except FileNotFoundError:
        print('Файл не найден')
        return data_dict
    return data_dict

def sort_ch(data_dict):
    sorted_by_ch = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
    result = []
    for key, value in sorted_by_ch.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)

def sort_str(data_dict):
    sorted_by_str = dict(sorted(data_dict.items(), key=lambda item: item[1][1][0]))
    result = []
    for key, value in sorted_by_str.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)


def sort_param(data_dict, param):
    result = []
    for key, value in data_dict.items():
        if value[2] == param:
            result.append(f'{key}: {value}')
    return '\n'.join(result)

def main():
   k = int(input('Куда будем выводить: 1 - консоль, 2 - файл\n'))
   flag = False
   if k == 2:
       flag = True

   c = int(input('Введите номер задания: '))
   result = gener_dict()

   if c == 1:
       if flag == True:
           with open('answer.txt', 'w',encoding='utf-8') as file:
               file.write(f"Кол-во файлов в директории: {_dir('D:/IDE/PyCharm Community Edition 2024.2.1/projects/pythonProject/lab3')}")
       else:
           print(f"Кол-во файлов в директории: {_dir('D:/IDE/PyCharm Community Edition 2024.2.1/projects/pythonProject/lab3')}")

   if c == 2:
       if flag == True:
           with open('answer.txt', 'w',encoding='utf-8') as file:
                file.write(sort_str(result))
       else:
           print(sort_str(result))

   if c == 3:
       if flag == True:
           with open('answer.txt', 'w',encoding='utf-8') as file:
                file.write(sort_ch(result))
       else:
           print(sort_ch(result))

   if c == 4:
       param = str(input('Введите Да/Нет '))
       if flag == True:
           with open('answer.txt', 'w',encoding='utf-8') as file:
                file.write(sort_param(result, param))
       else:
           print(sort_param(result, param))



if __name__ == '__main__':
    main()