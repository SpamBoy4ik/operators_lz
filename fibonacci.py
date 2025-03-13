print("Нахождение n-го члена ряда Фибоначчи.")
print("Исходные значения должны быть в формате: N")
print("N - номер искомого члена ряда Фибоначчи")
choise = input("Прочитать файл(0) или продолжить в терминале(1): ")

if choise == "0":
    file = open('file.txt', 'r+')
    n = int(file.read())
    f_number1 = 0 # число Фибоначчи 1
    f_number2 = 1
    for i in range(1, n):
        temp = f_number1
        f_number1 = f_number2
        f_number2 = f_number2 + temp
    file.write("\n" + str(f_number2))
    file.close()
    print("Результат записан в исходный файл.")
else:
    n = int(input("Введите номер искомого члена ряда Фибоначчи: "))
    f_number1 = 0 # число Фибоначчи 1
    f_number2 = 1
    for i in range(1, n):
        temp = f_number1
        f_number1 = f_number2
        f_number2 = f_number2 + temp
    print(f_number2)