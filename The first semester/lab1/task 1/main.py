def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


with open("input.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    n = int(lines[0].strip())
    arr = list(map(int, lines[1].strip().split()))

insertion_sort(arr)

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, arr)))

with open("output.txt", "r") as f:
    print(f.read())
