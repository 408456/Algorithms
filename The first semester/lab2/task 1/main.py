def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge_two_list(left, right)


def main():
    with open("input.txt", "r") as f:
        n = int(f.readline().strip())
        arr = list(map(int, f.readline().strip().split()))
        print(n, arr)

    sorted_arr = merge_sort(arr)

    with open("output.txt", "w+") as f:
        f.write(" ".join(map(str, sorted_arr)) + "\n")
        f.seek(0)
        print(f.read())


if __name__ == "__main__":
    main()
