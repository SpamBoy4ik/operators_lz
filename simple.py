print("Проверка числа на простоту.")
choise = input("Ввод исходных данных через файл или консоль? (0 - файл, 1 - консоль)\n")

if choise == "0":
    file_name = input("Введите название файла: ")
    f = open(f'{file_name}.txt', 'r+')
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