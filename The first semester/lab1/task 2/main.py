def insertion_sort(arr):
    n = len(arr)
    r = [0] * n
    for i in range(n):
        r[i] = i + 1

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        index = i + 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            r[j + 1] = r[j]
            j -= 1

        arr[j + 1] = key
        r[j + 1] = index

    return r


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    n = int(lines[0].strip())
    arr = list(map(int, lines[1].strip().split()))

res = insertion_sort(arr)

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, res)) + "\n")
    f.write(" ".join(map(str, arr)) + "\n")

with open("output.txt", "r") as f:
    print(f.read())
