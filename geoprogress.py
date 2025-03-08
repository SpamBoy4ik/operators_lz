print("Нахождение n-го члена геометрической прогрессиии.")
choise = input("Ввод исходных данных через файл или консоль? (0 - файл, 1 - консоль)\n")

if choise == "0":
    file_name = input("Введите название файла: ")
    f = open(f'{file_name}.txt', 'r+')
    text = f.read()
    b, q, n = map(int, text.split())
    result = b * pow(q, n - 1)
    f.write("\n" + str(result))
    f.close()
    print("Результат записан в исходный файл.")
else:
    print("Введите исходные данные в формате: b q n\nb - значение первого элемента прогрессии, q - множитель прогрессии, n - номер искомого элемента")
    b, q, n = map(int, input().split()) # как правильно делать ввод нескольких
    result = b * pow(q, n - 1)
    print(result)