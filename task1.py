def generate_arithmetic_progression():
    a1 = int(input("Введите первый элемент прогрессии: "))
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите количество элементов: "))

    progression = [a1 + (i - 1) * d for i in range(1, n + 1)]

    return progression

progression = generate_arithmetic_progression()
print(progression)
