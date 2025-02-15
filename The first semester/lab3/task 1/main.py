def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = list(filter(lambda x: x == elem, s))
    right = list(filter(lambda x: x > elem, s))
    # middle = [i for i in s if i == elem]
    return quick_sort(left) + middle + quick_sort(right)


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())  # Читаем количество элементов
        arr = list(map(int, f.readline().strip().split()))  # Читаем массив

    sorted_arr = quick_sort(arr)  # Сортируем массив
    print(" ".join(map(str, sorted_arr)))  # Выводим в консоль

    with open("output.txt", "w") as f:
        f.write(" ".join(map(str, sorted_arr)))  # Записываем в файл


if __name__ == "__main__":
    main()