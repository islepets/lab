import random

def _input():
    arr = []
    ch = input("Введите 1 для ручного ввода или 2 для автоматической генерации:\n")

    if ch == '1':
        print('Введите числа массива (для завершения ввода оставьте пустую строку):')
        while (el := input()) != '':
            arr.append(int(el))

    elif ch == '2':
        size = int(input("Введите размер массива для генерации: "))
        lower_bound = int(input("Введите нижнюю границу значений: "))
        upper_bound = int(input("Введите верхнюю границу значений: "))
        arr = [random.randint(lower_bound, upper_bound) for _ in range(size)]

    else:
        print("Неверный ввод. Пожалуйста, выберите 1 или 2.")

    return arr


def insert_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def main():
    arr = _input()
    if not arr:
        print("Массив пуст. Завершение программы.")
        return
    print('Отсортированный массив:')
    sort_arr = insert_sort(arr)
    print(' '.join(map(str, sort_arr)))


if __name__ == '__main__':
    main()