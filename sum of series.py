print("Нахождение суммы ряда.")
print("Исходные значения должны быть в формате: L ε S")
print("L – начальная сумма, ε – количество знаков после запятой (точность), S - искомая сумма ряда")
choise = input("Прочитать файл(0) или продолжить в терминале(1): ")

if choise == "0":
    f = open("file.txt", "r+")
    enter_list = f.read().split()
    start_sum = float(enter_list[0])
    final_sum = float(enter_list[2])
    eps = pow(10, -int(enter_list[1]))

    sum = start_sum
    n = 1
    while final_sum - sum > eps:
        sum += 1/pow(n, 2)
        n += 1
    f.write(f"\nThe sum of the series is {sum}\n It took {n - 1} iterations.")
    f.close()
    print("Результат записан в исходный файл.")
else:
    print("Введите исходные значения: ")
    enter_list = input().split()

    start_sum = float(enter_list[0])
    final_sum = float(enter_list[2])
    eps = pow(10, -int(enter_list[1]))

    sum = start_sum
    n = 1
    while final_sum - sum > eps:
        sum += 1/pow(n, 2)
        n += 1
    print(f"Сумма ряда: {sum}\n Понадобилось {n - 1} итераций.")



