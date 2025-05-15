from lab4.ClassCallCenter import CallCenter

def main():
    k = int(input('Куда будем выводить: 1 - консоль, 2 - файл\n'))
    flag = k == 2

    c = int(input('Введите номер задания: '))
    call_center = CallCenter.load_calls_from_csv('data.csv')

    if c == 1:
        result = call_center.count_files('D:/IDE/PyCharm Community Edition 2024.2.1/projects/pythonProject/lab3')
        output = f"Количество файлов в директории: {result}"

    elif c == 2:
        sorted_calls = call_center.sort_str()
        output = "\n".join(str(call) for call in sorted_calls.values())

    elif c == 3:
        sorted_calls = call_center.sort_ch()
        output = "\n".join(str(call) for call in sorted_calls.values())

    elif c == 4:
        param = input('Введите Да/Нет ')
        filtered_calls = call_center.sort_param(param)
        output = "\n".join(str(call) for call in filtered_calls.values())

    if flag:
        with open('answer.txt', 'w', encoding='utf-8') as file:
            file.write(output)
    else:
        print(output)

if __name__ == '__main__':
    main()
