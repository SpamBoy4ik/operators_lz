print("Нахождение n-го члена геометрической прогрессиии.")
print("Исходные значения должны быть в формате: b q n")
print("b - первый элемента прогрессии, q - множитель прогрессии, n - номер искомого элемента")
choise = input("Прочитать файл(0) или продолжить в терминале(1): ")

if choise == "0":
    f = open('file.txt', 'r+')
    enter_list = f.read().split()
    b = float(enter_list[0])
    q = float(enter_list[1])
    n = float(enter_list[2])
    result = b * pow(q, n - 1)
    f.write("\n" + str(result))
    f.close()
    print("Результат записан в исходный файл.")
else:
    print("Введите исходные данные: ")
    b, q, n = map(int, input().split()) # как правильно делать ввод нескольких
    result = b * pow(q, n - 1)
    print(result)