def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    middle = list(filter(lambda x: x == elem, s))
    right = list(filter(lambda x: x > elem, s))
    return quick_sort(left) + middle + quick_sort(right)


def k_closest_points(n, k, points):
    points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    return points[:k]


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        n, k = map(int, lines[0].split())
        points = [tuple(map(int, line.split())) for line in lines[1:n + 1]]

    closest_points = k_closest_points(n, k, points)
    result = ",".join(f"[{x},{y}]" for x, y in closest_points)
    print(result)

    with open("output.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
