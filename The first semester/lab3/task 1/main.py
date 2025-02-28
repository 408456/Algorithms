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
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))

    sorted_arr = quick_sort(arr)
    print(" ".join(map(str, sorted_arr)))

    with open("output.txt", "w") as f:
        f.write(" ".join(map(str, sorted_arr)))


if __name__ == "__main__":
    main()
