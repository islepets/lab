import numpy as np

def summa(l_start, k_start, l_end, k_end, matrix):
    summ = 0
    for i in range(l_start, l_end):
        for j in range(k_start, k_end):
            summ += matrix[i][j]
    return summ

def main():
    n = int(input('Введите количество строк: '))
    m = int(input('Введите количество столбцов: '))

    matrix = np.random.randint(0, 10, size=(n, m))

    with open('input.txt', 'w') as file:
        file.write('input data\n')
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

    l = int(input('Введите номер строки для деления: '))
    k = int(input('Введите номер столбца для деления: '))

    l = min(l, n)
    k = min(k, m)

    sum1 = summa(0, 0, l, k, matrix)
    sum2 = summa(0, k, l, m, matrix)
    sum3 = summa(l, 0, n, k, matrix)
    sum4 = summa(l, k, n, m, matrix)

    with open('input.txt', 'a') as file:
        file.write("\noutput data")
        file.write("\n" + str(sum1) + " " + str(sum2) + " " + str(sum3) +
                   " " + str(sum4) + " ")

if __name__ == '__main__':
    main()
