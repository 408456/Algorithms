# Сбор подписей жильцов
# дано n отрезков [a0, b0], [a1, b1], ... [an-1, bn-1]
# найти min x, ai <= x <= b1
# Оценка стоимости алгоритма: O(n logn)
def collector(l):
    l.sort(key=lambda x: x[1]) # сортируем по b
    points = []
    last_point = None

    for a, b in l:
        if last_point is None or last_point < a:
            last_point = b
            points.append(last_point)

    return points


def file_handler(input_file, output_file):
    with open(input_file, "r") as f:
        n = int(f.readline().strip())
        l = [tuple(map(int, f.readline().split())) for _ in range(n)]

    points = collector(l)

    with open(output_file, "w") as f:
        f.write(f"{len(points)}\n")
        f.write(" ".join(map(str, points)) + "\n")


def main():
    file_handler("input.txt", "output.txt")


if __name__ == "__main__":
    main()
