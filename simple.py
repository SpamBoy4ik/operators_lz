print("Проверка числа на простоту.")
print("Исходные значения должны быть в формате: n")
print("n - проверяемое число")
print("Y - означает, что число простое. N - число составное.")
choise = input("Прочитать файл(0) или продолжить в терминале(1): ")

if choise == "0":
    f = open('file.txt', 'r+')
    number = int(f.read())
    if type(number) != int or number == 1:
        print("N")
    else:
        divider = 2
        while number % divider != 0:
            divider = divider + 1
        if divider == number:
            f.write("\n" + "Y")
        else:
            f.write("\n" + "N")
    f.close()
    print("Результат записан в исходный файл.")
else:
    number = int(input("Введите число: "))
    if type(number) != int or number == 1:
        print("N")
    else:
        divider = 2
        while number % divider != 0:
            divider = divider + 1
        if divider == number:
            print("Y")
        else:
            print("N")